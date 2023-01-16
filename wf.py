import os 
exec(open("config").read())

localrules: target


bws_vplot = [f"/home/fchuffar/projects/datashare/hsspz/{sample}_end-to-end_trim30_bowtie2_{species}_{version}_fsmin{lb:03d}_fsmax{lb+10:03d}_srt_PE_30_4_RPKM.bw" for sample in ["input_rep10","cth2b_rep11","cth2b_rep12","input_rep20","cth2b_rep21","cth2b_rep22"] for lb in [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]]






foo=version # patch for bug in target shell
rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input:
      "/home/fchuffar/projects/datashare/hsspz/raw/input_rep10_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/input_rep10_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep11_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep11_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep12_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep12_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/input_rep20_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/input_rep20_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep21_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep21_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep22_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep22_R2_fastxtrimf30.fastq.gz",


      "/home/fchuffar/projects/datashare/hsspz/input_rep10_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep11_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep12_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/input_rep20_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep21_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep22_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_30_4_RPKM.bw",

      "/home/fchuffar/projects/datashare/hsspz/input_rep10_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep11_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep12_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/input_rep20_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep21_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep22_end-to-end_trim30_bowtie2_"+species+"_"+version+"_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/input_rep10_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin025_fsmax075_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep11_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin025_fsmax075_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep12_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin025_fsmax075_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/input_rep20_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin025_fsmax075_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep21_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin025_fsmax075_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep22_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin025_fsmax075_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/input_rep10_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin125_fsmax175_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep11_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin125_fsmax175_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep12_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin125_fsmax175_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/input_rep20_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin125_fsmax175_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep21_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin125_fsmax175_srt_PE_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/hsspz/cth2b_rep22_end-to-end_trim30_bowtie2_"+species+"_"+version+"_fsmin125_fsmax175_srt_PE_0_4_RPKM.bw",

      bws_vplot,

    shell:"""
echo done.
multiqc --force -o ~/projects/"""+datashare+"""/"""+gse+"""/raw/ -n multiqc_notrim \
  ~/projects/"""+datashare+"""/"""+gse+"""/*_end-to-end_trim30_bowtie2_"""+species+"""_"""+foo+""".log \
  ~/projects/"""+datashare+"""/"""+gse+"""/*_end-to-end_trim30_bowtie2_"""+species+"""_"""+foo+""".bam \
  ~/projects/"""+datashare+"""/"""+gse+"""/raw/*_*_fastqc.zip

echo workflow \"pipeline_mnase\" completed at `date`
          """










rule mmq_filter_for_danpos:
    input:
      bam = "{prefix}/{sample}_{localendtoend}_trim{trim}_srt.bam",
    output: 
      bam = "{prefix}/{sample}_{localendtoend}_trim{trim}_srt_mmq30.bam",
      bai = "{prefix}/{sample}_{localendtoend}_trim{trim}_srt_mmq30.bam.bai",
    threads: 1
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
samtools view -bq 30 {input.bam} > {output.bam}
samtools index {output.bam}
    """

          
          
          
          
rule align_bowtie:
    input:
      # fwd="{prefix}/{sample}_R1_{trim}.fastq.gz",
      # rev="{prefix}/{sample}_R2_{trim}.fastq.gz",
      fastq_info="{prefix}/{sample}_trim{trim}.info",
      # star_index="/home/fchuffar/projects/datashare/genomes/Mus_musculus/UCSC/mm10/Sequence/Bowtie2Index/genome",
      # gtf="/scratch_r730/datashare/genomes/{species}/UCSC/{index}/Annotation/Genes/genes.gtf",
    output:
      log =    "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{version}.log",
      bam =    "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{version}.bam",
      srtbam = "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{version}_srt.bam",
      bai =    "{prefix}/{sample}_{localendtoend}_trim{trim}_bowtie2_{species}_{version}_srt.bam.bai"
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
  -x  /home/fchuffar/projects/datashare/genomes/{wildcards.species}/UCSC/{wildcards.version}/Sequence/Bowtie2Index/genome \
  `cat {input.fastq_info}` \
  2> {output.log} \
  | samtools view -bS - > {output.bam}
  
samtools sort -@ {threads} -T /dev/shm/{wildcards.sample}_{wildcards.localendtoend}_trim{wildcards.trim} -o {output.srtbam} {output.bam}
samtools index {output.srtbam}
cat {output.log}
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

ruleorder: awk_filter_fragment_length > align_bowtie


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


























rule align_solid:
    input:
      fastq_info="{prefix}/{sample}_solid.info",
    output:
      log    = "{prefix}/{sample}_solid.log",
      bam    = "{prefix}/{sample}_solid.bam",
      srtbam = "{prefix}/{sample}_solid_srt.bam",
      bai    = "{prefix}/{sample}_solid_srt.bam.bai",
      # bw     = "{prefix}/{sample}_solid_maqerr{maqerr}_srt_0_0_4_RPKM.bw",
    threads: 32
    message:  "--- mapping with bowtie2 ---"
    shell:    """
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
bowtie --chunkmbs 1024 -t -p {threads} -C --sam \
  --trim3 20 \
  --fr \
  /home/fchuffar/projects/datashare/genomes/Mus_musculus/UCSC/mm10/Sequence/BowtieIndexSolid/genome -f \
  `cat {input.fastq_info}` \
  2> {output.log}   | samtools view -bS - > {output.bam}
samtools sort -@ 32 -T /dev/shm/{wildcards.sample}_solid -o {output.srtbam} {output.bam}
samtools index {output.srtbam}
    """

rule saf_featurecounts:
    input: 
      saf_file="tss.saf",
    output: "{prefix}_fastxtrimf{trim}.count.txt"
    threads: 32
    shell:"""
/summer/epistorage/miniconda3/envs/subread_env/bin/featureCounts \
  -a {input.saf} \
  -F SAF \
  --largestOverlap \
  -p -d 30 -D 200  \
  -O \
  -Q {mmq} \
  -T {threads} \
  -o {output} \
  /home/fchuffar/projects/datashare/dapseq/hghfat_chip_nme2ko_m273_end-to-end_trim30_srt.bam \
  /home/fchuffar/projects/datashare/dapseq/hghfat_chip_nme2ko_m292_end-to-end_trim30_srt.bam \
  /home/fchuffar/projects/datashare/dapseq/hghfat_chip_nme2wt_m300_end-to-end_trim30_srt.bam \
  /home/fchuffar/projects/datashare/dapseq/hghfat_chip_nme2wt_m303_end-to-end_trim30_srt.bam \
  /home/fchuffar/projects/datashare/dapseq/hghfat_inpt_nme2ko_m273_end-to-end_trim30_srt.bam \
  /home/fchuffar/projects/datashare/dapseq/hghfat_inpt_nme2ko_m292_end-to-end_trim30_srt.bam \
  /home/fchuffar/projects/datashare/dapseq/hghfat_inpt_nme2wt_m300_end-to-end_trim30_srt.bam \
  /home/fchuffar/projects/datashare/dapseq/hghfat_inpt_nme2wt_m303_end-to-end_trim30_srt.bam \
  /home/fchuffar/projects/datashare/dapseq/normal_chip_nme2ko_m291_end-to-end_trim30_srt.bam \
  /home/fchuffar/projects/datashare/dapseq/normal_chip_nme2ko_m293_end-to-end_trim30_srt.bam \

"""

rule bed_to_fasta:
    input: os.path.expanduser("{prefix}.bed")
    output: os.path.expanduser("~/projects/heatshock/data/{subject}.blast.db")
    threads: 1
    shell:"""
bedtools  getfasta -fi /home/fchuffar/projects/datashare/genomes/Mus_musculus/UCSC/mm10/Sequence/WholeGenomeFasta/genome.fa \
  -bed ~/projects/small_structs/results/for_blastn.bed > \
  ~/projects/small_structs/results/for_blastn.fasta

/summer/epistorage/miniconda3/envs/mnase_env/bin/makeblastdb -in ~/projects/small_structs/results/for_blastn.fasta \
  -dbtype nucl -parse_seqids -out  ~/projects/small_structs/results/for_blastn.blast.db

/summer/epistorage/miniconda3/envs/mnase_env/bin/blastn -db ~/projects/small_structs/results/for_blastn.blast.db \
  -num_threads=1 \
  -query ~/projects/small_structs/results/for_blastn.fasta \
  -outfmt "10 std sstrand" \
  -evalue 10 -task blastn-short -word_size 8 -perc_identity 100 -qcov_hsp_perc 1  2>/dev/null | gzip  > ~/projects/small_structs/results/for_blastn.blasted.txt.gz





  
if (!exists("mgzread.table")) {
gzread.table = function(fn, ...) read.table(gzfile(fn), ...)
mgzread.table = memoise::memoise(gzread.table)
}


fn = "~/projects/small_structs/results/for_blastn.blasted.txt.gz"
print(fn)
foo = mgzread.table(fn, sep=",", stringsAsFactors=FALSE)
colnames(foo) = c("qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore", "sstrand")
# foo$sseqid_strand =   factor(foo$sseqid_strand, levels=paste(rep(sseqids, each=2), unique(foo$sstrand), sep="_"))
# foo$sseqid = factor(foo$sseqid, levels=sseqids)
# foo$sstrand = factor(foo$sstrand, levels=c("plus", "minus"))
# foo$sseqid_strand = interaction(foo$sseqid, foo$sstrand)

head(foo)
dim(foo)

layout(matrix(1:2, 1), respect=TRUE)
barplot(table(foo$length))
# plot(density(foo$mismatch))
# plot(density(foo$gapopen))
# plot(density(-log10(foo$evalue)))
plot(-log10(foo$evalue), foo$length)
# plot(density(foo$bitscore))
# plot(foo$bitscore, foo$length)
layout(1, respect=TRUE)
barplot(table(foo$length))
abline(v=20)

foo$key = paste0(foo$qseqid, "_", foo$sseqid)
foo = foo[order(foo$key, -foo$length),]
foo = foo[!duplicated(foo$key),]
rownames(foo) = foo$key
dim(foo)

idx = rownames(foo)[foo$length >100 & foo$length<401]
length(idx)

sort(table(foo[idx,]$qseqid))


foo[idx[foo[idx,]$qseqid=="chr5:102524331-102524732"],]





stop("EFN")

>chr5:102524331-102524732
tcctcaggtgagaattctttgttcagttctgagccccattttttaatggggttatttgattttctgaagtccaccttcttgagttctttatatatgttggatattagtcccctatctgatttaggataggtaaagatcctttcccaatctgttggtggtctttttgtcttattgacggtgtcttttgccttgcagaaactttggagtttcattaggtcccatttgtcgattctcgatcttacagcacaagcccttgctgttctgttcaggaatttttcccctgtgcccatatcttcaaggcttttccccactttctcctctataagtttcagtgtctctggttttatgtgaagttccttgatccacttagatttgaccttagtacaaggagataagtatgg
>chr2:21598331-21598732
ttcaaggcttttccccactttctcctctataagtttcagtgtctctggttttatgtgaagttccttgatccacttagatttgaccttagtacaaggagataagtatggatcgattcgcattcttctacatgataacaaccagttgtgccagcaccaattgttgaaaatgctgtctttcttccactggatggttttagctcccttgtcgaagatcaagtgaccataggtgtgtgggttcatttctgggtcttcaattctataccattggtctacttgtctgtctctataccagtaccatgcagtttttatcacaattgctctgtagtaaagctttaggtctggcatggtgattccgccagaagttcttttatccttgagaagactttttgctatcctaggtt


chr5:102524331-102524732_chr2:21598331-21598732 





chr5:102524331-102524732_chr1:159027321-159027722     100    110        0
chr5:102524331-102524732_chr1:17964631-17965032       100    123        0
chr5:102524331-102524732_chr1:65413431-65413832       100    135        0
chr5:102524331-102524732_chr1:9734561-9734962         100    131        0
chr5:102524331-102524732_chr10:125821061-125821462    100    118        0
chr5:102524331-102524732_chr10:72734101-72734502      100    116        0
chr5:102524331-102524732_chr13:50130581-50130982      100    131        0
chr5:102524331-102524732_chr14:91801551-91801952      100    129        0
chr5:102524331-102524732_chr14:95271951-95272352      100    123        0
chr5:102524331-102524732_chr15:18319031-18319432      100    112        0
chr5:102524331-102524732_chr15:65606461-65606862      100    109        0
chr5:102524331-102524732_chr16:23753461-23753862      100    119        0
chr5:102524331-102524732_chr16:3389201-3389602        100    106        0
chr5:102524331-102524732_chr16:60738051-60738452      100    124        0
chr5:102524331-102524732_chr17:57653671-57654072      100    142        0
chr5:102524331-102524732_chr18:15948581-15948982      100    119        0
chr5:102524331-102524732_chr18:55901141-55901542      100    119        0
chr5:102524331-102524732_chr2:21598331-21598732       100    108        0
chr5:102524331-102524732_chr2:53780721-53781122       100    109        0
chr5:102524331-102524732_chr2:98447951-98448352       100    120        0
chr5:102524331-102524732_chr3:6711501-6711902         100    108        0
chr5:102524331-102524732_chr3:79638841-79639242       100    103        0
chr5:102524331-102524732_chr3:91021231-91021632       100    115        0
chr5:102524331-102524732_chr4:110471111-110471512     100    109        0
chr5:102524331-102524732_chr4:111238711-111239112     100    110        0
chr5:102524331-102524732_chr4:113210601-113211002     100    110        0
chr5:102524331-102524732_chr5:62033741-62034142       100    112        0
chr5:102524331-102524732_chr6:109646191-109646592     100    127        0
chr5:102524331-102524732_chr6:16924091-16924492       100    125        0
chr5:102524331-102524732_chr6:57057881-57058282       100    117        0
chr5:102524331-102524732_chr7:87550551-87550952       100    102        0
chr5:102524331-102524732_chr8:113099311-113099712     100    135        0
chr5:102524331-102524732_chr8:77886571-77886972       100    111        0
chr5:102524331-102524732_chr9:112620521-112620922     100    135        0
chr5:102524331-102524732_chr9:11726831-11727232       100    103        0
   

keys = unique(c(foo$sseqid,foo$qseqid))
data = matrix(0, length(keys), length(keys))
rownames(data) = colnames(data) = keys
dim(data)
data[1:6, 1:6]
for (k in idx) {
  i = foo[k,]$qseqid 
  j = foo[k,]$sseqid 
  data[i, j] = foo[k,]$length
}




data[1:6, 1:6]

# data[data==401] = 0
# plot(density(log2(data + 1)))
# heatmap(plot(density(log2(data + 1)))
#
#
#
# print(i)
# layout(matrix(1:2, 1), respect=TRUE)
# matrix_file = "tmp/matrix_spectral_10000.txt.gz"
# barplot(counts[[matrix_file]][,i], main=matrix_file, las=2, ylim=c(0,50), xaxt="n")
#
# heatmap


tmp_d = log2(data + 1)
tmp_d = data==401
sum(tmp_d)
# tmp_d[1:nrow(tmp_d), 1:nrow(tmp_d)] = 0
table(apply(tmp_d, 1, sum))







# Go!
normalization=FALSE
# normalization
# colnames(data) = s$exp_grp[colnames(data),]$tissue_group_level1
if (normalization=="zscore_rows" | normalization==TRUE) {
  data = data - apply(data, 1, mean)
  data = data / apply(data, 1, sd)    
} else if (normalization=="zscore_cols") {
  data = t(data)
  data = data - apply(data, 1, mean)
  data = data / apply(data, 1, sd)    
  data = t(data)
} else if (normalization=="rank_cols") {
  data = apply(data, 2, rank)
} else if (normalization=="qqnorm_cols") {
  data = apply(data, 2, function(c) {
    qqnorm(c, plot.it=FALSE)$x
  })
}

hcmeth_cols = FALSE
# clustering samples...
if (hcmeth_cols != FALSE) {
  tmp_d = t(data)
  if (hcmeth_cols == "cor") {
    # ... based on correlation
    tmp_d = tmp_d[!apply(is.na(tmp_d), 1, any), ]
    d = dist(1 - cor(t(tmp_d), method="pe"))
    hc_col = hclust(d, method="complete")
    Colv = as.dendrogram(hc_col)
  } else if (hcmeth_cols == "ordered") {
    # ... ordered by median
    data = data[,order(apply(tmp_d, 1, ordering_func, na.rm=TRUE), decreasing=TRUE)]
    hc_col = Colv = NULL
  } else {
    # ... based on eucl. dist.
    d = dist(tmp_d)
    hc_col = hclust(d, method="complete", members=members)
    Colv = as.dendrogram(hc_col)
  }
} else {
  hc_col = Colv = NULL
}

Colv = dd
ColSideColors = CSC
names(ColSideColors) = colnames(data)



hcmeth_rows = "eucl_dist"
hcmeth_rows = TRUE
# clustering features...
if (hcmeth_rows != FALSE) {
  tmp_d = data
  if (hcmeth_rows == "eucl_dist") {
    # ... based on eucl. dist.
    d = dist(tmp_d)
    hc_row = hclust(d, method="complete")
    Rowv = as.dendrogram(hc_row)
  } else if (hcmeth_rows == "ordered") {
    # ... ordered by median
    data = data[order(apply(tmp_d, 1, ordering_func, na.rm=TRUE), decreasing=TRUE),]
    hc_row = Rowv = NULL
  } else {
    # ... bases on correlation
    tmp_d = tmp_d[!apply(is.na(tmp_d), 1, any), ]
    d = dist(1 - cor(t(tmp_d), method="pe"))
    hc_row = hclust(d, method="complete")
    Rowv = as.dendrogram(hc_row)
  }
} else {
  hc_row = Rowv = NULL
}
RowSideColors = rep("white", nrow(data))
names(RowSideColors) = rownames(data)
```

```{r fig.width=9, fig.height=9, dpi=150}
colors = c("cyan", "black", "red")
# colors = c("cyan", "cyan", "black", "red", "red")
# colors = c("cyan", "cyan", "cyan", "black", "red", "red", "red")
# colors = c("blue", "yellow", "red")
# colors = rev(RColorBrewer::brewer.pal(n=11, "RdYlBu"))
cols = colorRampPalette(colors)(20)
main=""

dendrogram="row"
mgn = lapply(study_tcga_filenames, function(study_tcga_filename) {
  s = mcreate_study(study_tcga_filename)
  tmp_idx_features = rownames(features) #intersect(rownames(features), rownames(s$data))
  idx_nt = rownames(s$exp_grp)[s$exp_grp$tissue_status == "normal"]
  idx_kc = rownames(s$exp_grp)[s$exp_grp$tissue_status == "tumoral"]
  s$exp_grp[idx_kc,]$main_gse_number
})
baz = t(sapply(bar, function(foo) {
  c(foo$main_gse_number,foo$mid_indiv)
}))

data[data > 4] = 4
data[data < -4] = -4

cnd = colnames(data)
names(cnd) = colnames(data)
cnd[names(cnd)] = ""
cnd[baz[,2]] = baz[,1]
colnames(data) = cnd
# colnames(data)[duplicated(unlist(mgn))] = ""
foo = gplots::heatmap.2(data, Rowv=Rowv, Colv=Colv, dendrogram=dendrogram, trace="none", col=cols, main=paste0(main, " (", nrow(data), " features x ", ncol(data), " tissues)"), mar=c(8,8), useRaster=TRUE, RowSideColors=RowSideColors, ColSideColors=ColSideColors, cexRow=0.6, cexCol=0.6)

































 # sapply(counts,function(d) {
 #   # d = counts[[matrix_file]]
 #   t(d[,i])
 # })
 head(tmp_d)
 dim(tmp_d)
 q = sort(unique(quantile(tmp_d, probs=seq(0,1,length.out=20), na.rm=TRUE)))
 q = c(-1,q)
 colors=c("royalblue", "springgreen", "yellow", "red")
 cols = colorRampPalette(colors)(length(q)-1)
 # image(tmp_d, col=cols, breaks=q, xaxt="n", yaxt="n", main="", useRaster=FALSE)

 # idx = 1:ncol(counts)
 # idx = unique(c(1,floor(seq(1, ncol(counts), l=10))))
 # axis(2, ((1:ncol(counts)-1)/(ncol(counts)-1))[idx], colnames(counts)[idx], las=2)
 # idx = unique(floor((1:(nrow(counts)-1))/10) * 10) + 1
 # axis(1, ((1:nrow(counts)-1)/(nrow(counts)-1))[idx], signif(seq(0,20, length.out=nrow(counts))[idx], 2), las=2)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
     """
    


rule compile_blastdb:
    input: os.path.expanduser("~/projects/heatshock/data/{subject}.fasta")
    output: os.path.expanduser("~/projects/heatshock/data/{subject}.blast.db")
    threads: 1
    shell:"""
/summer/epistorage/miniconda3/envs/mnase_env/bin/makeblastdb -in {input} -dbtype nucl -parse_seqids -out {output}
touch {output}
    """
    
rule blastn_ggaat:
    input:
      blast_db=os.path.expanduser("~/projects/heatshock/data/{subject}.blast.db"),
      query_fqgz="{prefix}/{sample}_1.fastq.gz",
    output: "{prefix}/{sample}_{subject}.blasted.txt.gz"
    threads: 1
    shell:"""
gunzip -c {input.query_fqgz} | /summer/epistorage/miniconda3/envs/mnase_env/bin/seqtk seq -A | 
/summer/epistorage/miniconda3/envs/mnase_env/bin/blastn -db {input.blast_db} -num_threads=1 -query - -outfmt "10 std sstrand" -evalue 10 -task blastn-short -word_size 8 -perc_identity 100 -qcov_hsp_perc 1  2>/dev/null | gzip  > {output}
    """


rule blastn_unmapped_ggaat:
    input:
      blast_db=os.path.expanduser("~/projects/heatshock/data/{subject}.blast.db"),
      query_fqgz="{prefix}/{sample}_{trim}_star_{species}_{index}_Unmapped.out.mate1.gz",
    output: "{prefix}/{sample}_{trim}_star_{species}_{index}_{subject}.unmapblasted.txt.gz"
    threads: 1
    shell:"""
cat {input.query_fqgz} | /summer/epistorage/miniconda3/envs/mnase_env/bin/seqtk seq -A | 
/summer/epistorage/miniconda3/envs/mnase_env/bin/blastn -db {input.blast_db} -num_threads=1 -query - -outfmt "10 std sstrand" -evalue 10 -task blastn-short -word_size 8 -perc_identity 100 -qcov_hsp_perc 1  2>/dev/null | gzip  > {output}
    """



rule trim_fastxtoolkit:
    input:
      fastq="{prefix}.fastq.gz", 
      fastqc="{prefix}_fastqc.zip",
    output: "{prefix}_fastxtrimf{trim}.fastq.gz"
    threads: 1
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
tmpfile=$(mktemp /var/tmp/tmp_trimed_file_XXXXXXXXXX.fq.gz)
echo computing $tmpfile ...
gunzip -c  {input.fastq} | fastx_trimmer -l {wildcards.trim} -Q33 -z -o $tmpfile
echo move $tmpfile to output.
cp $tmpfile {output}
rm $tmpfile
    """

rule count_bowtie:
    input:
      bam_file="{prefix}/{sample}_{localendtoend}_trim{trim}.bam",
      gtf_file= "/scratch_r730/datashare/genomes/Mus_musculus/UCSC/mm10/Annotation/Genes/genes.gtf"
    output: "{prefix}/{sample}_{localendtoend}_trim{trim}_gene_counts.txt"
    priority: 50000
    threads: 1
    shell:"""
/summer/epistorage/miniconda3/envs/mnase_env/bin/htseq-count -f bam -r name -s no -m intersection-nonempty \
  {input.bam_file} \
  {input.gtf_file} \
  > {output}
    """


          

rule bigwig_coverage_advanced_PESF:
    input: "{prefix}_srt.bam", 
    output: "{prefix}_srt_PESF_{mmq}_{binsize}_None_SF{sf}.bw"
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
  --normalizeUsing None \
  --scaleFactor {wildcards.sf} \
  -o {output}

    """

rule bigwig_coverage_advanced_PESF_mmq30:
    input: "{prefix}_srt_mmq30.bam", 
    output: "{prefix}_srt_mmq30_PESF_{mmq}_{binsize}_None_SF{sf}.bw"
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
  --normalizeUsing None \
  --scaleFactor {wildcards.sf} \
  -o {output}

    """
    
          
          
          
rule fastqc:
    input:  fastqgz="{prefix}.fastq.gz"
    output: zip="{prefix}_fastqc.zip",
            html="{prefix}_fastqc.html"
    threads: 1
    shell:"""
    PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
    fastqc {input.fastqgz}
    """









rule index_genome:
    input:
      genome_fasta="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Sequence/WholeGenomeFasta/genome.fa", 
      gtf="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Annotation/Genes/genes.gtf",
    output: directory("/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Sequence/StarIndex")
    #priority: 0
    threads: 32
    shell:    """
mkdir -p {output}
/summer/epistorage/miniconda3/envs/mnase_env/bin/STAR \
  --runThreadN `echo "$(({threads} * 2))"` \
  --runMode genomeGenerate \
  --genomeDir {output} \
  --genomeFastaFiles  {input.genome_fasta} \
  --sjdbGTFfile {input.gtf} \
  --sjdbOverhang 100
    """


      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn1_local_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      #  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn1_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.info

rule align_trimed:
    input:
      # fqgz_file="{prefix}/{sample}_{trim}.fastq.gz",
      # fastqc_file="{prefix}/{sample}_{trim}_fastqc.zip",
      fastq_info="{prefix}/{sample}_{trim}_fqgz.info",
      star_index="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Sequence/StarIndex",
      # star_index_file="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Sequence/StarIndex/SAindex",
      gtf="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Annotation/Genes/genes.gtf",
    output:  "{prefix}/{sample}_{trim}_star_{species}_{index}_Aligned.sortedByCoord.out.bam"
    threads: 32
    shell:"""
cd {wildcards.prefix}
/summer/epistorage/miniconda3/envs/mnase_env/bin/STAR \
  --runThreadN {threads} \
  --genomeDir  {input.star_index} \
  --sjdbGTFfile {input.gtf} \
  --readFilesCommand gunzip -c \
  --readFilesIn `cat {input.fastq_info}` \
  --outFileNamePrefix {wildcards.prefix}/{wildcards.sample}_{wildcards.trim}_star_{wildcards.species}_{wildcards.index}_ \
  --outReadsUnmapped Fastx \
  --outSAMtype BAM SortedByCoordinate
sleep 30
echo "indexing bam_file"
/summer/epistorage/miniconda3/envs/mnase_env/bin/samtools index {output}
    """







rule count_classic:
    input:
      bam_file="{prefix}/{sample}_{sr_or_pe}_{trim}_star_{species}_{index}_Aligned.sortedByCoord.out.bam",
      gtf_file= "/scratch_r730/datashare/genomes/{species}/UCSC/{index}/Annotation/Genes/genes.gtf" 
    output: "{prefix}/{sample}_{sr_or_pe}_{trim}_star_{species}_{index}_gene_counts.txt"
    # priority: 50
    threads: 1
    shell:"""
/summer/epistorage/miniconda3/envs/mnase_env/bin/htseq-count -f bam -r name -s no -m intersection-nonempty \
  {input.bam_file} \
  {input.gtf_file} \
  > {output}
    """

# rule bigwig_coverage:
#     input:
#       bam_file="{prefix}/{sample}_{sr_or_pe}_{trim}_star_{species}_{index}_Aligned.sortedByCoord.out.bam",
#     output: "{prefix}/{sample}_{sr_or_pe}_{trim}_star_{species}_{index}_Aligned.sortedByCoord.out.bw"
#     threads: 4
#     shell:"""
# /summer/epistorage/miniconda3/envs/mnase_env/bin/bamCoverage \
#   -b {input.bam_file} \
#   --numberOfProcessors `echo "$(({threads} * 2))"` \
#   --binSize 10 \
#   --minMappingQuality 30 \
#   --normalizeUsingRPKM \
#   -o {output}
#
#     """