cd ~/projects/nme2/results/chip_domenico_tgml
source config
ssh cargo

# cd ~/projects/nme2/results/highfatdiet/geo_submission
# wget https://www.ncbi.nlm.nih.gov/geo/info/examples/seq_template.xlsx

GSE_TARGET_NAME=GSE2full 

# Transfering files
cd /home/fchuffar/projects/${datashare}/${gse}/
ls -lha raw/*1.fastq.gz raw/*2.fastq.gz
# cat raw/md5sum.summer.txt
ls -lha *.bw
mkdir -p /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq
mkdir -p /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/bw
rsync -cauvP --copy-links \
  /home/fchuffar/projects/${datashare}/${gse}/raw/*1.fastq.gz \
  /home/fchuffar/projects/${datashare}/${gse}/raw/*2.fastq.gz \
  /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq/.
rsync -auvP --copy-links \
  /home/fchuffar/projects/${datashare}/${gse}/*.bw \
  /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/bw/.

# MD5
cd /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq
md5sum *.fastq.gz > md5.geo.txt
cat md5.geo.txt | cut -f1 -d" " | sort > tmp_md5_1.txt
cat /home/fchuffar/projects/datashare/chip_domenico_tgml/raw/fastq/md5sum.txt | cut -f1 -d" " | sort > tmp_md5_2.txt
diff tmp_md5_1.txt tmp_md5_2.txt
rm tmp_md5_*.txt
cd /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/bw
md5sum *.bw > md5.geo.txt


# Put metadata
cd ~/projects/${project}/results/${gse}/geo_submission
Rscript generate_metadata.R 

cd ~/projects/${project}/results/${gse}/geo_submission
rsync -auvP cargo:~/projects/${project}/results/${gse}/geo_submission/0*.xlsx ~/projects/${project}/results/${gse}/geo_submission/
open seq_template.xlsx

rsync -auvP seq_template.xlsx cargo:/bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/.

# Creating archive
cd /bettik/chuffarf/geo_submission/${gse}/
ls -lha ${GSE_TARGET_NAME}/*
 
tar -cvf ${GSE_TARGET_NAME}.tar ${GSE_TARGET_NAME}


# Put on GEO
ssh cargo
cd /bettik/chuffarf/geo_submission/${gse}/
lftp ftp-private.ncbi.nlm.nih.gov
# identification requiered...
put ${GSE_TARGET_NAME}.tar

