cd  ~/projects/all_tchin/results/chip_gao_novogen/geo_submission
ssh cargo
source ~/projects/all_tchin/results/${gse}/config

GSE_TARGET_NAME="GSE7"
# Transfering files
cd /home/fchuffar/projects/${datashare}/${gse}/
ls -lha raw/*R1.fastq.gz raw/*R2.fastq.gz
cat raw/delivered/md5.summer.txt 
ls -lha *.bw
mkdir -p /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq
mkdir -p /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/bw
rsync -auvP --copy-links \
  /home/fchuffar/projects/${datashare}/${gse}/raw/*R1.fastq.gz \
  /home/fchuffar/projects/${datashare}/${gse}/raw/*R2.fastq.gz \
  /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq/.
rsync -auvP --copy-links \
  /home/fchuffar/projects/${datashare}/${gse}/*.bw \
  /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/bw

ls -lha /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/*

# MD5
cd /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq
md5sum *.fastq.gz > md5.geo.txt
cd /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/bw
md5sum *.bw > md5.geo.txt

# cat /home/fchuffar/projects/datashare_epistorage/${gse}/raw/md5_orig.txt
# cat /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq/md5.geo.txt


# Put metadata
cat /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq/md5.geo.txt
cat /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/counts/md5.geo.txt
ls -lha /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq/*1_notrim.fastq.gz
ls -lha /bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/fastq/*2_notrim.fastq.gz
cd ~/projects/${project}/results/${gse}/geo_submission
open geo_submission_metadata.xlsx
rsync -auvP geo_submission_metadata.xlsx cargo:/bettik/chuffarf/geo_submission/${gse}/${GSE_TARGET_NAME}/.

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

