<<<<<<< HEAD
cd ~/projects/atad2/results/chip_hira_ssrp1
=======
cd ~/projects/atad2/results/GSE70312
>>>>>>> e40209656a670e34b3a9fde1da524381f15d2482
source config
echo $gse
echo $project
## bw are there
echo ~/projects/${datashare}/${gse}/.
## QC is here
echo ~/projects/${datashare}/${gse}/multiqc_notrim.html
echo ~/projects/${project}/results/${gse}/ 
echo ~/projects/${datashare}/${gse}

<<<<<<< HEAD
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
=======
# GSM1723635 SRR2079661 ES_Atad2tag_AntiHA  
# GSM1723636 SRR2079662 ES wild type_antiHA 
>>>>>>> e40209656a670e34b3a9fde1da524381f15d2482

# Dear Florent,
# The samples are Embryonic Stem cells(cell line 46C) and KOs are ATAD2 KO.
# SSRP1 is a sub-unit of histone chaperone FACT and HIRA is another histone chaperone.
# Tao could you confirme.
# Thanks
# Saadi
#
# -rw-r--r-- 1 chuffarf l-iab        2.1G Nov 25 13:40 S003914_1_Input_WT-1_1.fastq.gz
# -rw-r--r-- 1 chuffarf l-iab        2.1G Nov 25 13:06 S003915_2_Input_KO-1_1.fastq.gz
# -rw-r--r-- 1 chuffarf l-iab        1.6G Nov 25 13:09 S003916_3_SSRP1-CHIP_WT-1_1.fastq.gz
# -rw-r--r-- 1 chuffarf l-iab        2.0G Nov 25 13:58 S003917_4_SSRP1-CHIP_KO-1_1.fastq.gz
# -rw-r--r-- 1 chuffarf l-iab        1.9G Nov 25 13:47 S003918_5_HIRA-CHIP_WT-1_1.fastq.gz
# -rw-r--r-- 1 chuffarf f-epimedcore 1.7G Nov 25 12:55 S003919_6_HIRA-CHIP_KO-1_1.fastq.gz
# -rw-r--r-- 1 chuffarf l-iab        2.0G Nov 25 13:16 S003920_7_Input_WT-2_1.fastq.gz
# -rw-r--r-- 1 chuffarf l-iab        2.2G Nov 25 13:54 S003921_8_Input_KO-2_1.fastq.gz
# -rw-r--r-- 1 chuffarf l-iab        1.8G Nov 25 13:50 S003922_9_SSRP1-CHIP_WT-2_1.fastq.gz
# -rw-r--r-- 1 chuffarf l-iab        1.7G Nov 25 13:13 S003923_10_SSRP1-CHIP_KO-2_1.fastq.gz
# -rw-r--r-- 1 chuffarf f-epimedcore 1.8G Nov 25 12:51 S003924_11_HIRA-CHIP_WT-2_1.fastq.gz
# -rw-r--r-- 1 chuffarf l-iab        1.7G Nov 25 12:58 S003925_12_HIRA-CHIP_KO-2_1.fastq.gz


mkdir -p ~/projects/${datashare}/${gse}
cd ~/projects/${datashare}/${gse}
ln -s  ~/projects/datashare_epistorage/TGML_runs/fastq/202011030_R338_SK/fastq raw

# SR or PE?
ls -lha ~/projects/${datashare}/${gse}/raw
sequencing_read_type=PE

<<<<<<< HEAD
=======
## metadata linking sample and raw files
gsms=`cat ~/projects/${datashare}/platforms/SRA_Accessions.tab | grep RUN | grep ${sra} | cut -f10 | cut -f1 -d_ | uniq`
echo $gsms
echo $gsms | wc
cd ~/projects/${datashare}/${gse}/
for gsm in $gsms
do
  # echo ${gsm}
  srrs=`cat ~/projects/${datashare}/platforms/SRA_Accessions.tab | grep RUN | grep ${gsm} | cut -f1 | grep SRR | sort`
  echo $srrs ${gsm}
  # echo raw/`echo $srrs | sed 's/ /_1\.fastq\.gz,raw\//g'`_1.fastq.gz raw/`echo $srrs | sed 's/ /_2\.fastq\.gz,raw\//g'`_2.fastq.gz > ${gsm}_notrim_fqgz.info
done
>>>>>>> e40209656a670e34b3a9fde1da524381f15d2482

ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003914_1_Input_WT-1_1.fastq.gz      
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003915_2_Input_KO-1_1.fastq.gz      
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003916_3_SSRP1-CHIP_WT-1_1.fastq.gz
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003917_4_SSRP1-CHIP_KO-1_1.fastq.gz
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003918_5_HIRA-CHIP_WT-1_1.fastq.gz 
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003919_6_HIRA-CHIP_KO-1_1.fastq.gz 
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003920_7_Input_WT-2_1.fastq.gz      
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003921_8_Input_KO-2_1.fastq.gz      
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003922_9_SSRP1-CHIP_WT-2_1.fastq.gz
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003923_10_SSRP1-CHIP_KO-2_1.fastq.gz
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003924_11_HIRA-CHIP_WT-2_1.fastq.gz
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003925_12_HIRA-CHIP_KO-2_1.fastq.gz
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003914_1_Input_WT-1_2.fastq.gz       
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003915_2_Input_KO-1_2.fastq.gz       
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003916_3_SSRP1-CHIP_WT-1_2.fastq.gz  
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003917_4_SSRP1-CHIP_KO-1_2.fastq.gz  
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003918_5_HIRA-CHIP_WT-1_2.fastq.gz   
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003919_6_HIRA-CHIP_KO-1_2.fastq.gz   
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003920_7_Input_WT-2_2.fastq.gz       
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003921_8_Input_KO-2_2.fastq.gz       
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003922_9_SSRP1-CHIP_WT-2_2.fastq.gz  
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003923_10_SSRP1-CHIP_KO-2_2.fastq.gz 
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003924_11_HIRA-CHIP_WT-2_2.fastq.gz  
ls -lha /home/fchuffar/projects/${datashare}/${gse}/raw/S003925_12_HIRA-CHIP_KO-2_2.fastq.gz  

<<<<<<< HEAD
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003914_1_Input_WT-1_1_fastxtrimf30.fastq.gz        -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003914_1_Input_WT-1_2_fastxtrimf30.fastq.gz       " > /home/fchuffar/projects/${datashare}/${gse}/Input_WT_rep1_trim30.info      
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003915_2_Input_KO-1_1_fastxtrimf30.fastq.gz        -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003915_2_Input_KO-1_2_fastxtrimf30.fastq.gz       " > /home/fchuffar/projects/${datashare}/${gse}/Input_KO_rep1_trim30.info      
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003916_3_SSRP1-CHIP_WT-1_1_fastxtrimf30.fastq.gz   -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003916_3_SSRP1-CHIP_WT-1_2_fastxtrimf30.fastq.gz  " > /home/fchuffar/projects/${datashare}/${gse}/SSRP1_WT_rep1_trim30.info 
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003917_4_SSRP1-CHIP_KO-1_1_fastxtrimf30.fastq.gz   -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003917_4_SSRP1-CHIP_KO-1_2_fastxtrimf30.fastq.gz  " > /home/fchuffar/projects/${datashare}/${gse}/SSRP1_KO_rep1_trim30.info 
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003918_5_HIRA-CHIP_WT-1_1_fastxtrimf30.fastq.gz    -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003918_5_HIRA-CHIP_WT-1_2_fastxtrimf30.fastq.gz   " > /home/fchuffar/projects/${datashare}/${gse}/HIRA__WT_rep1_trim30.info  
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003919_6_HIRA-CHIP_KO-1_1_fastxtrimf30.fastq.gz    -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003919_6_HIRA-CHIP_KO-1_2_fastxtrimf30.fastq.gz   " > /home/fchuffar/projects/${datashare}/${gse}/HIRA__KO_rep1_trim30.info  
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003920_7_Input_WT-2_1_fastxtrimf30.fastq.gz        -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003920_7_Input_WT-2_2_fastxtrimf30.fastq.gz       " > /home/fchuffar/projects/${datashare}/${gse}/Input_WT_rep2_trim30.info      
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003921_8_Input_KO-2_1_fastxtrimf30.fastq.gz        -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003921_8_Input_KO-2_2_fastxtrimf30.fastq.gz       " > /home/fchuffar/projects/${datashare}/${gse}/Input_KO_rep2_trim30.info      
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003922_9_SSRP1-CHIP_WT-2_1_fastxtrimf30.fastq.gz   -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003922_9_SSRP1-CHIP_WT-2_2_fastxtrimf30.fastq.gz  " > /home/fchuffar/projects/${datashare}/${gse}/SSRP1_WT_rep2_trim30.info 
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003923_10_SSRP1-CHIP_KO-2_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003923_10_SSRP1-CHIP_KO-2_2_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/SSRP1_KO_rep2_trim30.info
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003924_11_HIRA-CHIP_WT-2_1_fastxtrimf30.fastq.gz   -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003924_11_HIRA-CHIP_WT-2_2_fastxtrimf30.fastq.gz  " > /home/fchuffar/projects/${datashare}/${gse}/HIRA__WT_rep2_trim30.info 
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/S003925_12_HIRA-CHIP_KO-2_1_fastxtrimf30.fastq.gz   -2 /home/fchuffar/projects/${datashare}/${gse}/raw/S003925_12_HIRA-CHIP_KO-2_2_fastxtrimf30.fastq.gz  " > /home/fchuffar/projects/${datashare}/${gse}/HIRA__KO_rep2_trim30.info 
=======

cd ~/projects/${datashare}/${gse}
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/SRR2079661_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/${datashare}/${gse}/raw/SRR207966_2_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/GSM1723635_trim30.info
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/SRR2079662_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/${datashare}/${gse}/raw/SRR2079662_2_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/GSM1723636_trim30.info
cat *.info
>>>>>>> e40209656a670e34b3a9fde1da524381f15d2482


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
