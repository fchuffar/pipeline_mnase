cd ~/projects/nme2/results/chip_domenico_tgml
source config
echo $gse
echo $project
## push to dahu
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
# fastq bw
mkdir -p ~/projects/${datashare}/${gse}
cd ~/projects/${datashare}/${gse}
# Server IP address : 139.124.66.9
# Protocol type : SFTP
# Authentication type : normal
# Username : 202111053_R397_SK
sftp 202111053_R397_SK@139.124.66.9
mv 202111053_R397_SK raw

# MD5 check 
cd ~/projects/datashare/chip_domenico_tgml/raw/fastq/
md5sum *.fastq.gz > md5sum.bettik.txt
diff md5sum.bettik.txt md5sum.txt
cat md5sum.bettik.txt | cut -f1 -d" " | sort > tmpmd5sum.bettik.txt
cat md5sum.txt        | cut -f1 -d" " | sort > tmpmd5sum.txt
diff tmpmd5sum.bettik.txt tmpmd5sum.txt
mkdir -p ~/projects/datashare_epistorage/chip_domenico_tgml
rsync -auvP ~/projects/datashare/chip_domenico_tgml/raw/ ~/projects/datashare_epistorage/chip_domenico_tgml/raw/
cd ~/projects/datashare_epistorage/chip_domenico_tgml/raw/fastq/
md5sum *.fastq.gz > md5sum.summer.txt
diff md5sum.bettik.txt md5sum.summer.txt

cd ~/projects/${datashare}/${gse}/raw/
ls -lha fastq/*.fastq.gz

ln -s fastq/S004414_1_normal_inpt_nme2wt_m301_1.fastq.gz  normal_inpt_nme2wt_m301_1.fastq.gz
ln -s fastq/S004414_1_normal_inpt_nme2wt_m301_2.fastq.gz  normal_inpt_nme2wt_m301_2.fastq.gz
ln -s fastq/S004415_2_normal_inpt_nme2wt_m302_1.fastq.gz  normal_inpt_nme2wt_m302_1.fastq.gz
ln -s fastq/S004415_2_normal_inpt_nme2wt_m302_2.fastq.gz  normal_inpt_nme2wt_m302_2.fastq.gz
ln -s fastq/S004416_3_normal_inpt_nme2ko_m291_1.fastq.gz  normal_inpt_nme2ko_m291_1.fastq.gz
ln -s fastq/S004416_3_normal_inpt_nme2ko_m291_2.fastq.gz  normal_inpt_nme2ko_m291_2.fastq.gz
ln -s fastq/S004417_4_normal_inpt_nme2ko_m293_1.fastq.gz  normal_inpt_nme2ko_m293_1.fastq.gz
ln -s fastq/S004417_4_normal_inpt_nme2ko_m293_2.fastq.gz  normal_inpt_nme2ko_m293_2.fastq.gz
ln -s fastq/S004418_5_hghfat_inpt_nme2wt_m300_1.fastq.gz  hghfat_inpt_nme2wt_m300_1.fastq.gz
ln -s fastq/S004418_5_hghfat_inpt_nme2wt_m300_2.fastq.gz  hghfat_inpt_nme2wt_m300_2.fastq.gz
ln -s fastq/S004419_6_hghfat_inpt_nme2wt_m303_1.fastq.gz  hghfat_inpt_nme2wt_m303_1.fastq.gz
ln -s fastq/S004419_6_hghfat_inpt_nme2wt_m303_2.fastq.gz  hghfat_inpt_nme2wt_m303_2.fastq.gz
ln -s fastq/S004420_7_hghfat_inpt_nme2ko_m292_1.fastq.gz  hghfat_inpt_nme2ko_m292_1.fastq.gz
ln -s fastq/S004420_7_hghfat_inpt_nme2ko_m292_2.fastq.gz  hghfat_inpt_nme2ko_m292_2.fastq.gz
ln -s fastq/S004421_8_hghfat_inpt_nme2ko_m273_1.fastq.gz  hghfat_inpt_nme2ko_m273_1.fastq.gz
ln -s fastq/S004421_8_hghfat_inpt_nme2ko_m273_2.fastq.gz  hghfat_inpt_nme2ko_m273_2.fastq.gz
ln -s fastq/S004422_9_normal_chip_nme2wt_m301_1.fastq.gz  normal_chip_nme2wt_m301_1.fastq.gz
ln -s fastq/S004422_9_normal_chip_nme2wt_m301_2.fastq.gz  normal_chip_nme2wt_m301_2.fastq.gz
ln -s fastq/S004423_10_normal_chip_nme2wt_m302_1.fastq.gz normal_chip_nme2wt_m302_1.fastq.gz
ln -s fastq/S004423_10_normal_chip_nme2wt_m302_2.fastq.gz normal_chip_nme2wt_m302_2.fastq.gz
ln -s fastq/S004424_11_normal_chip_nme2ko_m291_1.fastq.gz normal_chip_nme2ko_m291_1.fastq.gz
ln -s fastq/S004424_11_normal_chip_nme2ko_m291_2.fastq.gz normal_chip_nme2ko_m291_2.fastq.gz
ln -s fastq/S004425_12_normal_chip_nme2ko_m293_1.fastq.gz normal_chip_nme2ko_m293_1.fastq.gz
ln -s fastq/S004425_12_normal_chip_nme2ko_m293_2.fastq.gz normal_chip_nme2ko_m293_2.fastq.gz
ln -s fastq/S004426_13_hghfat_chip_nme2wt_m300_1.fastq.gz hghfat_chip_nme2wt_m300_1.fastq.gz
ln -s fastq/S004426_13_hghfat_chip_nme2wt_m300_2.fastq.gz hghfat_chip_nme2wt_m300_2.fastq.gz
ln -s fastq/S004427_14_hghfat_chip_nme2wt_m303_1.fastq.gz hghfat_chip_nme2wt_m303_1.fastq.gz
ln -s fastq/S004427_14_hghfat_chip_nme2wt_m303_2.fastq.gz hghfat_chip_nme2wt_m303_2.fastq.gz
ln -s fastq/S004428_15_hghfat_chip_nme2ko_m292_1.fastq.gz hghfat_chip_nme2ko_m292_1.fastq.gz
ln -s fastq/S004428_15_hghfat_chip_nme2ko_m292_2.fastq.gz hghfat_chip_nme2ko_m292_2.fastq.gz
ln -s fastq/S004429_16_hghfat_chip_nme2ko_m273_1.fastq.gz hghfat_chip_nme2ko_m273_1.fastq.gz
ln -s fastq/S004429_16_hghfat_chip_nme2ko_m273_2.fastq.gz hghfat_chip_nme2ko_m273_2.fastq.gz

## qc align count
# put wf on dahu and launch
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
cd ~/projects/${project}/results/${gse}/
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 16 -pn
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 49 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn


### DESIGN
cd ~/projects/${datashare}/${gse}/
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_chip_nme2ko_m273_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_chip_nme2ko_m273_2_fastxtrimf30.fastq.gz " > hghfat_chip_nme2ko_m273_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_chip_nme2ko_m292_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_chip_nme2ko_m292_2_fastxtrimf30.fastq.gz " > hghfat_chip_nme2ko_m292_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_chip_nme2wt_m300_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_chip_nme2wt_m300_2_fastxtrimf30.fastq.gz " > hghfat_chip_nme2wt_m300_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_chip_nme2wt_m303_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_chip_nme2wt_m303_2_fastxtrimf30.fastq.gz " > hghfat_chip_nme2wt_m303_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_inpt_nme2ko_m273_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_inpt_nme2ko_m273_2_fastxtrimf30.fastq.gz " > hghfat_inpt_nme2ko_m273_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_inpt_nme2ko_m292_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_inpt_nme2ko_m292_2_fastxtrimf30.fastq.gz " > hghfat_inpt_nme2ko_m292_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_inpt_nme2wt_m300_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_inpt_nme2wt_m300_2_fastxtrimf30.fastq.gz " > hghfat_inpt_nme2wt_m300_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_inpt_nme2wt_m303_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/hghfat_inpt_nme2wt_m303_2_fastxtrimf30.fastq.gz " > hghfat_inpt_nme2wt_m303_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_chip_nme2ko_m291_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_chip_nme2ko_m291_2_fastxtrimf30.fastq.gz " > normal_chip_nme2ko_m291_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_chip_nme2ko_m293_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_chip_nme2ko_m293_2_fastxtrimf30.fastq.gz " > normal_chip_nme2ko_m293_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_chip_nme2wt_m301_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_chip_nme2wt_m301_2_fastxtrimf30.fastq.gz " > normal_chip_nme2wt_m301_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_chip_nme2wt_m302_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_chip_nme2wt_m302_2_fastxtrimf30.fastq.gz " > normal_chip_nme2wt_m302_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_inpt_nme2ko_m291_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_inpt_nme2ko_m291_2_fastxtrimf30.fastq.gz " > normal_inpt_nme2ko_m291_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_inpt_nme2ko_m293_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_inpt_nme2ko_m293_2_fastxtrimf30.fastq.gz " > normal_inpt_nme2ko_m293_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_inpt_nme2wt_m301_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_inpt_nme2wt_m301_2_fastxtrimf30.fastq.gz " > normal_inpt_nme2wt_m301_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_inpt_nme2wt_m302_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/normal_inpt_nme2wt_m302_2_fastxtrimf30.fastq.gz " > normal_inpt_nme2wt_m302_trim30.info 
ls -lha
cat *.info
pwd

## qc align count
# put wf on dahu and launch
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
cd ~/projects/${project}/results/${gse}/
# snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 16 -pn
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 49 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn


## QC is here
echo ~/projects/${datashare}/${gse}/multiqc_notrim.html
echo ~/projects/${project}/results/${gse}/ 
echo ~/projects/${datashare}/${gse}

### FASTQ
cd ~/projects/${datashare}/${gse}/raw/
ls -lha *.fastq.gz

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
