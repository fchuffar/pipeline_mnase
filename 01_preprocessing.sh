cd ~/projects/atad2/results/GSE70312
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


# GSM1723635 SRR2079661 ES_Atad2tag_AntiHA  
# GSM1723636 SRR2079662 ES wild type_antiHA 

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
sequencing_read_type=PE

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



cd ~/projects/${datashare}/${gse}
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/SRR2079661_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/${datashare}/${gse}/raw/SRR207966_2_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/GSM1723635_trim30.info
echo " -1 /home/fchuffar/projects/${datashare}/${gse}/raw/SRR2079662_1_fastxtrimf30.fastq.gz  -2 /home/fchuffar/projects/${datashare}/${gse}/raw/SRR2079662_2_fastxtrimf30.fastq.gz " > /home/fchuffar/projects/${datashare}/${gse}/GSM1723636_trim30.info
cat *.info


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

