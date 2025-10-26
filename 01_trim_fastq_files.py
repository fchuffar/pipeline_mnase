import os 
exec(open("config").read())

def get_files(src_dir, src_suffix, dest_dir, dest_suffix):
  files = [f for f in os.listdir(os.path.expanduser(src_dir)) if re.match("^.*"+src_suffix+"$", f)]
  files = [x.replace(src_suffix, dest_suffix) for x in files ]
  return [os.path.join(os.path.expanduser(dest_dir), f) for f in files]

fastq_trim30_R1 = get_files("~/projects/datashare/"+gse+"/raw", "1.fastq.gz", "~/projects/datashare/"+gse+"/raw", "1_fastxtrimf30.fastq.gz")
fastq_trim30_R2 = get_files("~/projects/datashare/"+gse+"/raw", "2.fastq.gz", "~/projects/datashare/"+gse+"/raw", "2_fastxtrimf30.fastq.gz")
# fastq_trim30 = get_files("~/projects/datashare/"+gse+"/raw", ".fastq.gz", "~/projects/datashare/"+gse+"/raw", "_fastxtrimf30.fastq.gz")


localrules: target

foo=version # patch for bug in target shell
rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input:
      # fastq_trim30,
      fastq_trim30_R1,
      fastq_trim30_R2,
      # "/home/chuffarf/projects/datashare/GSE55819/raw/SRR1647907_fastxtrimf30.fastq.gz",
      # "/home/chuffarf/projects/datashare/GSE55819/raw/SRR1647908_fastxtrimf30.fastq.gz",
      # "/home/chuffarf/projects/datashare/GSE55819/raw/SRR1647909_fastxtrimf30.fastq.gz",
      # "/home/chuffarf/projects/datashare/GSE55819/raw/SRR1647910_fastxtrimf30.fastq.gz",

    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
multiqc --force -o ~/projects/"""+project+"""/results/"""+gse+"""/ . -n multiqc_trim_fastq_files \
  ~/projects/datashare/"""+gse+"""/raw/*_*_fastqc.zip \
  ~/projects/datashare/"""+gse+"""/raw/*_screen.txt \

echo workflow \"01_trim_fastq_files.py\" completed at `date`.
          """



rule trim_fastxtoolkit:
    input:
      fastqgz="{path}/raw/{prefix}.fastq.gz", 
      fastqc="{path}/raw/{prefix}_fastqc.zip",
    output: 
      fastqgz="{path}/raw/{prefix}_fastxtrimf{trim}.fastq.gz",
      # fastqc="{prefix}_fastxtrimf{trim}_fastqc.zip",
    threads: 1
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
tmpfile=$(mktemp /var/tmp/tmp_trimed_file_XXXXXXXXXX.fq.gz)
echo computing $tmpfile ...
gunzip -c  {input.fastqgz} | fastx_trimmer -l {wildcards.trim} -Q33 -z -o $tmpfile
echo move $tmpfile to output.
cp $tmpfile {output.fastqgz}
rm $tmpfile
fastqc {output.fastqgz}
fastq_screen --aligner bowtie2 --outdir {wildcards.path}/raw/ --threads {threads} {input.fastqgz}
    """

rule fastqc:
    input:  fastqgz="{path}/raw/{prefix}.fastq.gz"
    output: zip="{path}/raw/{prefix}_fastqc.zip",
            html="{path}/raw/{prefix}_fastqc.html"
    threads: 1
    shell:"""
PATH="/summer/epistorage/miniconda3/envs/mnase_env/bin:$PATH"
fastqc {input.fastqgz}
fastq_screen --aligner bowtie2 --outdir {wildcards.path}/raw/ --threads {threads} {input.fastqgz}
"""








