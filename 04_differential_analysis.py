import os
import re
exec(open("config").read())

# Differential analysis CP vs SD (replaces the R loops of 00_custom_preprocessing.sh):
#   03_count.Rmd (featureCounts, FRiP, tss_ratio)
#   03_gc_slope.Rmd (GC bias of the libraries on control tiles of gc_prefix, e_gc_slope.rds)
#   -> 04_ruv.Rmd (RUVg factors from the first-pass model, for the models with W_ terms)
#   -> 04_da.Rmd (DESeq2, ewas4combp bed) -> 04_combp.Rmd (comb-p DER, per seed threshold)
#   -> 04_der_classes.Rmd (feature classes of the DER)
#   -> 04_models.Rmd (all the models of a prefix: DER and their overlap, l2fc vs distance to TSS, l2fc correlation, tss_ratio vs status within strata)
# Each Rmd is rendered from a uniquely named copy (.render_XXXXXXXX.Rmd): parallel renders of the same Rmd would share <Rmd>.knit.md.
# FORCE=TRUE of the former loop: snakemake -R <rule> (e.g. -R count to recount and redo everything downstream).
# 03_features_classes.Rmd (features_classes_<prefix>.tsv, needed by 04_der_classes.Rmd) is local only (EpiMap and cCRE files):
#   run it locally and copy features_classes_<prefix>*.tsv to the cluster.
#
# snakemake -k -s 04_differential_analysis.py --cores 16 -pn
# on DRAC
# snakemake -k -s 04_differential_analysis.py --jobs 50 --cluster "sbatch --account=def-trasler --time=6:0:0 --mem-per-cpu=3G --nodes=1 --ntasks=1 --cpus-per-task={threads} " --latency-wait 60 -pn

prefixes        = ["peaks10"]
model_func_name = "deseq2"   # positional pipeline (da -> ruv -> combp -> der_classes -> models)
# non positional feature sets (meta-features, e.g. 99_rmsk.Rmd): comb-p threshold 0 = no comb-p, per feature results only (da_*.tsv)
#   model_func_names: deseq2 (size factors on all the features) and deseq2ctl (size factors on the control features, feat_type == "control")
nopos_features  = ["rmsk"]
nopos_prefixes  = ["rmsk50q0", "rmsk50q30"]
nopos_mfns      = ["deseq2ctl", "deseq2"]
nopos_models    = ["status+study+experimenter", "status_TER+study+experimenter", "status_nohi22+study+experimenter",
                   "status+study+experimenter+gc_slope", "status_TER+study+experimenter+gc_slope", "status_nohi22+study+experimenter+gc_slope"]
nopos_re        = "(?:"+"|".join(nopos_features)+")[0-9]+(?:q[0-9]+)?"
models = [
  "status",
  "status+tss_ratio",
  "status+study+experimenter",
  "status+study+experimenter+tss_ratio",
  "status+study+experimenter+W_1+W_2+W_3+W_4+W_5",
  "status+study+experimenter+W_1+W_2+W_3+W_4+W_5+tss_ratio",
  "status+study+experimenter+frip",          
  "status+study+experimenter+frip+tss_ratio",
  "status+study+experimenter+W_1+W_2+W_3+W_4+W_5+frip",            
  "status+study+experimenter+W_1+W_2+W_3+W_4+W_5+frip+tss_ratio",
  # status restricted to a subset (exp_grp.R, NA elsewhere: 04_da.Rmd drops these samples);
  # lot and experimenter adjusted for only where they vary
  "status_hi22",
  "status_hi23+experimenter",
  "status_hs24+experimenter",
  "status_hw24+experimenter",
  "status_nohi22+study+experimenter",
  "status_FCLI+study+experimenter",
  "status_AST+study+experimenter",
  "status_TER+study+experimenter",
  "status_IDI+study+experimenter",
  "status_AST_nohi22+study+experimenter",
  # samples of the paper (exp_grp.R status_paper: CP vs SD == 1, FCLI excluded), RUVg factors estimated on these samples (Wpaper_)
  "status_paper+study+experimenter",
  "status_paper+study+experimenter+Wpaper_1+Wpaper_2+Wpaper_3+Wpaper_4+Wpaper_5",
  # main sample set since 2026-11-23 (FCLI excluded, as suggested by Dalwinder and Sarah): gc_slope, tss_ratio, RUV
  "status_paper",
  "status_paper+study+experimenter+tss_ratio",
  "status_paper+study+experimenter+gc_slope",
  "status_paper+study+experimenter+tss_ratio+gc_slope",
  "status_paper+study+experimenter+Wpaper_1+Wpaper_2+Wpaper_3+Wpaper_4+Wpaper_5+tss_ratio",
  "status_paper+study+experimenter+Wpaper_1+Wpaper_2+Wpaper_3+Wpaper_4+Wpaper_5+gc_slope",
  "status_paper+study+experimenter+Wpaper_1+Wpaper_2+Wpaper_3+Wpaper_4+Wpaper_5+tss_ratio+gc_slope",
  # GC bias of the library as a covariate (gc_slope, 03_gc_slope.Rmd, e_gc_slope.rds)
  "status+study+experimenter+gc_slope",
  "status+study+experimenter+tss_ratio+gc_slope",
  "status_TER+study+experimenter+gc_slope",
  "status_nohi22+study+experimenter+gc_slope",
  # per CP diagnosis (status_AST/TER/IDI: SD + one diagnosis, no FCLI), with gc_slope
  "status_AST+study+experimenter+gc_slope",
  "status_IDI+study+experimenter+gc_slope",
]
pval_threshs = ["0.05", "0.01", "0.001"]
# gc_slope (03_gc_slope.Rmd): control tiles of gc_prefix with coverage <= gc_cov_mult x background mode, without CGI if gc_excl_cgi,
#   all of them (gc_n_tiles = "Inf") or a seeded random draw
gc_prefix   = "tiles5000"
gc_cov_mult = 1
gc_excl_cgi = "TRUE"
gc_n_tiles  = "Inf"
gc_seed     = 1
# RUVg: controls = ctl_frac least significant features of a first-pass formula, factors 1..k_max (04_ruv.Rmd defaults)
# one set of factors per first-pass formula, named by the column prefix used in the models (W_1.., Wpaper_1..)
ruv_sets = {
  "W":      "status+study+experimenter",
  "Wpaper": "status_paper+study+experimenter",
}
ruv_froms = {tag: model_func_name+"_~"+f+"_ctl25" for tag, f in ruv_sets.items()}
r_ruv_froms = 'ruv_froms = c('+', '.join(tag+' = "'+rf+'"' for tag, rf in ruv_froms.items())+');'
k_max       = 10

ewas     = ["ewas4combp_"+gse+"_"+prefix+"_"+model_func_name+"_~"+model+".bed"                      for prefix in prefixes for model in models]
ders     = ["dmrcombp_"+prefix+"_"+model_func_name+"_~"+model+"_"+thresh+".regions-t.bed"          for prefix in prefixes for model in models for thresh in pval_threshs]
classes  = ["der_classes_"+prefix+"_"+model_func_name+"_~"+model+".tsv"                            for prefix in prefixes for model in models]
models_html = ["04_models_"+prefix+".html"                                                       for prefix in prefixes]
nopos_da    = ["da_"+gse+"_"+prefix+"_"+mfn+"_~"+model+".tsv"                                      for prefix in nopos_prefixes for mfn in nopos_mfns for model in nopos_models]

wildcard_constraints:
  prefix  = "[a-z]+[0-9]+(?:q[0-9]+)?",   # <features><N>[q<M>]: 99_<features>.Rmd with parameter N, counted with featureCounts -Q M (30 by default)
  # model terms: letters with optional _suffix (tss_ratio, W_1), joined by +; the threshold contains a dot
  formula = "[A-Za-z]+(_[A-Za-z0-9]+)*(\\+[A-Za-z]+(_[A-Za-z0-9]+)*)*",
  thresh  = "0\\.[0-9]+"

# render an Rmd with R variables, from a uniquely named copy in the project dir (children are found, parallel renders do not share <Rmd>.knit.md)
def render(rmd, rvars, html):
  return """
tmprmd=$(mktemp -p . --suffix=.Rmd .render_XXXXXXXX)
trap "rm -f $tmprmd" EXIT
cp """+rmd+""" $tmprmd
Rscript -e '""" + rvars + """ rmarkdown::render("'$tmprmd'", output_file="""+'"'+html+'"'+""")'
rm -f $tmprmd
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

localrules: target, target_rmsk

rule target_rmsk:
    # non positional feature sets only: snakemake -s 04_differential_analysis.py target_rmsk --allowed-rules da_nopos target_rmsk
    # (--allowed-rules: the counts are not redone even when 03_count.Rmd is newer than them)
    threads: 1
    input: nopos_da
    shell: "echo target_rmsk completed at `date`."

rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input:
      ewas,
      ders,
      classes,
      models_html,
      nopos_da,
    shell:"""
echo workflow \"04_differential_analysis.py\" completed at `date`.
          """



rule count:
    # featureCounts on the features of <prefix> (COUNT = TRUE), FRiP and tss_ratio
    input:
      rmd = "03_count.Rmd",
    output:
      html       = "03_count_{prefix}.html",
      raw_counts = "datashare/"+gse+"/raw_counts_{prefix}.rds",
      frip       = "e_frip_{prefix}.rds",
      tss_ratio  = "e_tss_ratio_{prefix}.rds",
    threads: 32
    shell: env + render("03_count.Rmd", 'COUNT = TRUE; prefix = "{wildcards.prefix}";', "{output.html}")

rule gc_slope:
    # GC bias of the libraries: slope of log2 normalized count vs GC on the control tiles of gc_prefix (03_gc_slope.Rmd)
    input:
      rmd        = "03_gc_slope.Rmd",
      raw_counts = "datashare/"+gse+"/raw_counts_"+gc_prefix+".rds",
    output:
      html     = "03_gc_slope.html",
      gc_slope = "e_gc_slope.rds",
    threads: 4
    shell: env + render("03_gc_slope.Rmd", 'gc_prefix = "'+gc_prefix+'"; cov_mult = '+str(gc_cov_mult)+'; excl_cgi = '+gc_excl_cgi+'; n_tiles = '+gc_n_tiles+'; seed = '+str(gc_seed)+';', "{output.html}")


rule ruv:
    # RUVg factors 1..k_max from the ctl_frac least significant features of the first-pass model ~<formula> (estimated on its samples)
    input:
      rmd  = "04_ruv.Rmd",
      ewas = "ewas4combp_"+gse+"_{prefix}_"+model_func_name+"_~{formula}.bed",
    output:
      html = "04_ruv_{prefix}_"+model_func_name+"_~{formula}.html",
      w    = ["e_W_"+str(i)+"_{prefix}_"+model_func_name+"_~{formula}_ctl25.rds" for i in range(1, k_max + 1)],
    threads: 4
    shell: env + render("04_ruv.Rmd", 'prefix = "{wildcards.prefix}"; model_func_name = "'+model_func_name+'"; ruv_formula = "~{wildcards.formula}"; k_max = '+str(k_max)+';', "{output.html}")



def da_inputs(wildcards):
  ret = {
    "rmd":        "04_da.Rmd",
    "raw_counts": "datashare/"+gse+"/raw_counts_"+wildcards.prefix+".rds",
    "frip":       "e_frip_"+wildcards.prefix+".rds",
    "tss_ratio":  "e_tss_ratio_"+wildcards.prefix+".rds",
  }
  # GC bias of the library (exp_grp.R reads e_gc_slope_<prefix>.rds, else the common e_gc_slope.rds)
  if re.search("(^|\\+)gc_slope($|\\+)", wildcards.formula):
    ret["gc_slope"] = "e_gc_slope.rds"   # rule gc_slope
  # RUVg factors of each set used by the formula (W_.., Wpaper_..)
  for tag, rf in ruv_froms.items():
    if re.search("(^|\\+)"+tag+"_[0-9]", wildcards.formula):
      ret["w_"+tag] = "e_W_1_"+wildcards.prefix+"_"+rf+".rds"
  return ret

rule da:
    # DESeq2 ~<formula>, coefficient status_CP_vs_SD (or status_<subset>_CP_vs_SD), results table and ewas bed for comb-p (positional feature sets)
    input: unpack(da_inputs)
    output:
      html = "04_da_"+gse+"_{prefix}_"+model_func_name+"_~{formula}.html",
      tsv  = "da_"+gse+"_{prefix}_"+model_func_name+"_~{formula}.tsv",
      ewas = "ewas4combp_"+gse+"_{prefix}_"+model_func_name+"_~{formula}.bed",
    wildcard_constraints:
      prefix = "(?!(?:"+"|".join(nopos_features)+")[0-9])[a-z]+[0-9]+(?:q[0-9]+)?",   # positional feature sets only
    threads: 4
    shell: env + render("04_da.Rmd", 'gse = "'+gse+'"; prefix = "{wildcards.prefix}"; model_func_name = "'+model_func_name+'"; model_formula = "~{wildcards.formula}"; '+r_ruv_froms+'', "{output.html}")

rule da_nopos:
    # DESeq2 on a non positional feature set (comb-p threshold 0): results table only, size factors on all the features (deseq2) or on the controls (deseq2ctl)
    input: unpack(da_inputs)
    output:
      html = "04_da_"+gse+"_{prefix}_{mfn}_~{formula}.html",
      tsv  = "da_"+gse+"_{prefix}_{mfn}_~{formula}.tsv",
    wildcard_constraints:
      prefix = nopos_re,
      mfn    = "deseq2(?:ctl)?",
    threads: 4
    shell: env + render("04_da.Rmd", 'gse = "'+gse+'"; prefix = "{wildcards.prefix}"; model_func_name = "{wildcards.mfn}"; model_formula = "~{wildcards.formula}"; '+r_ruv_froms+'', "{output.html}")



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
    shell: env + render("04_combp.Rmd", 'gse = "'+gse+'"; prefix = "{wildcards.prefix}"; model_func_name = "'+model_func_name+'"; model_formula = "~{wildcards.formula}"; '+r_ruv_froms+' pval_thresh = "{wildcards.thresh}";', "{output.html}")



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
    shell: env + render("04_der_classes.Rmd", 'gse = "'+gse+'"; prefix = "{wildcards.prefix}"; model_func_name = "'+model_func_name+'"; model_formula = "~{wildcards.formula}"; '+r_ruv_froms+' pval_threshs = c("'+'", "'.join(pval_threshs)+'");', "{output.html}")



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
