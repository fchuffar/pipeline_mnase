cd ~/projects/all_tchin/results/chip_gao_novogen
source config
echo $gse
echo $project
## bw are there
echo ~/projects/${datashare}/${gse}/.
## QC is here
echo ~/projects/${datashare}/${gse}/multiqc_notrim.html
echo ~/projects/${project}/results/${gse}/ 
echo ~/projects/${datashare}/${gse}
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/

# transfering data on summer 
mkdir -p ~/projects/${datashare}/${gse}
cd ~/projects/${datashare}/${gse}
# rsync -auvP /Volumes/datashare1/datashare/chip_gao_novogen/ cargo:~/projects/datashare_epistorage/chip_gao_novogen/

# check MD5
cd ~/projects/datashare_epistorage/chip_gao_novogen/raw/delivered/
ls -lha *.*data/*/*.fq.gz
cat  *.*data/*/*.txt > md5.orig.txt
cat md5.orig.txt
# md5sum *.*data/*/*.fq.gz > md5.summer.txt &
# tail -f md5.summer.txt
cat md5.orig.txt| cut -f1 -d" " > tmp1
# cat md5.bettik.txt| cut -f1 -d" " > tmp2
cat md5.summer.txt| cut -f1 -d" " > tmp3
diff tmp1 tmp3

# design 
# ChIP Bu Ac REH,
# K5Ac    WT  
# K5Bu  x KO1 = 12 conditions
# BRD4    KO2 
# Input
cd ~/projects/datashare_epistorage/chip_gao_novogen/raw/
ls -lha delivered/2.cleandata/*/*.fq.gz

ln -s delivered/2.cleandata/KO1-BRD4_FMRC210105505-1a/KO1-BRD4_FMRC210105505-1a_1.clean.fq.gz   ./KO1_BRD4_R1.fastq.gz
ln -s delivered/2.cleandata/KO1-BRD4_FMRC210105505-1a/KO1-BRD4_FMRC210105505-1a_2.clean.fq.gz   ./KO1_BRD4_R2.fastq.gz
ln -s delivered/2.cleandata/KO1-Input_FMRC210105496-1a/KO1-Input_FMRC210105496-1a_1.clean.fq.gz ./KO1_Inpu_R1.fastq.gz
ln -s delivered/2.cleandata/KO1-Input_FMRC210105496-1a/KO1-Input_FMRC210105496-1a_2.clean.fq.gz ./KO1_Inpu_R2.fastq.gz
ln -s delivered/2.cleandata/KO1-K5ac_FMRC210105499-1a/KO1-K5ac_FMRC210105499-1a_1.clean.fq.gz   ./KO1_K5ac_R1.fastq.gz
ln -s delivered/2.cleandata/KO1-K5ac_FMRC210105499-1a/KO1-K5ac_FMRC210105499-1a_2.clean.fq.gz   ./KO1_K5ac_R2.fastq.gz
ln -s delivered/2.cleandata/KO1-K5bu_FMRC210105502-1a/KO1-K5bu_FMRC210105502-1a_1.clean.fq.gz   ./KO1_K5bu_R1.fastq.gz
ln -s delivered/2.cleandata/KO1-K5bu_FMRC210105502-1a/KO1-K5bu_FMRC210105502-1a_2.clean.fq.gz   ./KO1_K5bu_R2.fastq.gz
ln -s delivered/2.cleandata/KO2-BRD4_FMRC210105506-1a/KO2-BRD4_FMRC210105506-1a_1.clean.fq.gz   ./KO2_BRD4_R1.fastq.gz
ln -s delivered/2.cleandata/KO2-BRD4_FMRC210105506-1a/KO2-BRD4_FMRC210105506-1a_2.clean.fq.gz   ./KO2_BRD4_R2.fastq.gz
ln -s delivered/2.cleandata/KO2-Input_FMRC210105497-1a/KO2-Input_FMRC210105497-1a_1.clean.fq.gz ./KO2_Inpu_R1.fastq.gz
ln -s delivered/2.cleandata/KO2-Input_FMRC210105497-1a/KO2-Input_FMRC210105497-1a_2.clean.fq.gz ./KO2_Inpu_R2.fastq.gz
ln -s delivered/2.cleandata/KO2-K5ac_FMRC210105500-1a/KO2-K5ac_FMRC210105500-1a_1.clean.fq.gz   ./KO2_K5ac_R1.fastq.gz
ln -s delivered/2.cleandata/KO2-K5ac_FMRC210105500-1a/KO2-K5ac_FMRC210105500-1a_2.clean.fq.gz   ./KO2_K5ac_R2.fastq.gz
ln -s delivered/2.cleandata/KO2-K5bu_FMRC210105503-1a/KO2-K5bu_FMRC210105503-1a_1.clean.fq.gz   ./KO2_K5bu_R1.fastq.gz
ln -s delivered/2.cleandata/KO2-K5bu_FMRC210105503-1a/KO2-K5bu_FMRC210105503-1a_2.clean.fq.gz   ./KO2_K5bu_R2.fastq.gz
ln -s delivered/2.cleandata/WT-BRD4_FMRC210105504-1a/WT-BRD4_FMRC210105504-1a_1.clean.fq.gz     ./WTy_BRD4_R1.fastq.gz
ln -s delivered/2.cleandata/WT-BRD4_FMRC210105504-1a/WT-BRD4_FMRC210105504-1a_2.clean.fq.gz     ./WTy_BRD4_R2.fastq.gz
ln -s delivered/2.cleandata/WT-Input_FMRC210105495-1a/WT-Input_FMRC210105495-1a_1.clean.fq.gz   ./WTy_Inpu_R1.fastq.gz
ln -s delivered/2.cleandata/WT-Input_FMRC210105495-1a/WT-Input_FMRC210105495-1a_2.clean.fq.gz   ./WTy_Inpu_R2.fastq.gz
ln -s delivered/2.cleandata/WT-K5ac_FMRC210105498-1a/WT-K5ac_FMRC210105498-1a_1.clean.fq.gz     ./WTy_K5ac_R1.fastq.gz
ln -s delivered/2.cleandata/WT-K5ac_FMRC210105498-1a/WT-K5ac_FMRC210105498-1a_2.clean.fq.gz     ./WTy_K5ac_R2.fastq.gz
ln -s delivered/2.cleandata/WT-K5bu_FMRC210105501-1a/WT-K5bu_FMRC210105501-1a_1.clean.fq.gz     ./WTy_K5bu_R1.fastq.gz
ln -s delivered/2.cleandata/WT-K5bu_FMRC210105501-1a/WT-K5bu_FMRC210105501-1a_2.clean.fq.gz     ./WTy_K5bu_R2.fastq.gz

# metadata
cd ~/projects/datashare_epistorage/${gse}/
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/KO1_BRD4_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/KO1_BRD4_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/KO1_BRD4_R1_trimno.info      
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/KO1_Inpu_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/KO1_Inpu_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/KO1_Inpu_R1_trimno.info      
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/KO1_K5ac_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/KO1_K5ac_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/KO1_K5ac_R1_trimno.info 
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/KO1_K5bu_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/KO1_K5bu_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/KO1_K5bu_R1_trimno.info 
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/KO2_BRD4_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/KO2_BRD4_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/KO2_BRD4_R1_trimno.info  
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/KO2_Inpu_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/KO2_Inpu_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/KO2_Inpu_R1_trimno.info  
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/KO2_K5ac_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/KO2_K5ac_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/KO2_K5ac_R1_trimno.info      
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/KO2_K5bu_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/KO2_K5bu_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/KO2_K5bu_R1_trimno.info      
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/WTy_BRD4_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/WTy_BRD4_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/WTy_BRD4_R1_trimno.info 
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/WTy_Inpu_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/WTy_Inpu_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/WTy_Inpu_R1_trimno.info
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/WTy_K5ac_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/WTy_K5ac_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/WTy_K5ac_R1_trimno.info 
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/WTy_K5bu_R1.fastq.gz -2 /home/fchuffar/projects/${datashare}/${gse}/raw/WTy_K5bu_R2.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/WTy_K5bu_R1_trimno.info 
ls -lha 

cat *.info


## qc align count
# put wf on dahu and launch
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
cd ~/projects/${project}/results/${gse}/
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 16 -pn
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 49 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn


## get results
mkdir -p ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/*.txt ~/projects/${datashare}/${gse}/
rsync -auvP dahu:~/projects/${datashare}/${gse}/raw/*.html ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/multiqc_notrim* ~/projects/${datashare}/${gse}/



rsync -auvP cargo:~/projects/datashare_epistorage/chip_hira_ssrp1/Input_KO_rep1_end-to-end_trim30_srt_PE_30_4_RPKM.bw ~/projects/datashare_epistorage/chip_hira_ssrp1/.
