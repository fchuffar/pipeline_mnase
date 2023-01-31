import os 
exec(open("config").read())

localrules: target

foo=version # patch for bug in target shell
rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input:
      "/home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-165165_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-165165_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-172172_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-172172_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003634_Spz_pos_pos_8min-165166_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003634_Spz_pos_pos_8min-165166_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003634_Spz_pos_pos_8min-172173_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003634_Spz_pos_pos_8min-172173_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003635_Spz_pos_pos_12min-165167_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003635_Spz_pos_pos_12min-165167_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003635_Spz_pos_pos_12min-172174_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003635_Spz_pos_pos_12min-172174_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003636_Spz_neg_neg_4min-165168_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003636_Spz_neg_neg_4min-165168_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003636_Spz_neg_neg_4min-172175_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003636_Spz_neg_neg_4min-172175_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003637_Spz_neg_neg_8min-165169_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003637_Spz_neg_neg_8min-165169_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003637_Spz_neg_neg_8min-172176_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003637_Spz_neg_neg_8min-172176_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003638_Spz_neg_neg_12min-165170_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003638_Spz_neg_neg_12min-165170_R2_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003638_Spz_neg_neg_12min-172177_R1_001_fastxtrimf30.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003638_Spz_neg_neg_12min-172177_R2_001_fastxtrimf30.fastq.gz", 

      "/home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-165165_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-165165_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-172172_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003633_Spz_pos_pos_4min-172172_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003634_Spz_pos_pos_8min-165166_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003634_Spz_pos_pos_8min-165166_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003634_Spz_pos_pos_8min-172173_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003634_Spz_pos_pos_8min-172173_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003635_Spz_pos_pos_12min-165167_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003635_Spz_pos_pos_12min-165167_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003635_Spz_pos_pos_12min-172174_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003635_Spz_pos_pos_12min-172174_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003636_Spz_neg_neg_4min-165168_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003636_Spz_neg_neg_4min-165168_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003636_Spz_neg_neg_4min-172175_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003636_Spz_neg_neg_4min-172175_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003637_Spz_neg_neg_8min-165169_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003637_Spz_neg_neg_8min-165169_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003637_Spz_neg_neg_8min-172176_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003637_Spz_neg_neg_8min-172176_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003638_Spz_neg_neg_12min-165170_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003638_Spz_neg_neg_12min-165170_R2_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003638_Spz_neg_neg_12min-172177_R1_001_fastxtrimf60.fastq.gz", 
      "/home/chuffarf/projects/datashare/mmspz/raw/S003638_Spz_neg_neg_12min-172177_R2_001_fastxtrimf60.fastq.gz", 


    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
multiqc --force -o . -n multiqc_notrim \
  ~/projects/datashare/"""+gse+"""/raw/*_*_fastqc.zip

echo workflow \"01_trim_fastq_files.py\" completed at `date`.
          """



rule trim_fastxtoolkit:
    input:
      fastq="{prefix}.fastq.gz", 
      fastqc="{prefix}_fastqc.zip",
    output: 
      fastq="{prefix}_fastxtrimf{trim}.fastq.gz",
      fastqc="{prefix}_fastxtrimf{trim}_fastqc.zip",
    threads: 1
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
tmpfile=$(mktemp /var/tmp/tmp_trimed_file_XXXXXXXXXX.fq.gz)
echo computing $tmpfile ...
gunzip -c  {input.fastq} | fastx_trimmer -l {wildcards.trim} -Q33 -z -o $tmpfile
echo move $tmpfile to output.
cp $tmpfile {output.fastq}
rm $tmpfile
fastqc {output.fastq}
    """

rule fastqc:
    input:  fastqgz="{prefix}.fastq.gz"
    output: zip="{prefix}_fastqc.zip",
            html="{prefix}_fastqc.html"
    threads: 1
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
fastqc {input.fastqgz}
"""








