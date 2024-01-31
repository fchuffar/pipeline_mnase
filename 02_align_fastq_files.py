import os 
exec(open("config").read())

# trick to load samples from config.R
def c(*args): return list(args)

exec(open("config.R").read())

foo=version 
bam_srt = [f"/home/fchuffar/projects/datashare/{gse}/{sample}_end-to-end_trim{trim}_bowtie2_{species}_{annotation}_{foo}_srt.bam"             for sample in samples for trim in ["30"]]#, "60"]]
bam_mmq = [f"/home/fchuffar/projects/datashare/{gse}/{sample}_end-to-end_trim{trim}_bowtie2_{species}_{annotation}_{foo}_srt_mmq{mmq}.bam"    for sample in samples for trim in ["30"] for mmq in ["0", "30"]]
bw =      [f"/home/fchuffar/projects/datashare/{gse}/{sample}_end-to-end_trim30_bowtie2_{species}_{annotation}_{foo}_srt_{sr_or_pe}_30_4_RPKM.bw"     for sample in samples]

localrules: target

print(bam_srt)

rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input:
      bam_srt,
      bam_mmq,
      bw,
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
multiqc --force -o . -n multiqc_notrim \
  ~/projects/datashare/"""+gse+"""/*_end-to-end_trim30_bowtie2_"""+species+"""_"""+annotation+"""_"""+foo+""".log \
  ~/projects/datashare/"""+gse+"""/*_end-to-end_trim30_bowtie2_"""+species+"""_"""+annotation+"""_"""+foo+""".bam \
  ~/projects/datashare/"""+gse+"""/raw/*_*_fastqc.zip

echo workflow \"02_align_fastq_files.py\" completed at `date`.
          """







          
          
          
rule align_bowtie:
    input:
      fastq_info="{prefix}/{sample}_trim{trim}.info",
      bowtie2idx = "/home/fchuffar/projects/datashare/genomes/{species}/{annotation}/{version}/Sequence/Bowtie2Index/genome.1.bt2"
    output:
      log =    "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{annotation}_{version}.log",
      bam =    "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{annotation}_{version}.bam",
      srtbam = "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{annotation}_{version}_srt.bam",
      bai =    "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{annotation}_{version}_srt.bam.bai"
    threads: 32
    message:  "--- mapping with bowtie2 ---"
    shell:    """
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
bowtie2 \
  -t \
  -p {threads} \
  --{wildcards.localendtoend} \
  --no-mixed \
  --no-discordant \
  -x  /home/fchuffar/projects/datashare/genomes/{wildcards.species}/{wildcards.annotation}/{wildcards.version}/Sequence/Bowtie2Index/genome \
  `cat {input.fastq_info}` \
  2> {output.log} \
  | samtools view -bS - > {output.bam}
  
samtools sort -@ {threads} -T /dev/shm/{wildcards.sample}_{wildcards.localendtoend}_trim{wildcards.trim} -o {output.srtbam} {output.bam}
samtools index {output.srtbam}
cat {output.log}
"""



rule index_bowtie:
    input:
      genome = "/home/fchuffar/projects/datashare/genomes/{species}/{annotation}/{version}/Sequence/WholeGenomeFasta/genome.fa"
    output:
      bowtie2idx = "/home/fchuffar/projects/datashare/genomes/{species}/{annotation}/{version}/Sequence/Bowtie2Index/genome1.bt2"
    threads: 32
    message:  "--- mapping with bowtie2 ---"
    shell:    """
mkdir -p /home/fchuffar/projects/datashare/genomes/{wildcards.species}/{wildcards.annotation}/{wildcards.version}/Sequence/Bowtie2Index/
cd /home/fchuffar/projects/datashare/genomes/{wildcards.species}/{wildcards.annotation}/{wildcards.version}/Sequence/Bowtie2Index/
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

ruleorder: mmq_filter_for_danpos > align_bowtie


          



















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






