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

## 1. qc/triming
## 2. align count
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

###
mkdir -p ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/raw/multiqc_notrim.html ~/projects/${datashare}/${gse}/raw/.
open ~/projects/${datashare}/${gse}/raw/multiqc_notrim.html



## QC is here
echo ~/projects/${datashare}/${gse}/raw/multiqc_notrim.html
echo ~/projects/${project}/results/${gse}/ 
echo ~/projects/${datashare}/${gse}

### FASTQ
cd ~/projects/${datashare}/${gse}/raw/
ls -lha *.fastq.gz

## get results
mkdir -p ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/*.txt ~/projects/${datashare}/${gse}/
rsync -auvP dahu:~/projects/${datashare}/${gse}/raw/*.html ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/multiqc_notrim* ~/projects/${datashare}/${gse}/
rsync -auvP dahu:~/projects/${datashare}/${gse}/*_mmq30.bam* ~/projects/${datashare}/${gse}/ --dry-run


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






/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/chip_domenico_tgml/igv_session.xml -p "chr11:84190000-84200000"       # Acc1 Acaca 
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/chip_domenico_tgml/igv_session.xml -p "chr11:100523000-100533000"     # Acly       
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/chip_domenico_tgml/igv_session.xml -p "chr19:44403000-44413000"       # Scd1       
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/chip_domenico_tgml/igv_session.xml -p "chr7:35115000-35125000"        # Cebpa      
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/chip_domenico_tgml/igv_session.xml -p "chr5:51548000-51558000"        # Ppargc1a   
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/chip_domenico_tgml/igv_session.xml -p "chr11:60216000-60226000"       # Srebf1     
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/chip_domenico_tgml/igv_session.xml -p "chr6:115356000-115366000"      # Pparg      
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/chip_domenico_tgml/igv_session.xml -p "chr15:85731000-85741000"       # Ppara      







/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 igv_session.xml -p "chr11:84190000-84200000"       # Acc1 Acaca 
