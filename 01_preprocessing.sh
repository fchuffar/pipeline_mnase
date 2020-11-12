cd ~/projects/all_tchin/results/GSE101597
source config
echo $gse
echo $project
## design described here
echo https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=${gse}
## bw are there
echo ~/projects/${datashare}/${gse}/.
## QC is here
echo ~/projects/${datashare}/${gse}/multiqc_notrim.html
 
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/


# SRR5838434_1.fastq.gz GSM2706541  Input_R1
# SRR5838435_1.fastq.gz GSM2706542  H3K9ac_R1
# SRR5838436_1.fastq.gz GSM2706543  H3K14pr_R1
# SRR5838437_1.fastq.gz GSM2706544  H3K14bu_R1
# SRR5838438_1.fastq.gz GSM2706545  Input_R2
# SRR5838439_1.fastq.gz GSM2706546  H3K9ac_R2
# SRR5838440_1.fastq.gz GSM2706547  H3K14pr_R2
# SRR5838441_1.fastq.gz GSM2706548  H3K14bu_R2
# SRR5838442_1.fastq.gz GSM2706549  Input_F1
# SRR5838443_1.fastq.gz GSM2706550  H3K9ac_F1
# SRR5838444_1.fastq.gz GSM2706551  H3K14pr_F1
# SRR5838445_1.fastq.gz GSM2706552  H3K14bu_F1
# SRR5838446_1.fastq.gz GSM2706553  Input_F2
# SRR5838447_1.fastq.gz GSM2706554  H3K9ac_F2
# SRR5838448_1.fastq.gz GSM2706555  H3K14pr_F2
# SRR5838449_1.fastq.gz GSM2706556  H3K14bu_F2

## download fastq files
# wget https://ftp.ncbi.nlm.nih.gov/sra/reports/Metadata/SRA_Accessions.tab
sra=`cat ~/projects/${datashare}/platforms/SRA_Accessions.tab | grep ${gse} | cut -f1 | grep SRA`
echo $sra
srrs=`cat ~/projects/${datashare}/platforms/SRA_Accessions.tab | grep RUN | grep ${sra}| cut -f1 | grep SRR`
echo $srrs
echo $srrs | wc

mkdir -p ~/projects/${datashare}/${gse}/raw
cd ~/projects/${datashare}/${gse}/raw

echo "checking" $srrs >> checking_srrs_report.txt
for srr in $srrs
do
  FILE=${srr}_1.fastq.gz
  if [ -f $FILE ]; then
     echo "File $FILE exists."
  else
     echo "File $FILE does not exist."
     prefetch $srr
     vdb-validate $srr
     status=$?
     ## take some decision ##
     [ $status -ne 0 ] && echo "$srr check failed" || echo "$srr ok" >> checking_srrs_report.txt
     parallel-fastq-dump --threads 16 --tmpdir /dev/shm --gzip --split-files --outdir ./ --sra-id ${srr}
  fi
done

# SR or PE?
ls -lha ~/projects/${datashare}/${gse}/raw
sequencing_read_type=SR

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
cat *.info



echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838434_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706541_trim30.info # SRR5838434 GSM2706541 Input_R1
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838435_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706542_trim30.info # SRR5838435 GSM2706542 H3K9ac_R1
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838436_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706543_trim30.info # SRR5838436 GSM2706543 H3K14pr_R1
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838437_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706544_trim30.info # SRR5838437 GSM2706544 H3K14bu_R1
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838438_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706545_trim30.info # SRR5838438 GSM2706545 Input_R2
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838439_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706546_trim30.info # SRR5838439 GSM2706546 H3K9ac_R2
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838440_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706547_trim30.info # SRR5838440 GSM2706547 H3K14pr_R2
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838441_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706548_trim30.info # SRR5838441 GSM2706548 H3K14bu_R2
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838442_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706549_trim30.info # SRR5838442 GSM2706549 Input_F1
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838443_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706550_trim30.info # SRR5838443 GSM2706550 H3K9ac_F1
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838444_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706551_trim30.info # SRR5838444 GSM2706551 H3K14pr_F1
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838445_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706552_trim30.info # SRR5838445 GSM2706552 H3K14bu_F1
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838446_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706553_trim30.info # SRR5838446 GSM2706553 Input_F2
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838447_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706554_trim30.info # SRR5838447 GSM2706554 H3K9ac_F2
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838448_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706555_trim30.info # SRR5838448 GSM2706555 H3K14pr_F2
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR5838449_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2706556_trim30.info # SRR5838449 GSM2706556 H3K14bu_F2


## qc align count
# put wf on dahu and launch
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
cd ~/projects/${project}/results/${gse}/
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 16 -pn
snakemake -s ~/projects/${project}/results/${gse}/wf.py --cores 49 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 60 -pn


## get results
mkdir -p ~/projects/${datashare}/${gse}/
rsync -auvP dahu:~/projects/${datashare}/${gse}/*.txt ~/projects/${datashare}/${gse}/
rsync -auvP dahu:~/projects/${datashare}/${gse}/raw/*.html ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/multiqc_notrim* ~/projects/${datashare}/${gse}/

