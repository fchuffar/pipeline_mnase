import os 
exec(open("config").read())

localrules: target







foo=version # patch for bug in target shell
rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input:
      "/home/fchuffar/projects/datashare/mmspz/S_pp2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_mmq30.bam",

      "/home/fchuffar/projects/datashare/mmspz/S_pp2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_mmq30.bam",

      "/home/fchuffar/projects/datashare/mmspz/S_pp2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq30.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq30.bam",

      "/home/fchuffar/projects/datashare/mmspz/S_pp2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq0.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq0.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq0.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq0.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq0.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq0.bam",

      "/home/fchuffar/projects/datashare/mmspz/S_pp2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq1.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq1.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_pp6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq1.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq1.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq1.bam",
      "/home/fchuffar/projects/datashare/mmspz/S_nn6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_srt_mmq1.bam",


      "/home/fchuffar/projects/datashare/mmspz/S_pp2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_pp4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_pp6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_nn2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_nn4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_nn6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin025_fsmax075_srt_PE_30_4_RPKM.bw",

      "/home/fchuffar/projects/datashare/mmspz/S_pp2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_pp4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_pp6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_nn2_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_nn4_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/mmspz/S_nn6_end-to-end_trim30_bowtie2_"+species+"_"+foo+"_fsmin125_fsmax175_srt_PE_30_4_RPKM.bw",
    shell:"""
echo done.
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
multiqc --force -o . -n multiqc_notrim_fsmin125_fsmax175 \
  ~/projects/datashare/"""+gse+"""/*_end-to-end_trim30_bowtie2_"""+species+"""_"""+foo+"""_fsmin125_fsmax175_srt.bam


echo workflow \"pipeline_mnase\" completed at `date`
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

rule bigwig_coverage_advanced_SR:
    input: "{prefix}_srt.bam", 
    output: "{prefix}_srt_SR_{mmq}_{binsize}_{norm}.bw"
    threads: 32
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
export TMPDIR=/dev/shm
bamCoverage \
  -b {input} \
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

