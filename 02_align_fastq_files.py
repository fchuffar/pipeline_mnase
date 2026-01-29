import os 
exec(open("config").read())

# trick to load samples from config.R
def c(*args): return list(args)

exec(open("config.R").read())

foo=version 
bam_srt = [f"/home/chuffarf/projects/datashare/{gse}/{sample}_end-to-end_trim{trim}_bowtie2_{species}_{annotation}_{foo}_srt.bam"             for sample in samples for trim in ["30"]]#, "60"]]
bam_mmq = [f"/home/chuffarf/projects/datashare/{gse}/{sample}_end-to-end_trim{trim}_bowtie2_{species}_{annotation}_{foo}_srt_mmq{mmq}.bam"    for sample in samples for trim in ["30"] for mmq in ["0", "30"]]
bw =      [f"/home/chuffarf/projects/datashare/{gse}/{sample}_end-to-end_trim30_bowtie2_{species}_{annotation}_{foo}_srt_{sr_or_pe}_30_4_RPKM.bw"     for sample in samples]

localrules: target

# print(bam_srt)

rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input:
      # bam_srt,
      # bam_mmq,
      # bw,
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_ATHOOK_FLAG_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_ATHOOK_FLAG_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_BAH_FLAG_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_BAH_FLAG_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_BD2_FLAG_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_BD2_FLAG_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_WT_FLAG_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_WT_FLAG_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/UNTAG_WT_FLAG_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/UNTAG_WT_FLAG_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin200_fsmax250_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_ATHOOK_H3K4me3_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_ATHOOK_H3K4me3_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_BAH_H3K4me3_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_BAH_H3K4me3_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_BD2_H3K4me3_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_BD2_H3K4me3_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_WT_H3K4me3_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/RSC1-FLAG_WT_H3K4me3_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/UNTAG_WT_H3K4me3_Rep1_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 
      "/home/chuffarf/projects/datashare/cutntag_sayou_curie/UNTAG_WT_H3K4me3_Rep2_end-to-end_trim30_bowtie2_Candida_albicans_IAB_SC5314.A22.haplo_fsmin150_fsmax180_srt.bam", 


    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
multiqc --force -o . -n multiqc_notrim \
  ~/projects/datashare/"""+gse+"""/*_end-to-end_trim30_bowtie2_"""+species+"""_"""+annotation+"""_"""+foo+""".log \
  ~/projects/datashare/"""+gse+"""/*_end-to-end_trim30_bowtie2_"""+species+"""_"""+annotation+"""_"""+foo+""".bam \
  ~/projects/datashare/"""+gse+"""/raw/*_*_fastqc.zip

echo workflow \"02_align_fastq_files.py\" completed at `date`.
          """







          
          
          
# rule align_bowtie:
#     input:
#       fastq_info="{prefix}/{sample}_trim{trim}.info",
#       bowtie2idx = "/home/chuffarf/projects/datashare/genomes/{species}/{annotation}/{version}/Sequence/Bowtie2Index/genome.1.bt2"
#     output:
#       log =    "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{annotation}_{version}.log",
#       bam =    "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{annotation}_{version}.bam",
#       srtbam = "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{annotation}_{version}_srt.bam",
#       bai =    "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{annotation}_{version}_srt.bam.bai"
#     threads: 32
#     message:  "--- mapping with bowtie2 ---"
#     shell:    """
# PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
# bowtie2 \
#   -t \
#   -p {threads} \
#   --{wildcards.localendtoend} \
#   --no-mixed \
#   --no-discordant \
#   --dovetail \
#   --very-sensitive \
#   -X 1000 \
#   -x  /home/chuffarf/projects/datashare/genomes/{wildcards.species}/{wildcards.annotation}/{wildcards.version}/Sequence/Bowtie2Index/genome \
#   `cat {input.fastq_info}` \
#   2> {output.log} \
#   | samtools view -bS - > {output.bam}
  
# samtools sort -@ {threads} -T /dev/shm/{wildcards.sample}_{wildcards.localendtoend}_trim{wildcards.trim} -o {output.srtbam} {output.bam}
# samtools index {output.srtbam}
# cat {output.log}
# """



rule index_bowtie:
    input:
      genome = "/home/chuffarf/projects/datashare/genomes/{species}/{annotation}/{version}/Sequence/WholeGenomeFasta/genome.fa"
    output:
      bowtie2idx = "/home/chuffarf/projects/datashare/genomes/{species}/{annotation}/{version}/Sequence/Bowtie2Index/genome.1.bt2"
    threads: 32
    message:  "--- mapping with bowtie2 ---"
    shell:    """
mkdir -p /home/chuffarf/projects/datashare/genomes/{wildcards.species}/{wildcards.annotation}/{wildcards.version}/Sequence/Bowtie2Index/
cd /home/chuffarf/projects/datashare/genomes/{wildcards.species}/{wildcards.annotation}/{wildcards.version}/Sequence/Bowtie2Index/
ln -s ../WholeGenomeFasta/genome.fa 
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
bowtie2-build -f genome.fa genome

"""




rule mmq_filter_for_danpos:
    input:
      bam = "{prefix}_srt.bam",
    output: 
      bam = "{prefix}_srt_mmq{mmq}.bam",
      bai = "{prefix}_srt_mmq{mmq}.bam.bai",
    threads: 1
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
samtools view -bq {wildcards.mmq} {input.bam} > {output.bam}
samtools index {output.bam}
    """


rule awk_filter_fragment_length:
    input:
      bam = "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{version}_srt.bam",
    output: 
      bam = "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{version}_fsmin{fsmin}_fsmax{fsmax}_srt.bam",
      bai = "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{version}_fsmin{fsmin}_fsmax{fsmax}_srt.bam.bai",
    threads: 1
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
# https://www.biostars.org/p/65262/
BAM={input.bam}
fsmin={wildcards.fsmin}
fsmax={wildcards.fsmax}
BAM_OUT={output.bam}
samtools view -h $BAM | awk '$9 < -'$fsmin' && $9 > -'$fsmax' || $9 > '$fsmin' && $9 < '$fsmax' || $1 ~ /^@/' | samtools view -bS - > $BAM_OUT
ls -lha $BAM_OUT
samtools index {output.bam}
    """


# ruleorder: mmq_filter_for_danpos > align_bowtie


          



















rule bigwig_coverage_advanced_SR:
    input: "{prefix}_srt.bam", 
    output: "{prefix}_srt_SR_{mmq}_{binsize}_{norm}.bw"
    threads: 32
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
export TMPDIR=/dev/shm
bamCoverage \
  -b {input} \
  --extendReads 146\
  --numberOfProcessors {threads} \
  --binSize {wildcards.binsize} \
  --minMappingQuality {wildcards.mmq} \
  --normalizeUsing {wildcards.norm} \
  -o {output}

    """

rule bigwig_coverage_advanced_PE:
    input: "{prefix}_srt.bam", 
    output: "{prefix}_srt_PE_{mmq}_{binsize}_{norm}.bw"
    threads: 32
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
export TMPDIR=/dev/shm
bamCoverage \
  -b {input} \
  --extendReads \
  --numberOfProcessors {threads} \
  --binSize {wildcards.binsize} \
  --minMappingQuality {wildcards.mmq} \
  --normalizeUsing {wildcards.norm} \
  -o {output}

    """






