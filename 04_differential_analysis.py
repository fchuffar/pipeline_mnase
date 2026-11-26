import os
import re
exec(open("config").read())

# Differential analysis CP vs SD (replaces the R loops of 00_custom_preprocessing.sh):
#   03_count.Rmd (featureCounts, FRiP, tss_ratio)
#   03_gc_slope.Rmd (GC bias of the libraries on control tiles of gc_prefix, e_gc_slope.rds)
#   -> 04_da.Rmd (DESeq2, ewas4combp bed; lfmm latent factors e_LF<i>_*.rds) -> 04_combp.Rmd (comb-p DER, per seed threshold)
#   -> 04_der_classes.Rmd (feature classes of the DER)
#   -> 04_models.Rmd (all the models of a prefix: DER and their overlap, l2fc vs distance to TSS, l2fc correlation, tss_ratio vs status within strata)
# Models with LF<i> terms use the latent factors of the same model without them: the rule da depends on them and copies them
#   under the name read by exp_grp.R (lf_copy).
# RUVg (04_ruv.Rmd, models with W<i> terms) and the non positional feature sets (da_nopos) are disabled (rules commented below).
# Each Rmd is rendered from a uniquely named copy (.render_XXXXXXXX.Rmd): parallel renders of the same Rmd would share <Rmd>.knit.md.
# FORCE=TRUE of the former loop: snakemake -R <rule> (e.g. -R count to recount and redo everything downstream).
# 03_features_classes.Rmd (features_classes_<prefix>.tsv, needed by 04_der_classes.Rmd) is local only (EpiMap and cCRE files):
#   run it locally and copy features_classes_<prefix>*.tsv to the cluster.
#
# snakemake -k -s 04_differential_analysis.py --cores 16 -pn
# on DRAC
# snakemake -k -s 04_differential_analysis.py --jobs 50 --cluster "sbatch --account=def-trasler --time=6:0:0 --mem-per-cpu=3G --nodes=1 --ntasks=1 --cpus-per-task={threads} " --latency-wait 60 -pn

prefixes        = ["peaks10"]
model_func_name = "deseq2"   # positional pipeline (count -> da -> combp -> der_classes -> models)
models = [
  "status",                    
  "status+LF1",                
  "status+LF1+LF2",            
  "status+LF1+LF2+LF3",        
  "status+LF1+LF2+LF3+LF4",    
  "status+LF1+LF2+LF3+LF4+LF5",
  "status+study+experimenter",                              
  "status+study+experimenter+LF1",                              
  "status+study+experimenter+LF1+LF2",                              
  "status+study+experimenter+LF1+LF2+LF3",                              
  "status+study+experimenter+LF1+LF2+LF3+LF4",                              
  "status+study+experimenter+LF1+LF2+LF3+LF4+LF5",                              
]
pval_threshs = ["0.05"]
lf_k         = 10        # latent factors written by 04_da.Rmd (lf_k, default 10): the formulas can use LF1..LF<lf_k>

ewas     = ["ewas4combp_"+gse+"_"+prefix+"_"+model_func_name+"_~"+model+".bed"                      for prefix in prefixes for model in models]
ders     = ["dmrcombp_"+prefix+"_"+model_func_name+"_~"+model+"_"+thresh+".regions-t.bed"          for prefix in prefixes for model in models for thresh in pval_threshs]
classes  = ["der_classes_"+prefix+"_"+model_func_name+"_~"+model+".tsv"                            for prefix in prefixes for model in models]
models_html = ["04_models_"+prefix+".html"                                                       for prefix in prefixes]

wildcard_constraints:
  prefix  = "[a-z]+[0-9]+(?:q[0-9]+)?",   # <features><N>[q<M>]: 99_<features>.Rmd with parameter N, counted with featureCounts -Q M (30 by default)
  # model terms: letters with optional digits and _suffix (tss_ratio, W1, Wpaper1, LF1), joined by +; the threshold contains a dot
  formula = "[A-Za-z]+[0-9]*(_[A-Za-z0-9]+)*(\\+[A-Za-z]+[0-9]*(_[A-Za-z0-9]+)*)*",
  thresh  = "0\\.[0-9]+"

# render an Rmd with R variables, from a uniquely named copy in the project dir (children are found, parallel renders do not share <Rmd>.knit.md)
def render(rmd, rvars, html):
  return """
tmprmd=$(mktemp -p . --suffix=.Rmd .render_XXXXXXXX)
trap "rm -f $tmprmd" EXIT
cp """+rmd+""" $tmprmd
Rscript -e '""" + rvars + """ rmarkdown::render("'$tmprmd'", output_file="""+'"'+html+'"'+""")'
"""

env = """
set +u
source ~/conda_config.sh
conda activate mnase_env
set -u
export OMP_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1
export MKL_NUM_THREADS=1
"""

localrules: target

rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input:
      ewas,
      ders,
      classes,
      models_html,
    shell:"""
echo workflow \"04_differential_analysis.py\" completed at `date`.
          """


# rule count:
#     # featureCounts on the features of <prefix> (COUNT = TRUE), FRiP and tss_ratio
#     input:
#       rmd = "03_count.Rmd",
#     output:
#       html       = "03_count_{prefix}.html",
#       raw_counts = "datashare/"+gse+"/raw_counts_{prefix}.rds",
#       frip       = "e_frip_{prefix}.rds",
#       tss_ratio  = "e_tss_ratio_{prefix}.rds",
#     threads: 32
#     shell: env + render("03_count.Rmd", 'COUNT = TRUE; prefix = "{wildcards.prefix}";', "{output.html}")

# disabled; to re-enable: restore ruv_sets, ruv_froms, r_ruv_froms and k_max (git history), the W inputs of da_inputs and r_ruv_froms in the shells
# rule ruv:
#     # RUVg factors 1..k_max from the ctl_frac least significant features of the first-pass model ~<formula> (estimated on its samples)
#     input:
#       rmd  = "04_ruv.Rmd",
#       ewas = "ewas4combp_"+gse+"_{prefix}_"+model_func_name+"_~{formula}.bed",
#     output:
#       html = "04_ruv_{prefix}_"+model_func_name+"_~{formula}.html",
#       w    = ["e_W"+str(i)+"_{prefix}_"+model_func_name+"_~{formula}_ctl25.rds" for i in range(1, k_max + 1)],
#     threads: 4
#     shell: env + render("04_ruv.Rmd", 'prefix = "{wildcards.prefix}"; model_func_name = "'+model_func_name+'"; ruv_formula = "~{wildcards.formula}"; k_max = '+str(k_max)+';', "{output.html}")


def da_inputs(wildcards):
  ret = {
    "rmd":        "04_da.Rmd",
    "raw_counts": "datashare/"+gse+"/raw_counts_"+wildcards.prefix+".rds",
  }
  # GC bias of the libraries (exp_grp.R reads e_gc_slope_<prefix>.rds, else the common e_gc_slope.rds), made by 03_gc_slope.Rmd (no rule)
  if re.search("(^|\\+)gc_slope($|\\+)", wildcards.formula):
    ret["gc_slope"] = "e_gc_slope.rds"
  # latent factors: a model with LF<i> terms uses the factors of the same model without them (written by its da job)
  if re.search("(^|\\+)LF[0-9]", wildcards.formula):
    src = lf_source(wildcards.formula)
    ret["lf_src"] = ["e_LF"+str(i)+"_"+wildcards.prefix+"_"+model_func_name+"_~"+src+"_lfmm.rds" for i in range(1, lf_k + 1)]
  return ret

# model without its LF<i> terms (the model the latent factors come from)
def lf_source(formula):
  return re.sub("\\+LF[0-9]+", "", formula)

# exp_grp.R reads e_LF<i>_<prefix>_<model_func_name>_~<formula>_lfmm.rds for the formula of the model itself:
# before the render, the factors of the model without LF terms are copied under this name (04_da.Rmd then overwrites them with its own factors)
lf_copy = """
src=$(echo "{wildcards.formula}" | sed -E 's/\\+LF[0-9]+//g')
if [ "$src" != "{wildcards.formula}" ]; then
  for i in $(seq 1 """+str(lf_k)+"""); do
    cp "e_LF${{i}}_{wildcards.prefix}_"""+model_func_name+"""_~${{src}}_lfmm.rds" "e_LF${{i}}_{wildcards.prefix}_"""+model_func_name+"""_~{wildcards.formula}_lfmm.rds"
  done
fi
"""

rule da:
    # DESeq2 ~<formula>, coefficient status_CP_vs_SD (or status_<subset>_CP_vs_SD), results table and ewas bed for comb-p (positional feature sets)
    input: unpack(da_inputs)
    output:
      html = "04_da_"+gse+"_{prefix}_"+model_func_name+"_~{formula}.html",
      tsv  = "da_"+gse+"_{prefix}_"+model_func_name+"_~{formula}.tsv",
      ewas = "ewas4combp_"+gse+"_{prefix}_"+model_func_name+"_~{formula}.bed",
      lf   = ["e_LF"+str(i)+"_{prefix}_"+model_func_name+"_~{formula}_lfmm.rds" for i in range(1, lf_k + 1)],   # 04_da.Rmd, section "Latent factors"
    threads: 4
    shell: env + lf_copy + render("04_da.Rmd", 'gse = "'+gse+'"; prefix = "{wildcards.prefix}"; model_func_name = "'+model_func_name+'"; model_formula = "~{wildcards.formula}";', "{output.html}")

# disabled; to re-enable: restore nopos_features, nopos_re, nopos_da and the target_rmsk rule (git history)
# rule da_nopos:
#     # DESeq2 on a non positional feature set (comb-p threshold 0): results table only, size factors on all the features (deseq2) or on the controls (deseq2ctl)
#     input: unpack(da_inputs)
#     output:
#       html = "04_da_"+gse+"_{prefix}_{mfn}_~{formula}.html",
#       tsv  = "da_"+gse+"_{prefix}_{mfn}_~{formula}.tsv",
#     wildcard_constraints:
#       prefix = nopos_re,
#       mfn    = "deseq2(?:ctl)?",
#     threads: 4
#     shell: env + render("04_da.Rmd", 'gse = "'+gse+'"; prefix = "{wildcards.prefix}"; model_func_name = "{wildcards.mfn}"; model_formula = "~{wildcards.formula}"; '+r_ruv_froms+'', "{output.html}")


rule combp:
    # comb-p DER, seed threshold <thresh>
    input:
      rmd  = "04_combp.Rmd",
      ewas = "ewas4combp_"+gse+"_{prefix}_"+model_func_name+"_~{formula}.bed",
    output:
      html    = "04_combp_"+gse+"_{prefix}_"+model_func_name+"_~{formula}_{thresh}.html",
      regions = "dmrcombp_{prefix}_"+model_func_name+"_~{formula}_{thresh}.regions-t.bed",
      slk     = "dmrcombp_{prefix}_"+model_func_name+"_~{formula}_{thresh}.slk.bed.gz",
    threads: 4
    shell: env + render("04_combp.Rmd", 'gse = "'+gse+'"; prefix = "{wildcards.prefix}"; model_func_name = "'+model_func_name+'"; model_formula = "~{wildcards.formula}"; pval_thresh = "{wildcards.thresh}";', "{output.html}")


rule der_classes:
    # feature classes of the DER (needs features_classes_<prefix>.tsv from 03_features_classes.Rmd, local)
    input:
      rmd     = "04_der_classes.Rmd",
      classes = "features_classes_{prefix}.tsv",
      genes   = "features_classes_{prefix}_genes.tsv",
      go      = "features_classes_{prefix}_go_bp.tsv",
      rmsk    = "features_classes_{prefix}_rmsk.tsv",
      regions = ["dmrcombp_{prefix}_"+model_func_name+"_~{formula}_"+thresh+".regions-t.bed" for thresh in pval_threshs],
    output:
      html = "04_der_classes_{prefix}_"+model_func_name+"_~{formula}.html",
      tsv  = "der_classes_{prefix}_"+model_func_name+"_~{formula}.tsv",
      go   = "der_go_{prefix}_"+model_func_name+"_~{formula}.tsv",
      rep  = "der_repeats_{prefix}_"+model_func_name+"_~{formula}.tsv",
    threads: 1
    shell: env + render("04_der_classes.Rmd", 'gse = "'+gse+'"; prefix = "{wildcards.prefix}"; model_func_name = "'+model_func_name+'"; model_formula = "~{wildcards.formula}"; pval_threshs = c("'+'", "'.join(pval_threshs)+'");', "{output.html}")


rule models:
    # all the models of a prefix: DER and their overlap, l2fc vs distance to TSS, l2fc correlation between models, tss_ratio vs status within strata
    input:
      rmd  = "04_models.Rmd",
      ewas = lambda wildcards: ["ewas4combp_"+gse+"_"+wildcards.prefix+"_"+model_func_name+"_~"+model+".bed" for model in models],
      ders = lambda wildcards: ["dmrcombp_"+wildcards.prefix+"_"+model_func_name+"_~"+model+"_"+thresh+".regions-t.bed" for model in models for thresh in pval_threshs],
    output:
      html = "04_models_{prefix}.html",
    threads: 1
    shell: env + render("04_models.Rmd", 'gse = "'+gse+'"; prefix = "{wildcards.prefix}"; model_func_name = "'+model_func_name+'"; pval_threshs = c("'+'", "'.join(pval_threshs)+'"); models = c("~'+'", "~'.join(models)+'");', "{output.html}")
