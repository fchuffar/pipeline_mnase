# 1. Set parameters there and in *config* file. 
## The two main setable parameters are *project* (the global project) *gse* (the batch/run of fastq files)
cd ~/projects/atacclock/results/GSE193140
source config
echo $gse
echo $project
## push to dahu
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/


# 2. Put raw fastq file in ~/projects/datashare/${gse}/raw
mkdir -p ~/projects/datashare/${gse}/raw
cd ~/projects/datashare/${gse}/raw
# done previously using https://github.com/fchuffar/gse2study


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
## SR or PE?
ls -lha ~/projects/datashare/${gse}/raw
if [[ -f ${srr}_2.fastq || -f ${srr}_2.fastq.gz ]]; then
  sequencing_read_type=PE
else
  sequencing_read_type=SR
fi
echo $sequencing_read_type
## metadata linking sample and raw files
gsms=`cat ~/projects/datashare/platforms/SRA_Accessions_${srp}.tab | grep RUN | grep ${srp} | cut -f10 | cut -f1 -d_ | uniq`
echo $gsms
echo $gsms | wc
cd ~/projects/datashare/${gse}/
for gsm in $gsms
do
  echo ${gsm}  
  srrs=`cat ~/projects/datashare/platforms/SRA_Accessions_${srp}.tab | grep RUN | grep ${gsm} | cut -f1 | grep SRR | sort`
  echo ${srrs}    
  if [[ $sequencing_read_type == PE ]]; then
    # PE
    echo PE    
    echo " -1 /home/chuffarf/projects/datashare/${gse}/raw/`echo $srrs | sed 's/ /_1\.fastq\.gz,raw\//g'`_1_fastxtrimf30.fastq.gz -2 /home/chuffarf/projects/datashare/${gse}/raw/`echo $srrs | sed 's/ /_1\.fastq\.gz,raw\//g'`_2_fastxtrimf30.fastq.gz " > ${gsm}_trim30.info
  else
   #  # # SR
   echo SR
    echo " -U /home/chuffarf/projects/datashare/${gse}/raw/`echo $srrs | sed 's/ /_1\.fastq\.gz,raw\//g'`_fastxtrimf30.fastq.gz " > ${gsm}_trim30.info
  fi
done
cat  *_trim30.info
## and set samples there:
cd ~/projects/${project}/results/${gse}/
echo "samples = c("         >  config.R                                                                    
for gsm in $gsms                                                        
do                                                        
  echo "  '${gsm}',     "   >> config.R                                                                
done                                                        
echo ")           "         >> config.R                                                         
cat config.R                                                        




## 5. Align and wiggle
cd ~/projects/${project}/results/${gse}/
## set targets in 02_align_fastq_files.py, then launch pipeline on a node:
snakemake -k -s 02_align_fastq_files.py --cores 16 -pn
## or on the dahu cluster:
snakemake -k -s 02_align_fastq_files.py --jobs 50 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn
## QC is there:
echo ${project}/results/${study}/multiqc_notrim.html

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
