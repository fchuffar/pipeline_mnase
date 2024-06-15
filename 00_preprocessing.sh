# 1. Set parameters there and in *config* file. 
## The two main setable parameters are *project* (the global project) *gse* (the batch/run of fastq files)
cd ~/projects/cometh/results/atacseq_cometh_lot4
source config
echo $gse
echo $project
## push to dahu
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/


# 2. Put raw fastq file in ~/projects/datashare/${gse}/raw
mkdir -p ~/projects/datashare/${gse}/raw
cd ~/projects/datashare/${gse}/raw
# done previously using https://github.com/fchuffar/gse2study

## download fastq files
# wget https://ftp.ncbi.nlm.nih.gov/sra/reports/Metadata/SRA_Accessions.tab
sra=`cat ~/projects/datashare/platforms/SRA_Accessions.tab | grep ${gse} | cut -f1 | grep SRA`
echo $sra
srrs=`cat ~/projects/datashare/platforms/SRA_Accessions.tab | grep RUN | grep ${sra}| cut -f1 | grep SRR`
echo $srrs
echo $srrs | wc

conda activate sra_env
echo "checking" $srrs >> checking_srrs_report.txt
for srr in $srrs
do
  FILE=${srr}.fastq
  if [ -f $FILE ]; then
     echo "File $FILE exists."
  else
     echo "File $FILE does not exist."
     fasterq-dump --threads 16 -p --temp /dev/shm --split-files --outdir ./ ${srr}
  fi
done
cat checking_srrs_report.txt
gzip *.fastq


# 3. QC/Trim fastq files using 01_trim_fastq_files.py 
source ~/conda_config.sh 
conda activate mnase_env
cd ~/projects/${project}/results/${gse}/
ls -lha ~/projects/datashare/${gse}/raw/*.fastq.gz
## set targets in 01_trim_fastq_files.py, then launch pipeline on a node:
snakemake -k -s 01_trim_fastq_files.py --cores 16 -pn
## or on the dahu cluster:
snakemake -k -s 01_trim_fastq_files.py --jobs 50 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn


# 4. Design. Link here samples and fastqz unsing .info file.
cd  /home/chuffarf/projects/datashare/${gse}
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/01_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/01_R2_fastxtrimf30.fastq.gz " > 01_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/02_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/02_R2_fastxtrimf30.fastq.gz " > 02_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/03_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/03_R2_fastxtrimf30.fastq.gz " > 03_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/04_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/04_R2_fastxtrimf30.fastq.gz " > 04_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/05_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/05_R2_fastxtrimf30.fastq.gz " > 05_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/06_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/06_R2_fastxtrimf30.fastq.gz " > 06_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/07_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/07_R2_fastxtrimf30.fastq.gz " > 07_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/08_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/08_R2_fastxtrimf30.fastq.gz " > 08_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/09_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/09_R2_fastxtrimf30.fastq.gz " > 09_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/10_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/10_R2_fastxtrimf30.fastq.gz " > 10_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/11_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/11_R2_fastxtrimf30.fastq.gz " > 11_trim30.info
echo " -1 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/12_R1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/atacseq_cometh_lot4/raw/12_R2_fastxtrimf30.fastq.gz " > 12_trim30.info

# echo " -U /home/chuffarf/projects/datashare/GSE77277/raw/SRR3126242_fastxtrimf30.fastq.gz "  > GSM2047206_trim30.info

# echo " -1  /home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-165165_R1_001_fastxtrimf30.fastq.gz, /home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-172172_R1_001_fastxtrimf30.fastq.gz    -2  /home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-165165_R2_001_fastxtrimf30.fastq.gz, /home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-172172_R2_001_fastxtrimf30.fastq.gz   "  > S_pp2_trim30.info
## and set samples there:

cat  *_trim30.info

cd ~/projects/${project}/results/${gse}/
cat config.R



## 5. Align and wiggle
cd ~/projects/${project}/results/${gse}/
## set targets in 02_align_fastq_files.py, then launch pipeline on a node:
snakemake -k -s 02_align_fastq_files.py --cores 16 -pn
## or on the dahu cluster:
snakemake -k -s 02_align_fastq_files.py --jobs 50 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn


#/home/fchuffar/projects/datashare/genomes/Candida_albicans/CGD/SC5314.A22/Annotation/Genes/genes.gtf 
# cat /home/fchuffar/projects/datashare/genomes/Candida_albicans/CGD/SC5314.A22/Annotation/Genes/genes.gtf  |  awk 'OFS="\t" {if ($3=="CDS") {print $1,$4-1,$5,$10,$6,$7}}' | tr -d '";' > /home/fchuffar/projects/datashare/genomes/Candida_albicans/CGD/SC5314.A22/Annotation/Genes/genes.bed
# cat /home/fchuffar/projects/datashare/genomes/Homo_sapiens/UCSC/hg38/Annotation/Genes/genes.gtf  |  awk 'OFS="\t" {if ($3=="CDS") {print $1,$4-1,$5,$10,$6,$7}}' | tr -d '";' > /home/fchuffar/projects/datashare/genomes/Homo_sapiens/UCSC/hg38/Annotation/Genes/genes.bed
# 6. 03_metagene.Rmd and so on
source ~/conda_config.sh 
conda activate mnase_env
## set samples in the config.R file then under R:
rmarkdown::render("03_metagene.Rmd")
rmarkdown::render("03_fragment_length.Rmd")
# source(knitr::purl("05_spectral_coverage.Rmd"))
rmarkdown::render("05_spectral_coverage.Rmd")


#7. split bam according to fragment lengths
cd ~/projects/${project}/results/${gse}/
## set targets in 06_split_bam_frag_length.py, then launch pipeline on a node:
snakemake -k -s 06_split_bam_frag_length.py --cores 16 -pn
## or on the dahu cluster:
snakemake -k -s 06_split_bam_frag_length.py  --jobs 50 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn



rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
cd ~/projects/${project}/results/${gse}/
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 16 -pn
snakemake -s ~/projects/${project}/results/${gse}/wf.py --jobs 49 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn


### DESIGN
cd ~/projects/datashare/${gse}/
echo " -1 /home/fchuffar/projects/datashare/mmspz/raw/input_rep10_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/mmspz/raw/input_rep10_R2_fastxtrimf30.fastq.gz " > input_rep10_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/mmspz/raw/cth2b_rep11_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/mmspz/raw/cth2b_rep11_R2_fastxtrimf30.fastq.gz " > cth2b_rep11_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/mmspz/raw/cth2b_rep12_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/mmspz/raw/cth2b_rep12_R2_fastxtrimf30.fastq.gz " > cth2b_rep12_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/mmspz/raw/input_rep20_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/mmspz/raw/input_rep20_R2_fastxtrimf30.fastq.gz " > input_rep20_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/mmspz/raw/cth2b_rep21_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/mmspz/raw/cth2b_rep21_R2_fastxtrimf30.fastq.gz " > cth2b_rep21_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/mmspz/raw/cth2b_rep22_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/mmspz/raw/cth2b_rep22_R2_fastxtrimf30.fastq.gz " > cth2b_rep22_trim30.info 
ls -lha
cat *.info
pwd

###
mkdir -p ~/projects/datashare/${gse}/raw/
rsync -auvP dahu:~/projects/datashare/${gse}/raw/multiqc_notrim.html ~/projects/datashare/${gse}/raw/.
open ~/projects/datashare/${gse}/raw/multiqc_notrim.html



## QC is here
echo ~/projects/datashare/${gse}/raw/multiqc_notrim.html
echo ~/projects/${project}/results/${gse}/ 
echo ~/projects/datashare/${gse}

### FASTQ
cd ~/projects/datashare/${gse}/raw/
ls -lha *.fastq.gz

## get results
mkdir -p ~/projects/datashare/${gse}/raw/
rsync -auvP dahu:~/projects/datashare/${gse}/*.txt ~/projects/datashare/${gse}/
rsync -auvP dahu:~/projects/datashare/${gse}/raw/*.html ~/projects/datashare/${gse}/raw/
rsync -auvP dahu:~/projects/datashare/${gse}/multiqc_notrim* ~/projects/datashare/${gse}/
rsync -auvP dahu:~/projects/datashare/${gse}/*_mmq30.bam* ~/projects/datashare/${gse}/ --dry-run


normal_chip_nme2wt_m301 1.338421
normal_chip_nme2wt_m302 1.033158
hghfat_chip_nme2wt_m300 1.550526
hghfat_chip_nme2wt_m303 1.964737
normal_chip_nme2ko_m291 1.093158
normal_chip_nme2ko_m293 1.528421
hghfat_chip_nme2ko_m273 1.419474
hghfat_chip_nme2ko_m292 1.426842



bamCoverage -b in_wt_notrim.srt.bam --extendReads --numberOfProcessors 32 --binSize 4 --minMappingQuality 30 --normalizeUsing None --scaleFactor $sf_in_wt_dm6 -o in_wt_notrim_scalf.bw
bamCoverage -b in_g3_notrim.srt.bam --extendReads --numberOfProcessors 32 --binSize 4 --minMappingQuality 30 --normalizeUsing None --scaleFactor $sf_in_g3_dm6 -o in_g3_notrim_scalf.bw
bamCoverage -b in_g5_notrim.srt.bam --extendReads --numberOfProcessors 32 --binSize 4 --minMappingQuality 30 --normalizeUsing None --scaleFactor $sf_in_g5_dm6 -o in_g5_notrim_scalf.bw
bamCoverage -b ac_wt_notrim.srt.bam --extendReads --numberOfProcessors 32 --binSize 4 --minMappingQuality 30 --normalizeUsing None --scaleFactor $sf_ac_wt_dm6 -o ac_wt_notrim_scalf.bw
bamCoverage -b ac_g3_notrim.srt.bam --extendReads --numberOfProcessors 32 --binSize 4 --minMappingQuality 30 --normalizeUsing None --scaleFactor $sf_ac_g3_dm6 -o ac_g3_notrim_scalf.bw
bamCoverage -b ac_g5_notrim.srt.bam --extendReads --numberOfProcessors 32 --binSize 4 --minMappingQuality 30 --normalizeUsing None --scaleFactor $sf_ac_g5_dm6 -o ac_g5_notrim_scalf.bw
bamCoverage -b cr_wt_notrim.srt.bam --extendReads --numberOfProcessors 32 --binSize 4 --minMappingQuality 30 --normalizeUsing None --scaleFactor $sf_cr_wt_dm6 -o cr_wt_notrim_scalf.bw
bamCoverage -b cr_g3_notrim.srt.bam --extendReads --numberOfProcessors 32 --binSize 4 --minMappingQuality 30 --normalizeUsing None --scaleFactor $sf_cr_g3_dm6 -o cr_g3_notrim_scalf.bw
bamCoverage -b cr_g5_notrim.srt.bam --extendReads --numberOfProcessors 32 --binSize 4 --minMappingQuality 30 --normalizeUsing None --scaleFactor $sf_cr_g5_dm6 -o cr_g5_notrim_scalf.bw





Acc1 Acaca "chr11:84190000-84200000"
Acly       "chr11:100523000-100533000"
Scd1       "chr19:44403000-44413000"
Cebpa      "chr7:35115000-35125000"
Ppargc1a   "chr5:51548000-51558000"
Srebf1     "chr11:60216000-60226000"
Pparg      "chr6:115356000-115366000"
Ppara      "chr15:85731000-85741000"






/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr11:84190000-84200000"       # Acc1 Acaca 
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr11:100523000-100533000"     # Acly       
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr19:44403000-44413000"       # Scd1       
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr7:35115000-35125000"        # Cebpa      
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr5:51548000-51558000"        # Ppargc1a   
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr11:60216000-60226000"       # Srebf1     
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr6:115356000-115366000"      # Pparg      
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr15:85731000-85741000"       # Ppara      







/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 igv_session.xml -p "chr11:84190000-84200000"       # Acc1 Acaca 
