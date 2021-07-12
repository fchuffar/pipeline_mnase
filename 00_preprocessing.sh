cd ~/projects/atad2/results/chip_hira_ssrp1_spg
source config
echo $gse
echo $project
## push to dahu
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
# fastq bw
mkdir -p ~/projects/${datashare}/${gse}
cd ~/projects/${datashare}/${gse}
# ln -s ../TGML_runs/fastq/202105024_R373_SK/fastq raw
cd ~/projects/${datashare}/${gse}/raw/
ls -lha *.fastq.gz
## QC is here
echo ~/projects/${datashare}/${gse}/multiqc_notrim.html
echo ~/projects/${project}/results/${gse}/ 
echo ~/projects/${datashare}/${gse}

### FASTQ
cd ~/projects/${datashare}/${gse}/raw/
ls -lha *.fastq.gz

S004219_2_Input_KO_1_1_fastxtrimf30.fastq.gz
S004219_2_Input_KO_1_2_fastxtrimf30.fastq.gz
S004220_3_SSRP1_CHIP_WT_1_1_fastxtrimf30.fastq.gz
S004220_3_SSRP1_CHIP_WT_1_2_fastxtrimf30.fastq.gz
S004221_4_SSRP1_CHIP_KO_1_1_fastxtrimf30.fastq.gz
S004221_4_SSRP1_CHIP_KO_1_2_fastxtrimf30.fastq.gz
S004222_5_HIRA_CHIP_WT_1_1_fastxtrimf30.fastq.gz
S004222_5_HIRA_CHIP_WT_1_2_fastxtrimf30.fastq.gz
S004223_6_HIRA_CHIP_KO_1_1_fastxtrimf30.fastq.gz
S004223_6_HIRA_CHIP_KO_1_2_fastxtrimf30.fastq.gz
S004225_8_Input_KO_2_1_fastxtrimf30.fastq.gz
S004225_8_Input_KO_2_2_fastxtrimf30.fastq.gz
S004226_9_SSRP1_CHIP_WT_2_1_fastxtrimf30.fastq.gz
S004226_9_SSRP1_CHIP_WT_2_2_fastxtrimf30.fastq.gz
S004227_10_SSRP1_CHIP_KO_2_1_fastxtrimf30.fastq.gz
S004227_10_SSRP1_CHIP_KO_2_2_fastxtrimf30.fastq.gz
S004228_11_HIRA_CHIP_WT_2_1_fastxtrimf30.fastq.gz
S004228_11_HIRA_CHIP_WT_2_2_fastxtrimf30.fastq.gz
S004229_12_HIRA_CHIP_KO_2_1_fastxtrimf30.fastq.gz
S004229_12_HIRA_CHIP_KO_2_2_fastxtrimf30.fastq.gz
S004230_13_Input_WT_1_1_fastxtrimf30.fastq.gz
S004230_13_Input_WT_1_2_fastxtrimf30.fastq.gz
S004231_14_Input_WT_2_1_fastxtrimf30.fastq.gz
S004231_14_Input_WT_2_2_fastxtrimf30.fastq.gz


S004219_2_Input_KO_1_1_fastqc.zip
S004219_2_Input_KO_1_2_fastqc.zip
S004220_3_SSRP1_CHIP_WT_1_1_fastqc.zip
S004220_3_SSRP1_CHIP_WT_1_2_fastqc.zip
S004221_4_SSRP1_CHIP_KO_1_1_fastqc.zip
S004221_4_SSRP1_CHIP_KO_1_2_fastqc.zip
S004222_5_HIRA_CHIP_WT_1_1_fastqc.zip
S004222_5_HIRA_CHIP_WT_1_2_fastqc.zip
S004223_6_HIRA_CHIP_KO_1_1_fastqc.zip
S004223_6_HIRA_CHIP_KO_1_2_fastqc.zip
S004225_8_Input_KO_2_1_fastqc.zip
S004225_8_Input_KO_2_2_fastqc.zip
S004226_9_SSRP1_CHIP_WT_2_1_fastqc.zip
S004226_9_SSRP1_CHIP_WT_2_2_fastqc.zip
S004227_10_SSRP1_CHIP_KO_2_1_fastqc.zip
S004227_10_SSRP1_CHIP_KO_2_2_fastqc.zip
S004228_11_HIRA_CHIP_WT_2_1_fastqc.zip
S004228_11_HIRA_CHIP_WT_2_2_fastqc.zip
S004229_12_HIRA_CHIP_KO_2_1_fastqc.zip
S004229_12_HIRA_CHIP_KO_2_2_fastqc.zip
S004230_13_Input_WT_1_1_fastqc.zip
S004230_13_Input_WT_1_2_fastqc.zip
S004231_14_Input_WT_2_1_fastqc.zip
S004231_14_Input_WT_2_2_fastqc.zip


# check MD5

# cd projects/datashare_epistorage/
# ls
# ls  | grep hira
# cd chip_hira_ssrp1/
# ls
# cd raw
# ls
# ls -lha
# ls ..
# ls ../..
# pwd
# cd ..
# ls
# ls =lha
# ls -lha
# cd /home/chuffarf/projects/datashare_epistorage/TGML_runs/fastq/
# ls
# rsync -auvP 202105024_R373_SK@139.124.66.9:202105024_R373_SK/ ~/projects/datashare_epistorage/TGML_runs/fastq/202105024_R373_SK/
# sftp 202105024_R373_SK@139.124.66.9
# cd 202105024_R373_SK
# ls
# cd fastq/
# ls
# ls -lha
# cat md5sum.txt
# md5sum *.fastq.gz > md5sum.summer.txt
# cat md5sum.summer.txt
# cat md5sum.txt
# cat md5sum.txt | sort
# cat md5sum.txt | sort > md5.orig.sort.txt
# cat md5sum.summer.txt | sort > md5.summer.sort.txt
# diff md5.orig.sort.txt md5.summer.sort.txt
# sftp 202105024_R373_SK@139.124.66.9
# md5sum *.fastq.gz > md5sum.summer.txt
# md5sum S004220_3_SSRP1_CHIP_WT_1_2.fastq.gz
# cat md5sum.txt | grep  S004220_3_SSRP1_CHIP_WT_1_2.fastq.gz
# md5sum *.fastq.gz > md5sum.summer.txt
# cat md5sum.summer.txt | sort > md5.summer.sort.txt
# diff md5.orig.sort.txt md5.summer.sort.txt
# pwd
# exit


# cat md5.orig.sort.txt
# # # md5sum *.*data/*/*.fq.gz > md5.summer.txt &
# # # tail -f md5.summer.txt
# # cat md5.orig.txt| cut -f1 -d" " > tmp1
# # # cat md5.bettik.txt| cut -f1 -d" " > tmp2
# # cat md5.summer.txt| cut -f1 -d" " > tmp3
# # diff tmp1 tmp3


## qc align count
# put wf on dahu and launch
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
cd ~/projects/${project}/results/${gse}/
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 16 -pn
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 49 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn





### DESIGN
cd ~/projects/${datashare}/${gse}/
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004230_13_Input_WT_1_1.fastq.gz      -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004230_13_Input_WT_1_2.fastq.gz        " > Input_WT_rep1_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004219_2_Input_KO_1_1.fastq.gz       -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004219_2_Input_KO_1_2.fastq.gz         " > Input_KO_rep1_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004231_14_Input_WT_2_1.fastq.gz      -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004231_14_Input_WT_2_2.fastq.gz        " > Input_WT_rep2_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004225_8_Input_KO_2_1.fastq.gz       -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004225_8_Input_KO_2_2.fastq.gz         " > Input_KO_rep2_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004223_6_HIRA_CHIP_KO_1_1.fastq.gz   -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004223_6_HIRA_CHIP_KO_1_2.fastq.gz     " > HIRA__KO_rep1_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004229_12_HIRA_CHIP_KO_2_1.fastq.gz  -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004229_12_HIRA_CHIP_KO_2_2.fastq.gz    " > HIRA__KO_rep2_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004222_5_HIRA_CHIP_WT_1_1.fastq.gz   -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004222_5_HIRA_CHIP_WT_1_2.fastq.gz     " > HIRA__WT_rep1_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004228_11_HIRA_CHIP_WT_2_1.fastq.gz  -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004228_11_HIRA_CHIP_WT_2_2.fastq.gz    " > HIRA__WT_rep2_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004221_4_SSRP1_CHIP_KO_1_1.fastq.gz  -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004221_4_SSRP1_CHIP_KO_1_2.fastq.gz    " > SSRP1_KO_rep1_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004227_10_SSRP1_CHIP_KO_2_1.fastq.gz -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004227_10_SSRP1_CHIP_KO_2_2.fastq.gz   " > SSRP1_KO_rep2_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004220_3_SSRP1_CHIP_WT_1_1.fastq.gz  -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004220_3_SSRP1_CHIP_WT_1_2.fastq.gz    " > SSRP1_WT_rep1_trim30.info 
echo "-1 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004226_9_SSRP1_CHIP_WT_2_1.fastq.gz  -2 /home/fchuffar/projects/datashare_epistorage/chip_hira_ssrp1_spg/raw/S004226_9_SSRP1_CHIP_WT_2_2.fastq.gz    " > SSRP1_WT_rep2_trim30.info 
ls -lha
cat *.info
pwd



HIRA__KO_rep1
HIRA__KO_rep2
HIRA__WT_rep1
HIRA__WT_rep2
Input_KO_rep1
Input_KO_rep2
Input_WT_rep1
Input_WT_rep2
SSRP1_KO_rep1
SSRP1_KO_rep2
SSRP1_WT_rep1
SSRP1_WT_rep2


## get results
mkdir -p ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/*.txt ~/projects/${datashare}/${gse}/
rsync -auvP dahu:~/projects/${datashare}/${gse}/raw/*.html ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/multiqc_notrim* ~/projects/${datashare}/${gse}/



rsync -auvP cargo:~/projects/datashare_epistorage/chip_hira_ssrp1/Input_KO_rep1_end-to-end_trim30_srt_PE_30_4_RPKM.bw ~/projects/datashare_epistorage/chip_hira_ssrp1/.
