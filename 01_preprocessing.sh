cd ~/projects/all_tchin/results/GSE101597
source config
echo $gse
echo $project
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
## data description
echo https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=${gse}
# GSM2706541  Input_R1
# GSM2706542  H3K9ac_R1
# GSM2706543  H3K14pr_R1
# GSM2706544  H3K14bu_R1
# GSM2706545  Input_R2
# GSM2706546  H3K9ac_R2
# GSM2706547  H3K14pr_R2
# GSM2706548  H3K14bu_R2
# GSM2706549  Input_F1
# GSM2706550  H3K9ac_F1
# GSM2706551  H3K14pr_F1
# GSM2706552  H3K14bu_F1
# GSM2706553  Input_F2
# GSM2706554  H3K9ac_F2
# GSM2706555  H3K14pr_F2
# GSM2706556  H3K14bu_F2

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

echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126242_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047206_trim30.info # SRR3126242 GSM2047206 R-Input_ChIPSeq
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126243_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047207_trim30.info # SRR3126243 GSM2047207 R-H4K5ac_ChIPSeq
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126244_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047208_trim30.info # SRR3126244 GSM2047208 R-H4K5bu_ChIPSeq
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126245_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047209_trim30.info # SRR3126245 GSM2047209 R-H4K8ac_ChIPSeq
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126246_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047210_trim30.info # SRR3126246 GSM2047210 R-H4K8bu_ChIPSeq
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126247_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047211_trim30.info # SRR3126247 GSM2047211 S-Input_ChIPSeq
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126248_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047212_trim30.info # SRR3126248 GSM2047212 S-H4K5ac_ChIPSeq
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126249_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047213_trim30.info # SRR3126249 GSM2047213 S-H4K5bu_ChIPSeq
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126250_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047214_trim30.info # SRR3126250 GSM2047214 S-H4K8ac_ChIPSeq
echo " -U /home/fchuffar/projects/${datashare}/GSE101597/raw/SRR3126251_1_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/GSE101597/GSM2047215_trim30.info # SRR3126251 GSM2047215 S-H4K8bu_ChIPSeq


## qc align count
# put wf on dahu and launch
rsync -auvP ~/projects/${project}/results/${gse}/ dahu:~/projects/${project}/results/${gse}/
cd ~/projects/${project}/results/${gse}/
snakemake -s wf.py --cores 16 -pn
snakemake -s wf.py --cores 49 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 "  --latency-wait 30 -pn


## get results
mkdir -p ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/*.txt ~/projects/${datashare}/${gse}/
rsync -auvP dahu:~/projects/${datashare}/${gse}/raw/*.html ~/projects/${datashare}/${gse}/raw/
rsync -auvP dahu:~/projects/${datashare}/${gse}/raw/multiqc_notrim* ~/projects/${datashare}/${gse}/raw/

