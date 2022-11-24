cd ~/projects/small_structs/results/hsspz
source config
echo $gse
echo $project
## push to dahu
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
# fastq bw
mkdir -p ~/projects/${datashare}/${gse}
cd ~/projects/${datashare}/${gse}
mkdir raw

ln -s ~/projects/datashare/202107033_R436_SK/fastq/S004307_1_Input_h_1.fastq.gz         raw/input_rep10_R1.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S004307_1_Input_h_2.fastq.gz         raw/input_rep10_R2.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S004308_2_ChIP_TH2B_h_1_1.fastq.gz   raw/cth2b_rep11_R1.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S004308_2_ChIP_TH2B_h_1_2.fastq.gz   raw/cth2b_rep11_R2.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S004309_3_ChIP_TH2B_h_2_1.fastq.gz   raw/cth2b_rep12_R1.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S004309_3_ChIP_TH2B_h_2_2.fastq.gz   raw/cth2b_rep12_R2.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S005158_6_hs_spz_input_1.fastq.gz    raw/input_rep20_R1.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S005158_6_hs_spz_input_2.fastq.gz    raw/input_rep20_R2.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S005159_7_hs_spz_th2brep1_1.fastq.gz raw/cth2b_rep21_R1.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S005159_7_hs_spz_th2brep1_2.fastq.gz raw/cth2b_rep21_R2.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S005160_8_hs_spz_th2brep2_1.fastq.gz raw/cth2b_rep22_R1.fastq.gz
ln -s ~/projects/datashare/202107033_R436_SK/fastq/S005160_8_hs_spz_th2brep2_2.fastq.gz raw/cth2b_rep22_R2.fastq.gz

raw/input_rep10_R1.fastq.gz
raw/cth2b_rep11_R1.fastq.gz
raw/cth2b_rep12_R1.fastq.gz
raw/input_rep20_R1.fastq.gz
raw/cth2b_rep21_R1.fastq.gz
raw/cth2b_rep22_R1.fastq.gz

## 1. qc/triming
## 2. align count
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
cd ~/projects/${project}/results/${gse}/
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 16 -pn
snakemake -s ~/projects/${project}/results/${gse}/wf.py --jobs 49 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn


### DESIGN
cd ~/projects/${datashare}/${gse}/
echo " -1 /home/fchuffar/projects/datashare/hsspz/raw/input_rep10_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/hsspz/raw/input_rep10_R2_fastxtrimf30.fastq.gz " > input_rep10_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep11_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep11_R2_fastxtrimf30.fastq.gz " > cth2b_rep11_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep12_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep12_R2_fastxtrimf30.fastq.gz " > cth2b_rep12_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/hsspz/raw/input_rep20_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/hsspz/raw/input_rep20_R2_fastxtrimf30.fastq.gz " > input_rep20_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep21_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep21_R2_fastxtrimf30.fastq.gz " > cth2b_rep21_trim30.info 
echo " -1 /home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep22_R1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/datashare/hsspz/raw/cth2b_rep22_R2_fastxtrimf30.fastq.gz " > cth2b_rep22_trim30.info 
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






/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr11:84190000-84200000"       # Acc1 Acaca 
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr11:100523000-100533000"     # Acly       
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr19:44403000-44413000"       # Scd1       
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr7:35115000-35125000"        # Cebpa      
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr5:51548000-51558000"        # Ppargc1a   
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr11:60216000-60226000"       # Srebf1     
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr6:115356000-115366000"      # Pparg      
/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 ~/projects/nme2/results/dapseq/igv_session.xml -p "chr15:85731000-85741000"       # Ppara      







/Applications/IGV_2.4.16.app/Contents/MacOS/JavaAppLauncher -Xmx750m -jar /Applications/IGV_2.4.16.app/Contents/Java/igv.jar  -g mm10 igv_session.xml -p "chr11:84190000-84200000"       # Acc1 Acaca 
