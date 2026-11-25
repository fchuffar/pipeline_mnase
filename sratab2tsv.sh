# Build the table linking each sample (GSM) to its SRR runs, from the NCBI SRA_Accessions.tab file
## A way to build the runs table used at step 2 of 00_preprocessing.sh (.info files), for any GEO/SRA dataset.
## Input: ~/projects/datashare/platforms/SRA_Accessions_${srp}.tab, the lines of the SRA study ${srp} in
##   SRA_Accessions.tab (https://ftp.ncbi.nlm.nih.gov/sra/reports/Metadata/SRA_Accessions.tab), e.g.:
##   cd ~/projects/datashare/platforms/
##   wget https://ftp.ncbi.nlm.nih.gov/sra/reports/Metadata/SRA_Accessions.tab
##   grep ${srp} SRA_Accessions.tab > SRA_Accessions_${srp}.tab
## column 1: accession (SRR...), column 10: alias (GSM..._r1...)
## Output: ~/projects/datashare/${gse}/raw/${gse}_runs.tsv, tab-separated, columns run and gsm (one row per run)
## Needs gse, project and srp in config.
cd ~/projects/${project}/results/${gse}/
source config
echo $gse $project $srp
mkdir -p ~/projects/datashare/${gse}/raw
runs_tsv=~/projects/datashare/${gse}/raw/${gse}_runs.tsv
echo -e "run\tgsm" > ${runs_tsv}
cat ~/projects/datashare/platforms/SRA_Accessions_${srp}.tab | grep RUN | grep ${srp} | cut -f1,10 | grep ^SRR | sed 's/_[^\t]*$//' | sort -k2,2 -k1,1 >> ${runs_tsv}
cat ${runs_tsv}



# Former version of step 4 of 00_preprocessing.sh (design), kept as it was before the refactoring of the pipeline
## for GSE292230 (step 2 now builds the .info files from a runs table, see above).
## It writes the {gsm}_trim30.info files and samples.R directly from SRA_Accessions_${srp}.tab;
## run only if legacy_design=TRUE (e.g. legacy_design=TRUE bash sratab2tsv.sh), as it overwrites samples.R.
## Known issue: when a GSM has several SRR runs, the sed loop builds wrong paths (_1.fastq.gz,raw/ separator).
if [[ ${legacy_design:-FALSE} == TRUE ]]; then
## SR or PE?
ls -lha ~/projects/datashare/${gse}/raw/
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
echo "samples = c("         >  samples.R                                                                    
for gsm in $gsms                                                        
do                                                        
  echo "  '${gsm}',     "   >> samples.R                                                                
done                                                        
echo ")           "         >> samples.R                                                         
cat samples.R                                                        
# or previouly done in design.sh and then:
# cp samples.template.R samples.R 
fi
