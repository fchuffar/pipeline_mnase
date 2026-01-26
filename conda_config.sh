source ~/conda_config.sh
# conda create -n mnase_env
conda activate mnase_env
mamba install -c anaconda -c bioconda -c conda-forge -c r r-base libopenblas bioconductor-geoquery bioconductor-affy bioconductor-biobase r-seqinr r-rcpparmadillo r-devtools r-fastmap r-matrix r-kernsmooth r-catools r-gtools r-nortest r-survival r-beanplot r-gplots r-dbi snakemake=7.32.4 macs3 subread bioconductor-deseq2 bioconductor-annotatr bioconductor-vplotr
# devtools::install_github("fchuffar/epimedtools")
# devtools::install_github("fchuffar/deeptoolsr")
# mamba install -c anaconda -c bioconda -c conda-forge -c r r-fork
# devtools::install_github("fchuffar/bot")


# # conda deactivate
# # rm -Rf /summer/epistorage/miniconda3/*
# # ~/Miniconda3-latest-Linux-x86_64.sh -u -p /summer/epistorage/miniconda3 -b
# # conda update -n base -c defaults conda
#
# __conda_setup="$('/summer/epistorage/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
# if [ $? -eq 0 ]; then
#    eval "$__conda_setup"
# else
#    if [ -f "/summer/epistorage/miniconda3/etc/profile.d/conda.sh" ]; then
#        . "/summer/epistorage/miniconda3/etc/profile.d/conda.sh"
#    else
#        export PATH="/summer/epistorage/miniconda3/bin:$PATH"
#    fi
# fi
# unset __conda_setup


# conda create --name mnase_env
conda activate mnase_env


# conda install  -c bioconda snakemake fastqc samtools star deeptools
# pip install --upgrade snakemake
# conda install -c bioconda -c conda-forge multiqc
#
# conda install -c bioconda bowtie2
# conda install -c bioconda fastx_toolkit
#
# conda install -c r -c bioconda \
#   r-base=3.6.1          \
#   r-rmarkdown           \
#   r-devtools            \
#   r r-xml               \
#   bioconductor-Biobase  \
#   bioconductor-affy     \
#   bioconductor-GEOquery
#
#
# conda install -c bioconda bioconductor-deseq2
#
# install.packages("https://cran.r-project.org/src/contrib/Archive/locfit/locfit_1.5-9.tar.gz")
#
#
# # # https://github.com/fchuffar/epimedtools
# # Sys.setenv(TAR = "/bin/tar") ; devtools::install_github("fchuffar/epimedtools")
#
  
