# pipeline_mnase
A set of scripts that orchestrate the analysis of MNase-Seq and ChIP-Seq data.

## How the pipeline works

### Layout

- Code: `~/projects/${project}/results/${gse}/` (this repository).
- Data: `~/projects/datashare/${gse}/`, with the FASTQ files in `raw/` and the `.info` files, BAM, bigWig and logs at its root.
- Data paths are absolute (`/home/chuffarf/...`), so they are the same locally and on the computing cluster.

### Parameters: `config`

- `config` is copied from one of the `config.XXX` files and sets `gse`, `project`, `species`, `annotation`, `version` and `sr_or_pe`.
- Its syntax is valid in bash (`source config`), Python (`exec(open("config").read())`) and R (`source("config")`), so the three languages share the same parameters.

### Design: `samples.R` and `.info` files

- `samples.R` defines `samples = c(...)`. The Snakemake workflows read it too, through the `def c(*args)` trick.
- One `{sample}_trim{trim}.info` file per sample, in `datashare/${gse}/`, holds the bowtie2 input arguments (`-1 ... -2 ...` or `-U ...`). It is the link between a sample and its FASTQ files.

### The `00_preprocessing.sh` concept

`00_preprocessing.sh` is **not a script to run**: it is an executable logbook, meant
to be copy-pasted line by line into a terminal. Step 0 copies it to
`00_custom_preprocessing.sh`, so that the original stays the clean template and the
copy carries the mess of an actual run. This is also why it contains lines that
change the shell itself (`cd`, `source config`, `conda activate`, `ssh dahu`):
they would be meaningless in a `bash 00_preprocessing.sh`.

It is **generic, and the dataset is a parameter**. Two variables carry everything,
`project` and `gse`; they are set in the file *and* in `config` ("the only double
copy"), and everything else is written `${project}` / `${gse}`. A typo in one of
them is not cosmetic: the variable expands to the empty string and the `rsync`
commands silently target the wrong place.

**Paths in the procedure are relative, by design.** The `cd` of step 1 moves once
and for all into the repository directory, the `datashare` symlink sits there, and
everything is then written `datashare/${gse}/...`. Hence no step may `cd` elsewhere
in the middle: the symlink lives in the repository, not in its target, so a
relative path stops resolving as soon as one leaves. (Paths *inside* the `.info`
files are a different matter: they are absolute, so that bowtie2 finds its FASTQ
files identically on both machines.)

**Two machines alternate**, and the `rsync` commands mark the boundaries: local for
downloading, building the design and getting the results back; cluster for QC,
trimming and alignment, with `cargo` as the transfer node and `dahu` for computing.
This is what gives the step order: 2 and 3 local, 4 pushes, 5 and 6 on the cluster,
7 brings back, 8 analyses locally.

**Dataset-specific parts are shadowed by a commented generic version.** `samples.R`
is hand-written for the dataset, with the generic `echo | sed` one-liner just below;
the runs table is a dataset file, with `sratab2tsv.sh` commented out for any
GEO/SRA dataset. The file therefore holds, at the same time, the record of this run
and the template for the next one.

**Steps are checked as they go.** Almost every block ends with a count and the
expected value as a comment (`ls ... | wc -l   # 48 expected`). One advances by
verifying, which is what the copy-paste usage calls for.

### Steps

What each step actually does. The numbering below is the historical one of this
README; `00_preprocessing.sh` now numbers its own blocks 0 to 8.

1. Choose the config (`cp config.XXX config`), then push the code to the cluster (`rsync` to `cargo`).
2. Put the raw FASTQ files in `datashare/${gse}/raw/` (e.g. with https://github.com/fchuffar/gse2study).
3. `01_trim_fastq_files.py` runs fastqc and multiqc. The fastx_trimmer trimming rule (`-l 30` or `-l 60`, giving `*_fastxtrimf30.fastq.gz`) is commented out in it.
4. Build the design: `samples.R` (one sample per GSM) and, in `datashare/${gse}/`, one `{gsm}_trim{trim}.info` file per sample and trimming (`trimno`: raw reads, `trim30`: reads cut to 30 bp), from a runs table linking each GSM to its SRR runs (columns `run` and `gsm`). `sratab2tsv.sh` builds this table from the NCBI `SRA_Accessions.tab` file (needs `srp` in `config`), and keeps the former version of this step (direct writing of the `.info` files and `samples.R`, run with `legacy_design=TRUE`). When a GSM has several runs, their FASTQ files are joined by commas, e.g. `-1 raw/SRR1_1.fastq.gz,raw/SRR2_1.fastq.gz -2 raw/SRR1_2.fastq.gz,raw/SRR2_2.fastq.gz` (absolute paths).
5. `02_align_fastq_files.py` runs:
   - bowtie2 (`--very-sensitive --no-mixed --no-discordant --dovetail -X 1000`);
   - `samtools sort` and `samtools index`;
   - bigWig with `bamCoverage` (RPKM, 4 bp bins, MAPQ 30, `--centerReads`);
   - multiqc.
6. Then the analysis Rmd files: `02_fraglen`, `03_metagene`, `04_vplot`/`12_vplot` (VplotR), etc. `header.Rmd` sources `common.R` and `config`, and `samples.Rmd` builds the `e` data frame (one row per sample, with its BAM and bigWig).

### Execution and results

- Run on the dahu cluster: `snakemake --jobs 50 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00" --latency-wait 60`, or on a single node with `--cores 16`.
- Get the results back with `rsync dahu:~/projects/datashare/${gse}/...` (multiqc reports, `*.txt`, `*_mmq30.bam*`).

### Known issues

- `index_bowtie` and several rules set a cluster-specific `PATH` (`/summer/epistorage/...`).
- `samtools sort -T /dev/shm` may fill `/dev/shm` with large BAM files.
- No ATAC-seq specific filtering: only a MAPQ filter (`mmq_filter_for_danpos`), no PCR duplicate removal and no chrM removal.
