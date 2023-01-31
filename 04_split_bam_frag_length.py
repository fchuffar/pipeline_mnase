import os 
exec(open("config").read())

# trick to load samples from config.R
def c(*args): return list(args)

exec(open("config.R").read())

foo=version 
# bam_awk_0 = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin025_fsmax075_srt_mmq30_srt_mmq{mmq}.bam" for sample in samples for mmq in ["1", "30"]]
# bam_awk_1 = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin075_fsmax100_srt_mmq30_srt_mmq{mmq}.bam" for sample in samples for mmq in ["1", "30"]]
# bam_awk_2 = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin100_fsmax125_srt_mmq30_srt_mmq{mmq}.bam" for sample in samples for mmq in ["1", "30"]]

# bam_awk_0 = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin200_fsmax500_srt.bam"           for sample in samples]
bw_awk_0  = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin200_fsmax500_srt_PE_0_4_RPKM.bw"        for sample in samples]

# bam_awk_1 = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin050_fsmax200_srt.bam"           for sample in samples for mmq in ["30"]]
# bam_awk_2 = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin050_fsmax125_srt.bam"           for sample in samples for mmq in ["30"]]
# bam_awk_3 = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin125_fsmax200_srt.bam"           for sample in samples for mmq in ["30"]]
bw_awk_1  = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin050_fsmax200_srt_PE_30_4_RPKM.bw"        for sample in samples]
bw_awk_2  = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin050_fsmax125_srt_PE_30_4_RPKM.bw"        for sample in samples]
bw_awk_3  = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin125_fsmax200_srt_PE_30_4_RPKM.bw"        for sample in samples]

bw_awk_4  = [f"/home/fchuffar/projects/datashare/mmspz/{sample}_end-to-end_trim30_bowtie2_{species}_{foo}_fsmin100_fsmax125_srt_PE_30_4_RPKM.bw"        for sample in samples]





foo=version # patch for bug in target shell
rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input:
      # bam_awk_0,
      # bam_awk_1,
      # bam_awk_2,
      # bam_awk_3,
      bw_awk_0 ,
      bw_awk_1 ,
      bw_awk_2 ,
      bw_awk_3 ,
      bw_awk_4
    shell:"""
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
