# cd ~/projects/small_structs/results
# ls ~/projects/datashare_epistorage/TGML_runs/bam_epimed
# oarstat | grep fch | cut -f1 -d" " | xargs oardel
# snakemake -s wf.py --cores 8 -pn
# snakemake -s wf.py --cores 50 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 " -pn
# snakemake -s ~/projects/small_structs/results/wf.py --cores 50 --cluster "oarsub --project epimed -l nodes=1/core={threads},walltime=6:00:00 " --latency-wait 60 -pn
# cd /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/
# cp C_rn1_trimno.info C_rn2_trimno.info
# cp P_rn1_trimno.info P_rn2_trimno.info
# cp R_rn1_trimno.info R_rn2_trimno.info
# cp S_rn1_trimno.info S_rn2_trimno.info
# cp C_rn1_trimno.info C_rn3_trimno.info
# cp P_rn1_trimno.info P_rn3_trimno.info
# cp R_rn1_trimno.info R_rn3_trimno.info
# cat C_rn1_trimno.info | sed -e 's/Rep1/Rep2/g' > C_rn2_trimno.info
# cat P_rn1_trimno.info | sed -e 's/Rep1/Rep2/g' > P_rn2_trimno.info
# cat R_rn1_trimno.info | sed -e 's/Rep1/Rep2/g' > R_rn2_trimno.info
# cat S_rn1_trimno.info | sed -e 's/Rep1/Rep2/g' > S_rn2_trimno.info
# cat C_rn1_trimno.info | sed -e 's/Rep1/Rep3/g' > C_rn3_trimno.info
# cat P_rn1_trimno.info | sed -e 's/Rep1/Rep3/g' > P_rn3_trimno.info
# cat R_rn1_trimno.info | sed -e 's/Rep1/Rep3/g' > R_rn3_trimno.info

# cd /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/
# cat C_rn1_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > C_rn1_trim30.info
# cat P_rn1_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > P_rn1_trim30.info
# cat R_rn1_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > R_rn1_trim30.info
# cat S_rn1_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > S_rn1_trim30.info
# cat C_rn2_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > C_rn2_trim30.info
# cat P_rn2_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > P_rn2_trim30.info
# cat R_rn2_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > R_rn2_trim30.info
# cat S_rn2_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > S_rn2_trim30.info
# cat C_rn3_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > C_rn3_trim30.info
# cat P_rn3_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > P_rn3_trim30.info
# cat R_rn3_trimno.info | sed -e 's/\.fastq\.gz/_fastxtrimf30.fastq.gz/g' > R_rn3_trim30.info

# cd /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep1_notrim_fqgz.info P_rn1_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep2_notrim_fqgz.info P_rn2_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep3_notrim_fqgz.info P_rn3_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep1_notrim_fqgz.info R_rn1_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep2_notrim_fqgz.info R_rn2_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep3_notrim_fqgz.info R_rn3_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep1_notrim_fqgz.info C_rn1_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep2_notrim_fqgz.info C_rn2_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep3_notrim_fqgz.info C_rn3_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep1_notrim_fqgz.info S_rn1_trimno_fqgz.info
# cp /home/florent/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep2_notrim_fqgz.info S_rn2_trimno_fqgz.info


# RNA seq
# for LINE in P R C S
# do
#   for REP in 1 2 3
#   do
#     for KW in KO WT
#     do
#       echo " -1 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L1_R1_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L2_R1_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L3_R1_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L4_R1_fastxtrimf30.fastq.gz -2 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L1_R2_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L2_R2_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L3_R2_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L4_R2_fastxtrimf30.fastq.gz" >  /Users/florent/projects/datashare_epistorage/TGML_runs/bam_epimed/${LINE}_${KW}${REP}_trim30.info
#     done
#   done
# done
#
#
# mate /Users/florent/projects/datashare_epistorage/TGML_runs/bam_epimed/*_KO*_trim30.info
# mate /Users/florent/projects/datashare_epistorage/TGML_runs/bam_epimed/*_WT*_trim30.info
#
#
# rsync -auvP ~/projects/datashare_epistorage/TGML_runs/bam_epimed/*_KO*_trim30.info luke:~/projects/datashare_epistorage/TGML_runs/bam_epimed/
# rsync -auvP ~/projects/datashare_epistorage/TGML_runs/bam_epimed/*_WT*_trim30.info luke:~/projects/datashare_epistorage/TGML_runs/bam_epimed/
#
# rsync -auvP --exclude="*.bed" --exclude="*.saf" --exclude="tmp" ~/projects/small_structs/results/wf.py luke:~/projects/small_structs/results/
#
#
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO1_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO2_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO3_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO1_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO2_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO3_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO1_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO2_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO3_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO1_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO2_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO3_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT1_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT2_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT3_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT1_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT2_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT3_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT1_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT2_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT3_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT1_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT2_end-to-end_trim30.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT3_end-to-end_trim30.log"
#
#
# snakemake -s wf.py --cores 8 -pn







# RNA seq
# for LINE in P R C S
# do
#   for REP in 1 2 3
#   do
#     for KW in KO WT
#     do
#       printf " -1 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L1_R1.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L2_R1.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L3_R1.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L4_R1.fastq.gz -2 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L1_R2.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L2_R2.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L3_R2.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-${LINE}-H2AL2-${KW}-Rep${REP}/L4_R2.fastq.gz" >  /Users/florent/projects/datashare_epistorage/TGML_runs/bam_epimed/${LINE}_${KW}${REP}_trimno.info
#     done
#   done
# done
#
# mate /Users/florent/projects/datashare_epistorage/TGML_runs/bam_epimed/*_KO*_trimno.info
# mate /Users/florent/projects/datashare_epistorage/TGML_runs/bam_epimed/*_WT*_trimno.info
#
#
# rsync -auvP ~/projects/datashare_epistorage/TGML_runs/bam_epimed/*_KO*_trimno.info luke:~/projects/datashare_epistorage/TGML_runs/bam_epimed/
# rsync -auvP ~/projects/datashare_epistorage/TGML_runs/bam_epimed/*_WT*_trimno.info luke:~/projects/datashare_epistorage/TGML_runs/bam_epimed/
# rsync -auvP --exclude="*.bed" --exclude="*.saf" --exclude="tmp" ~/projects/small_structs/results/wf.py luke:~/projects/small_structs/results/
#
#
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO1_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO2_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO3_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO1_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO2_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO3_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO1_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO2_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO3_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO1_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO2_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO3_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT1_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT2_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT3_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT1_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT2_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT3_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT1_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT2_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT3_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT1_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT2_end-to-end_trimno.log"
# rm  "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT3_end-to-end_trimno.log"
#
# cd ~/projects/small_structs/results
# snakemake -s wf.py --cores 8 -pn


# MNase spermatozoide H2AL2 WT/KO no size selection
"""
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003633_Spz_pos_pos_4min-165165_R1_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003633_Spz_pos_pos_4min-165165_R2_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003634_Spz_pos_pos_8min-165166_R1_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003634_Spz_pos_pos_8min-165166_R2_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003635_Spz_pos_pos_12min-165167_R1_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003635_Spz_pos_pos_12min-165167_R2_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003636_Spz_neg_neg_4min-165168_R1_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003636_Spz_neg_neg_4min-165168_R2_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003637_Spz_neg_neg_8min-165169_R1_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003637_Spz_neg_neg_8min-165169_R2_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003638_Spz_neg_neg_12min-165170_R1_001_fastxtrimf30.fastq.gz",
"/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003638_Spz_neg_neg_12min-165170_R2_001_fastxtrimf30.fastq.gz",

# ls -lha ~/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/
# ls -lha ~/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/
printf " -1 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003633_Spz_pos_pos_4min-165165_R1_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003633_Spz_pos_pos_4min-172172_R1_001_fastxtrimf30.fastq.gz   -2 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003633_Spz_pos_pos_4min-165165_R2_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003633_Spz_pos_pos_4min-172172_R2_001_fastxtrimf30.fastq.gz   " > ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_trim30.info    
printf " -1 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003634_Spz_pos_pos_8min-165166_R1_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003634_Spz_pos_pos_8min-172173_R1_001_fastxtrimf30.fastq.gz   -2 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003634_Spz_pos_pos_8min-165166_R2_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003634_Spz_pos_pos_8min-172173_R2_001_fastxtrimf30.fastq.gz   " > ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp4_trim30.info    
printf " -1 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003635_Spz_pos_pos_12min-165167_R1_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003635_Spz_pos_pos_12min-172174_R1_001_fastxtrimf30.fastq.gz -2 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003635_Spz_pos_pos_12min-165167_R2_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003635_Spz_pos_pos_12min-172174_R2_001_fastxtrimf30.fastq.gz " > ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp6_trim30.info    
printf " -1 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003636_Spz_neg_neg_4min-165168_R1_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003636_Spz_neg_neg_4min-172175_R1_001_fastxtrimf30.fastq.gz   -2 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003636_Spz_neg_neg_4min-165168_R2_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003636_Spz_neg_neg_4min-172175_R2_001_fastxtrimf30.fastq.gz   " > ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn2_trim30.info    
printf " -1 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003637_Spz_neg_neg_8min-165169_R1_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003637_Spz_neg_neg_8min-172176_R1_001_fastxtrimf30.fastq.gz   -2 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003637_Spz_neg_neg_8min-165169_R2_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003637_Spz_neg_neg_8min-172176_R2_001_fastxtrimf30.fastq.gz   " > ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn4_trim30.info    
printf " -1 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003638_Spz_neg_neg_12min-165170_R1_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003638_Spz_neg_neg_12min-172177_R1_001_fastxtrimf30.fastq.gz -2 /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003638_Spz_neg_neg_12min-165170_R2_001_fastxtrimf30.fastq.gz,/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003638_Spz_neg_neg_12min-172177_R2_001_fastxtrimf30.fastq.gz " > ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn6_trim30.info    
"""




def get_files(src_dir, src_suffix, dest_dir, dest_suffix):
  files = [f for f in os.listdir(src_dir) if re.match("^.*"+src_suffix+"$", f)]
  files = [x.replace(src_suffix, dest_suffix) for x in files ]
  return [os.path.join(dest_dir, f) for f in files]


localrules: target

rule target:
    threads: 1
    message: "-- Rule target completed. --"
    input: 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_local_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_end-to-end_trimno.log",

      # # GSE45915 th2b tag
      # "/home/fchuffar~/projects/datashare/GSE45915/solid/GSM1119609_solid.bam",
      # "/home/fchuffar~/projects/datashare/GSE45915/solid/GSM1119610_solid.bam",
      # "/home/fchuffar~/projects/datashare/GSE45915/solid/GSM1119611_solid.bam",
      # "/home/fchuffar~/projects/datashare/GSE45915/solid/GSM1119612_solid.bam",
      # "/home/fchuffar~/projects/datashare/GSE45915/solid/GSM1179189_solid.bam",
      # "/home/fchuffar~/projects/datashare/GSE45915/solid/GSM1179190_solid.bam",

      # nut ko wt kbu
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/nutko_kbu_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/nutwt_kbu_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/nutko_inp_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/nutwt_inp_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/nutko_kbu_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/nutwt_kbu_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/nutko_inp_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/nutwt_inp_end-to-end_trim30_srt_30_4_RPKM.bw",


      # Sperm ChIP H2AL2 et H3
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H2A_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H31_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H32_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H2A_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H31_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H32_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H2A_end-to-end_trim30_fsmin025_fsmax075_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H31_end-to-end_trim30_fsmin025_fsmax075_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H32_end-to-end_trim30_fsmin025_fsmax075_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H2A_end-to-end_trim30_fsmin125_fsmax175_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H31_end-to-end_trim30_fsmin125_fsmax175_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H32_end-to-end_trim30_fsmin125_fsmax175_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H2A_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H31_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H32_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H2A_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H31_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_H32_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",










      # GSE77277 R P H4K5ac H4K5bu H4K8ac H4K8bu input
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047212_end-to-end_trim30.log", # S-H4K5ac_ChIPSeq (pachyten)
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047213_end-to-end_trim30.log", # S-H4K5bu_ChIPSeq (pachyten)
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047214_end-to-end_trim30.log", # S-H4K8ac_ChIPSeq (pachyten)
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047215_end-to-end_trim30.log", # S-H4K8bu_ChIPSeq (pachyten)
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047207_end-to-end_trim30.log", # R-H4K5ac_ChIPSeq
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047208_end-to-end_trim30.log", # R-H4K5bu_ChIPSeq
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047209_end-to-end_trim30.log", # R-H4K8ac_ChIPSeq
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047210_end-to-end_trim30.log", # R-H4K8bu_ChIPSeq
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047212_end-to-end_trim30_srtsr_30_4_RPKM.bw", # S-H4K5ac_ChIPSeq (pachyten)
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047213_end-to-end_trim30_srtsr_30_4_RPKM.bw", # S-H4K5bu_ChIPSeq (pachyten)
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047214_end-to-end_trim30_srtsr_30_4_RPKM.bw", # S-H4K8ac_ChIPSeq (pachyten)
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047215_end-to-end_trim30_srtsr_30_4_RPKM.bw", # S-H4K8bu_ChIPSeq (pachyten)
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047207_end-to-end_trim30_srtsr_30_4_RPKM.bw", # R-H4K5ac_ChIPSeq
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047208_end-to-end_trim30_srtsr_30_4_RPKM.bw", # R-H4K5bu_ChIPSeq
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047209_end-to-end_trim30_srtsr_30_4_RPKM.bw", # R-H4K8ac_ChIPSeq
      "/home/fchuffar/projects/datashare/GSE77277/GSM2047210_end-to-end_trim30_srtsr_30_4_RPKM.bw", # R-H4K8bu_ChIPSeq









      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp4_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp6_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn4_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn6_end-to-end_trim30.log",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp4_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp6_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn2_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn4_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn6_end-to-end_trim30_srt_30_4_RPKM.bw",


      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_end-to-end_trim30_fsmin025_fsmax075_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp4_end-to-end_trim30_fsmin025_fsmax075_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp6_end-to-end_trim30_fsmin025_fsmax075_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn2_end-to-end_trim30_fsmin025_fsmax075_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn4_end-to-end_trim30_fsmin025_fsmax075_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn6_end-to-end_trim30_fsmin025_fsmax075_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_end-to-end_trim30_fsmin125_fsmax175_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp4_end-to-end_trim30_fsmin125_fsmax175_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp6_end-to-end_trim30_fsmin125_fsmax175_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn2_end-to-end_trim30_fsmin125_fsmax175_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn4_end-to-end_trim30_fsmin125_fsmax175_srt.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn6_end-to-end_trim30_fsmin125_fsmax175_srt.bam",


      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp4_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp6_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn2_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn4_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn6_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp4_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp6_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn2_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn4_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn6_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_in1_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_in2_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_th1_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_th2_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_in1_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_in2_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_th1_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_th2_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",



      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t1p_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t1p_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t1p_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t2p_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t2p_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t2p_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_Spe_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_Spe_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_Spe_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES2_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES2_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES2_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES1_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES1_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES1_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM.bw",




      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO3_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO3_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO3_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO1_end-to-end_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO2_end-to-end_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO3_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT3_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT3_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT3_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT2_end-to-end_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT3_end-to-end_trim30.log",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO1_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO2_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_KO3_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO1_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO2_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_KO3_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO1_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO2_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_KO3_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO1_end-to-end_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO2_end-to-end_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_KO3_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT1_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT2_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_WT3_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT1_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT2_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_WT3_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT1_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT2_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_WT3_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT1_end-to-end_trimno.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT2_end-to-end_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_WT3_end-to-end_trimno.log",



      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t11_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t12_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t13_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t21_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t22_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t23_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn3_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn3_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn3_end-to-end_trim30.log",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t11_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t12_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t13_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t21_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t22_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/N_t23_end-to-end_trim30_srt_30_4_RPKM.bw",




      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn1_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn1_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn1_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn1_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn2_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn2_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn2_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn2_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn3_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn3_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn3_end-to-end_trim30_srt_30_4_RPKM.bw",




      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_Spe_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES1_end-to-end_trim30.log",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_Spe_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES2_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/Q_ES1_end-to-end_trim30_srt_30_4_RPKM.bw",



      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_1U1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_2U1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_4U1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_6U1_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_1U2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_2U2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_4U2_end-to-end_trim30.log",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_6U2_end-to-end_trim30.log",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_1U1_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_2U1_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_4U1_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_6U1_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_1U2_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_2U2_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_4U2_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/E_6U2_end-to-end_trim30_srt_30_4_RPKM.bw",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nu3_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sm3_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_n08_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_n18_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_s08_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_s18_end-to-end_trim30_srt_30_4_RPKM.bw",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_in1_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_in2_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_th1_end-to-end_trim30_srt_30_4_RPKM.bw",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_th2_end-to-end_trim30_srt_30_4_RPKM.bw",

      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn1_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn1_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn1_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn1_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn2_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn2_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn2_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn2_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn3_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn3_local_trimno.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn3_local_trimno.log",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn1_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn1_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn1_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn1_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn2_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn2_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn2_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn2_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn3_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn3_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn3_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",

      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn1_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn1_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn1_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn1_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn2_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn2_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn2_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_rn2_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn3_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_rn3_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_rn3_local_trim30.log",

      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30.log",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30.log",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30.log",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30.log",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30.log",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30.log",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30.log",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30.log",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30.log",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_local_trim30.log",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30.log",
      #
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/F_ast_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30_srt_30_4_None.bw",
      #
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_local_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_local_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_local_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_local_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30_srt_0_1000_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30_srt_0_1000_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30_srt_0_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30_srt_0_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_local_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_local_trim30_srt_30_4_None.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30_srt_30_4_RPKM.bw",
      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30_srt_30_4_None.bw",

      # # H2ALA tag
      # [
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR823929_1_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR823930_2_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR823931_1_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR823932_2_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR823933_1_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR823934_2_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR823935_1_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR823936_2_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR924311_1_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR924311_2_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR924312_1_fastxtrimf30.fastq.gz",
      #   "/home/fchuffar/projects/datashare/GSE45915/raw/SRR924312_2_fastxtrimf30.fastq.gz"
      # ],
      
      
      
      # rnu140 run141 : GSE111931 ?? round-elongating spermatids ??
      [
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-KO/L1_R1_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-KO/L1_R2_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-KO/L2_R1_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-KO/L2_R2_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-KO/L3_R1_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-KO/L3_R2_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-KO/L4_R1_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-KO/L4_R2_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-WT/L1_R1_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-WT/L1_R2_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-WT/L2_R1_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-WT/L2_R2_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-WT/L3_R1_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-WT/L3_R2_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-WT/L4_R1_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/H4K5ac-Nut-WT/L4_R2_fastxtrimf30.fastq.gz", 
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-KO/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-KO/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-KO/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-KO/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-KO/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-KO/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-KO/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-KO/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-WT/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-WT/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-WT/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-WT/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-WT/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-WT/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-WT/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/H4K5ac-Nut-WT/L4_R2_fastxtrimf30.fastq.gz",

      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-KO/L1_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-KO/L1_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-KO/L2_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-KO/L2_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-KO/L3_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-KO/L3_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-KO/L4_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-KO/L4_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-WT/L1_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-WT/L1_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-WT/L2_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-WT/L2_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-WT/L3_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-WT/L3_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-WT/L4_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run140/Input-Nut-WT/L4_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-KO/L1_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-KO/L1_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-KO/L2_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-KO/L2_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-KO/L3_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-KO/L3_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-KO/L4_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-KO/L4_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-WT/L1_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-WT/L1_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-WT/L2_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-WT/L2_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-WT/L3_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-WT/L3_R2_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-WT/L4_R1_fastxtrimf30.fastq.gz" ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run141/Input-Nut-WT/L4_R2_fastxtrimf30.fastq.gz" ,
      ],

      
      
      [
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202009021_R321_SK/fastq/5_ChIP_H2A_L_2_1_S1_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202009021_R321_SK/fastq/5_ChIP_H2A_L_2_1_S1_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202009021_R321_SK/fastq/7_ChIP_H3_1_S2_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202009021_R321_SK/fastq/7_ChIP_H3_1_S2_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202009021_R321_SK/fastq/8_ChIP_H3_2_S3_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202009021_R321_SK/fastq/8_ChIP_H3_2_S3_R2_001_fastxtrimf30.fastq.gz",
      ],

      [
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202010021_R326_SK/fastq/S002923-5-ChIP-H2A-L-2-1_R1_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202010021_R326_SK/fastq/S002923-5-ChIP-H2A-L-2-1_R2_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202010021_R326_SK/fastq/S002925-7-ChIP-H3-1_R1_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202010021_R326_SK/fastq/S002925-7-ChIP-H3-1_R2_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202010021_R326_SK/fastq/S002926-8-ChIP-H3-2_R1_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/202010021_R326_SK/fastq/S002926-8-ChIP-H3-2_R2_fastxtrimf30.fastq.gz",
      ],
      
      [
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003633_Spz_pos_pos_4min-172172_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003633_Spz_pos_pos_4min-172172_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003634_Spz_pos_pos_8min-172173_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003634_Spz_pos_pos_8min-172173_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003635_Spz_pos_pos_12min-172174_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003635_Spz_pos_pos_12min-172174_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003636_Spz_neg_neg_4min-172175_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003636_Spz_neg_neg_4min-172175_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003637_Spz_neg_neg_8min-172176_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003637_Spz_neg_neg_8min-172176_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003638_Spz_neg_neg_12min-172177_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/S003638_Spz_neg_neg_12min-172177_R2_001_fastxtrimf30.fastq.gz"
      ],

      
      [
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003633_Spz_pos_pos_4min-165165_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003633_Spz_pos_pos_4min-165165_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003634_Spz_pos_pos_8min-165166_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003634_Spz_pos_pos_8min-165166_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003635_Spz_pos_pos_12min-165167_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003635_Spz_pos_pos_12min-165167_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003636_Spz_neg_neg_4min-165168_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003636_Spz_neg_neg_4min-165168_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003637_Spz_neg_neg_8min-165169_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003637_Spz_neg_neg_8min-165169_R2_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003638_Spz_neg_neg_12min-165170_R1_001_fastxtrimf30.fastq.gz",
        "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/S003638_Spz_neg_neg_12min-165170_R2_001_fastxtrimf30.fastq.gz"
      ],


      [ # TH2B spemato
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R283_SK/fastq/S002919_1_Input_1-149149_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R283_SK/fastq/S002919_1_Input_1-149149_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R283_SK/fastq/S002920_2_Input_2-149150_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R283_SK/fastq/S002920_2_Input_2-149150_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R283_SK/fastq/S002921_3_ChIP_TH2B_1-149151_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R283_SK/fastq/S002921_3_ChIP_TH2B_1-149151_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R283_SK/fastq/S002922_4_ChIP_TH2B_2-149152_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R283_SK/fastq/S002922_4_ChIP_TH2B_2-149152_R2_001_fastxtrimf30.fastq.gz"
      ],

      [ # C and S oct 2019
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003504_NUC_cond-146153_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003504_NUC_cond-146153_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003503_PS_cond-146152_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003503_PS_cond-146152_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003506_NUC_spz-146155_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003506_NUC_spz-146155_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003505_PS_spz-146154_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003505_PS_spz-146154_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003508_NUC_spz_1-146157_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003508_NUC_spz_1-146157_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003507_PS_spz_1-146156_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201907023_R280_SK/fastq/S003507_PS_spz_1-146156_R2_001_fastxtrimf30.fastq.gz"
      ],


      [ # C and S dec 2019
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003503_PS_cond-154154_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003503_PS_cond-154154_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003504_NUC_cond-154155_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003504_NUC_cond-154155_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003505_PS_spz-154156_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003505_PS_spz-154156_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003506_NUC_spz-154157_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003506_NUC_spz-154157_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003507_PS_spz_1-154158_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003507_PS_spz_1-154158_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003508_NUC_spz_1-154159_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201905013_R289_SK/fastq/S003508_NUC_spz_1-154159_R2_001_fastxtrimf30.fastq.gz"
      ],

      # [ # RANDO DNA
      # "/home/fchuffar/projects/datashare/GSE58101/raw/SRR1302810_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE58101/raw/SRR1302810_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE58101/raw/SRR1302811_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE58101/raw/SRR1302811_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE58101/raw/SRR1302812_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE58101/raw/SRR1302812_2_fastxtrimf30.fastq.gz"
      # ],
      #
      #
      # [ # NAKED DNA
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211647_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211647_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211648_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211648_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211649_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211649_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211650_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211650_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211651_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211651_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211652_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211652_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211653_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211653_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211654_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211654_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211655_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211655_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211656_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211656_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211657_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211657_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211658_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211658_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211659_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211659_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211660_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211660_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211661_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211661_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211662_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211662_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211663_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211663_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211664_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211664_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211665_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211665_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211666_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211666_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211667_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211667_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211668_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211668_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211669_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211669_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211670_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211670_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211671_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211671_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211672_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211672_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211673_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211673_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211674_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211674_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211675_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211675_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211676_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211676_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211677_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211677_2_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211678_1_fastxtrimf30.fastq.gz",
      # "/home/fchuffar/projects/datashare/GSE78984/raw/SRR3211678_2_fastxtrimf30.fastq.gz"
      # ],


      [ # triming RNAseq
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-KO-Rep1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-KO-Rep1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-KO-Rep1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-KO-Rep1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-KO-Rep1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-KO-Rep1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-WT-Rep3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-WT-Rep3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-WT-Rep3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-WT-Rep2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-P-H2AL2-KO-Rep3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-R-H2AL2-KO-Rep3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-C-H2AL2-KO-Rep3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-KO-Rep1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run176/RNA-S-H2AL2-KO-Rep1/L4_R2_fastxtrimf30.fastq.gz"],


      [
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001979_1-61061/1_S1_L001_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001979_1-61061/1_S1_L001_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001979_1-61061/1_S1_L002_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001979_1-61061/1_S1_L002_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001979_1-61061/1_S1_L003_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001979_1-61061/1_S1_L003_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001979_1-61061/1_S1_L004_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001979_1-61061/1_S1_L004_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001980_2-61062/2_S2_L001_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001980_2-61062/2_S2_L001_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001980_2-61062/2_S2_L002_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001980_2-61062/2_S2_L002_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001980_2-61062/2_S2_L003_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001980_2-61062/2_S2_L003_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001980_2-61062/2_S2_L004_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001980_2-61062/2_S2_L004_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001981_3-61063/3_S3_L001_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001981_3-61063/3_S3_L001_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001981_3-61063/3_S3_L002_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001981_3-61063/3_S3_L002_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001981_3-61063/3_S3_L003_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001981_3-61063/3_S3_L003_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001981_3-61063/3_S3_L004_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001981_3-61063/3_S3_L004_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001982_4-61064/4_S4_L001_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001982_4-61064/4_S4_L001_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001982_4-61064/4_S4_L002_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001982_4-61064/4_S4_L002_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001982_4-61064/4_S4_L003_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001982_4-61064/4_S4_L003_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001982_4-61064/4_S4_L004_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001982_4-61064/4_S4_L004_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001983_5-61065/5_S5_L001_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001983_5-61065/5_S5_L001_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001983_5-61065/5_S5_L002_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001983_5-61065/5_S5_L002_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001983_5-61065/5_S5_L003_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001983_5-61065/5_S5_L003_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001983_5-61065/5_S5_L004_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001983_5-61065/5_S5_L004_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001984_6-61066/6_S6_L001_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001984_6-61066/6_S6_L001_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001984_6-61066/6_S6_L002_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001984_6-61066/6_S6_L002_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001984_6-61066/6_S6_L003_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001984_6-61066/6_S6_L003_R2_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001984_6-61066/6_S6_L004_R1_001_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run192/S001984_6-61066/6_S6_L004_R2_001_fastxtrimf30.fastq.gz",
      
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-SC-WT/L1_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-SC-WT/L2_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-SC-WT/L3_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-SC-WT/L4_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/MNS-SC-WT/L1_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/MNS-SC-WT/L2_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/MNS-SC-WT/L3_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/MNS-SC-WT/L4_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/MNS-SC-WT/L1_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/MNS-SC-WT/L2_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/MNS-SC-WT/L3_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/MNS-SC-WT/L4_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-SC-WT/L1_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-SC-WT/L2_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-SC-WT/L3_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-SC-WT/L4_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/MNS-SC-WT/L1_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/MNS-SC-WT/L2_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/MNS-SC-WT/L3_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/MNS-SC-WT/L4_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/MNS-SC-WT/L1_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/MNS-SC-WT/L2_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/MNS-SC-WT/L3_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/MNS-SC-WT/L4_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/PSK-SC-WT/L1_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/PSK-SC-WT/L2_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/PSK-SC-WT/L3_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/PSK-SC-WT/L4_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/PSK-SC-WT/L1_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/PSK-SC-WT/L2_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/PSK-SC-WT/L3_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/PSK-SC-WT/L4_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/PSK-SC-WT/L1_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/PSK-SC-WT/L2_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/PSK-SC-WT/L3_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/PSK-SC-WT/L4_R1_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/PSK-SC-WT/L1_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/PSK-SC-WT/L2_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/PSK-SC-WT/L3_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/PSK-SC-WT/L4_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/PSK-SC-WT/L1_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/PSK-SC-WT/L2_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/PSK-SC-WT/L3_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run125/PSK-SC-WT/L4_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/PSK-SC-WT/L1_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/PSK-SC-WT/L2_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/PSK-SC-WT/L3_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run126/PSK-SC-WT/L4_R2_fastxtrimf30.fastq.gz"         ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-P-WT/L1_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-P-WT/L2_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-P-WT/L3_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-P-WT/L4_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-P-WT/L1_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-P-WT/L2_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-P-WT/L3_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-P-WT/L4_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-P-WT/L1_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-P-WT/L2_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-P-WT/L3_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-P-WT/L4_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-P-WT/L1_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-P-WT/L2_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-P-WT/L3_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-P-WT/L4_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-P-WT/L1_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-P-WT/L2_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-P-WT/L3_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-P-WT/L4_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-P-WT/L1_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-P-WT/L2_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-P-WT/L3_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-P-WT/L4_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-R-WT/L1_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-R-WT/L2_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-R-WT/L3_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-R-WT/L4_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-R-WT/L1_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-R-WT/L2_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-R-WT/L3_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-R-WT/L4_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-R-WT/L1_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-R-WT/L2_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-R-WT/L3_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-R-WT/L4_R1_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-R-WT/L1_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-R-WT/L2_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-R-WT/L3_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run113/MNS-R-WT/L4_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-R-WT/L1_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-R-WT/L2_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-R-WT/L3_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run119/MNS-R-WT/L4_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-R-WT/L1_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-R-WT/L2_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-R-WT/L3_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run124/MNS-R-WT/L4_R2_fastxtrimf30.fastq.gz"          ,
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band1/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band1/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band1/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band1/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band1/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band1/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band1/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band1/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band2/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band2/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band2/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band2/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band2/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band2/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band2/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band2/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band3/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band3/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band3/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band3/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band3/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band3/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band3/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band3/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band4/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band4/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band4/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band4/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band4/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band4/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band4/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band4/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band4/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band4/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band4/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band4/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band4/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band4/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band4/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band4/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band4/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band4/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band4/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band4/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band4/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band4/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band4/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band4/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band5/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band5/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band5/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band5/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band5/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band5/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band5/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band5/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band5/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band5/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band5/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band5/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band5/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band5/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band5/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band5/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band5/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band5/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band5/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band5/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band5/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band5/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band5/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band5/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band6/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band6/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band6/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band6/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band6/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band6/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band6/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band6/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band6/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band6/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band6/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band6/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band6/L1_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band6/L2_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band6/L3_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band6/L4_R1_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band6/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band6/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band6/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run163/MNase_Spm_WT_band6/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band6/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band6/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band6/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run167/MNase_Spm_WT_band6/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band6/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band6/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band6/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run184/MNase_Spm_WT_band6/L4_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band6/L1_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band6/L2_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band6/L3_R2_fastxtrimf30.fastq.gz",
      "/home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/run187/MNase_Spm_WT_band6/L4_R2_fastxtrimf30.fastq.gz"],
      
      "/home/fchuffar/projects/datashare/GSE39908/GSM984197_solid_srt_0_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/GSE39908/GSM984198_solid_srt_0_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/GSE39908/GSM984199_solid_srt_0_0_4_RPKM.bw",
      "/home/fchuffar/projects/datashare/GSE39908/GSM984200_solid_srt_0_0_4_RPKM.bw",

      "/home/fchuffar/projects/datashare/GSE45915/GSM1119609_solid_srt_0_0_4_RPKM.bw", 
      "/home/fchuffar/projects/datashare/GSE45915/GSM1119610_solid_srt_0_0_4_RPKM.bw", 
      "/home/fchuffar/projects/datashare/GSE45915/GSM1119611_solid_srt_0_0_4_RPKM.bw", 
      "/home/fchuffar/projects/datashare/GSE45915/GSM1119612_solid_srt_0_0_4_RPKM.bw", 
      "/home/fchuffar/projects/datashare/GSE45915/GSM1179189_solid_srt_0_0_4_RPKM.bw", 
      "/home/fchuffar/projects/datashare/GSE45915/GSM1179190_solid_srt_0_0_4_RPKM.bw", 
      
    shell:"""
echo workflow \"gsat_mm\" completed at `date` 

multiqc --force -o ~/projects/small_structs/results/ -n multiqc_h2al2_wtko_in_s \
  ~/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/*_fastqc.zip \
  ~/projects/datashare_epistorage/TGML_runs/fastq/201911039_R308_SK/fastq/*_fastqc.zip \
  ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp*_end-to-end_trim30.log \
  ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn*_end-to-end_trim30.log \
  ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp*_end-to-end_trim30.bam \
  ~/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn*_end-to-end_trim30.bam

#
# samtools view -c /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_end-to-end_trim30_fsmin125_fsmax175_srt.bam
# samtools view -c /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp4_end-to-end_trim30_fsmin125_fsmax175_srt.bam
# samtools view -c /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp6_end-to-end_trim30_fsmin125_fsmax175_srt.bam
# samtools view -c /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn2_end-to-end_trim30_fsmin125_fsmax175_srt.bam
# samtools view -c /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn4_end-to-end_trim30_fsmin125_fsmax175_srt.bam
# samtools view -c /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_nn6_end-to-end_trim30_fsmin125_fsmax175_srt.bam
#
#
# multiqc --force -o ~/projects/small_structs/results/ -n multiqc_h2al2_wtko_in_s /home/fchuffar/projects/datashare_epistorage/TGML_runs/fastq/201911039_R301_SK/fastq/*_fastqc.zip

          """


rule align_solid:
    input:
      fastq_info="{prefix}/{sample}_solid.info",
    output:
      log    = "{prefix}/{sample}_solid.log",
      bam    = "{prefix}/{sample}_solid.bam",
      srtbam = "{prefix}/{sample}_solid_srt.bam",
      bai    = "{prefix}/{sample}_solid_srt.bam.bai",
      # bw     = "{prefix}/{sample}_solid_maqerr{maqerr}_srt_0_0_4_RPKM.bw",
    threads: 32
    message:  "--- mapping with bowtie2 ---"
    shell:    """
PATH="/summer/epistorage/miniconda3/bin:$PATH"
bowtie --chunkmbs 1024 -t -p {threads} -C --sam \
  --trim3 20 \
  --fr \
  /home/fchuffar/projects/datashare/genomes/Mus_musculus/UCSC/mm10/Sequence/BowtieIndexSolid/genome -f \
  `cat {input.fastq_info}` \
  2> {output.log}   | samtools view -bS - > {output.bam}
samtools sort -@ 32 -T /dev/shm/{wildcards.sample}_solid -o {output.srtbam} {output.bam}
samtools index {output.srtbam}
    """

rule awk_filter_fragment_length:
    input:
      bam = "{prefix}/{sample}_{localendtoend}_trim{trim}_srt.bam",
    output: 
      bam = "{prefix}/{sample}_{localendtoend}_trim{trim}_fsmin{fsmin}_fsmax{fsmax}_srt.bam",
      bai = "{prefix}/{sample}_{localendtoend}_trim{trim}_fsmin{fsmin}_fsmax{fsmax}_srt.bam.bai",
    threads: 1
    shell:"""
PATH="/summer/epistorage/miniconda3/bin:$PATH"
# https://www.biostars.org/p/65262/
BAM={input.bam}
fsmin={wildcards.fsmin}
fsmax={wildcards.fsmax}
BAM_OUT={output.bam}
samtools view -h $BAM | awk '$9 < -'$fsmin' && $9 > -'$fsmax' || $9 > '$fsmin' && $9 < '$fsmax' || $1 ~ /^@/' | samtools view -bS - > $BAM_OUT
ls -lha $BAM_OUT
samtools index {output.bam}
    """
# BAM="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_end-to-end_trim30.bam"
# fsmin=025
# fsmax=075
# BAM_OUT="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_pp2_end-to-end_trim30_fsmin${fsmin}_fsmax${fsmax}.bam"
# rm $BAM_OUT

          
          
          
          
rule align_bowtie:
    input:
      # fwd="{prefix}/{sample}_R1_{trim}.fastq.gz",
      # rev="{prefix}/{sample}_R2_{trim}.fastq.gz",
      fastq_info="{prefix}/{sample}_trim{trim}.info",
      # star_index="/home/fchuffar/projects/datashare/genomes/Mus_musculus/UCSC/mm10/Sequence/Bowtie2Index/genome",
      # gtf="/scratch_r730/datashare/genomes/{species}/UCSC/{index}/Annotation/Genes/genes.gtf",
    output:
      log = "{prefix}/{sample}_{localendtoend}_trim{trim}.log",
      bam = "{prefix}/{sample}_{localendtoend}_trim{trim}.bam",
      srtbam = "{prefix}/{sample}_{localendtoend}_trim{trim}_srt.bam",
      bai = "{prefix}/{sample}_{localendtoend}_trim{trim}_srt.bam.bai"
    threads: 32
    message:  "--- mapping with bowtie2 ---"
    shell:    """
PATH="/summer/epistorage/miniconda3/bin:$PATH"
bowtie2 \
  -t \
  -p {threads} \
  --{wildcards.localendtoend} \
  --no-mixed \
  --no-discordant \
  -x  /home/fchuffar/projects/datashare/genomes/Mus_musculus/UCSC/mm10/Sequence/Bowtie2Index/genome \
  `cat {input.fastq_info}` \
  2> {output.log} \
  | samtools view -bS - > {output.bam}
  
samtools sort -@ {threads} -T /dev/shm/{wildcards.sample}_{wildcards.localendtoend}_trim{wildcards.trim} -o {output.srtbam} {output.bam}
samtools index {output.srtbam}
cat {output.log}
              """






rule count_featurecounts:
    input: "{prefix}.fastq.gz", 
      P_mns="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30.log",
      R_mns="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30.log",
      C_nuc="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30.log",
      C_sms="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30.log",
      S_bn1="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30.log",
      S_bn3="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30.log",
      S_bn6="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30.log",
      S_bn2="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30.log",
      S_bn5="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30.log",
      S_bn4="/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30.log",
    
    output: "{prefix}_fastxtrimf{trim}.count.txt"
    threads: 1
    shell:"""
/summer/epistorage/miniconda3/envs/subread_env/bin/featureCounts \
  -a nuc_feat.saf \
  -F SAF \
  --largestOverlap \
  -p -d 30 -D 200  \
  -O \
  -Q ${mmq} \
  -T 32 \
  -o ${output} \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30.bam \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30.bam \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30.bam \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30.bam \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30.bam \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30.bam \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30.bam \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30.bam \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30.bam \
  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30.bam \

    
mmq=0
# for mmq in 0 1 5 10 30
# do
  output=mixed_feat_count_${mmq}.txt
  /summer/epistorage/miniconda3/envs/subread_env/bin/featureCounts \
    -a mixed_feat.saf \
    -F SAF \
    --largestOverlap \
    -O \
    -Q ${mmq} \
    -T 32 \
    -o ${output} \
    /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_mns_end-to-end_trim30.bam \
    /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/R_mns_end-to-end_trim30.bam \
    /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_nuc_end-to-end_trim30.bam \
    /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/C_sms_end-to-end_trim30.bam \
    /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn3_end-to-end_trim30.bam \
    /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn1_end-to-end_trim30.bam \
    /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn6_end-to-end_trim30.bam \
    /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn5_end-to-end_trim30.bam \
    /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn2_end-to-end_trim30.bam \
    # /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/S_bn4_end-to-end_trim30.bam \

# done


    """

rule bed_to_fasta:
    input: os.path.expanduser("{prefix}.bed")
    output: os.path.expanduser("~/projects/heatshock/data/{subject}.blast.db")
    threads: 1
    shell:"""
bedtools  getfasta -fi /home/fchuffar/projects/datashare/genomes/Mus_musculus/UCSC/mm10/Sequence/WholeGenomeFasta/genome.fa \
  -bed ~/projects/small_structs/results/for_blastn.bed > \
  ~/projects/small_structs/results/for_blastn.fasta

/summer/epistorage/miniconda3/bin/makeblastdb -in ~/projects/small_structs/results/for_blastn.fasta \
  -dbtype nucl -parse_seqids -out  ~/projects/small_structs/results/for_blastn.blast.db

/summer/epistorage/miniconda3/bin/blastn -db ~/projects/small_structs/results/for_blastn.blast.db \
  -num_threads=1 \
  -query ~/projects/small_structs/results/for_blastn.fasta \
  -outfmt "10 std sstrand" \
  -evalue 10 -task blastn-short -word_size 8 -perc_identity 100 -qcov_hsp_perc 1  2>/dev/null | gzip  > ~/projects/small_structs/results/for_blastn.blasted.txt.gz





  
if (!exists("mgzread.table")) {
gzread.table = function(fn, ...) read.table(gzfile(fn), ...)
mgzread.table = memoise::memoise(gzread.table)
}


fn = "~/projects/small_structs/results/for_blastn.blasted.txt.gz"
print(fn)
foo = mgzread.table(fn, sep=",", stringsAsFactors=FALSE)
colnames(foo) = c("qseqid", "sseqid", "pident", "length", "mismatch", "gapopen", "qstart", "qend", "sstart", "send", "evalue", "bitscore", "sstrand")
# foo$sseqid_strand =   factor(foo$sseqid_strand, levels=paste(rep(sseqids, each=2), unique(foo$sstrand), sep="_"))
# foo$sseqid = factor(foo$sseqid, levels=sseqids)
# foo$sstrand = factor(foo$sstrand, levels=c("plus", "minus"))
# foo$sseqid_strand = interaction(foo$sseqid, foo$sstrand)

head(foo)
dim(foo)

layout(matrix(1:2, 1), respect=TRUE)
barplot(table(foo$length))
# plot(density(foo$mismatch))
# plot(density(foo$gapopen))
# plot(density(-log10(foo$evalue)))
plot(-log10(foo$evalue), foo$length)
# plot(density(foo$bitscore))
# plot(foo$bitscore, foo$length)
layout(1, respect=TRUE)
barplot(table(foo$length))
abline(v=20)

foo$key = paste0(foo$qseqid, "_", foo$sseqid)
foo = foo[order(foo$key, -foo$length),]
foo = foo[!duplicated(foo$key),]
rownames(foo) = foo$key
dim(foo)

idx = rownames(foo)[foo$length >100 & foo$length<401]
length(idx)

sort(table(foo[idx,]$qseqid))


foo[idx[foo[idx,]$qseqid=="chr5:102524331-102524732"],]





stop("EFN")

>chr5:102524331-102524732
tcctcaggtgagaattctttgttcagttctgagccccattttttaatggggttatttgattttctgaagtccaccttcttgagttctttatatatgttggatattagtcccctatctgatttaggataggtaaagatcctttcccaatctgttggtggtctttttgtcttattgacggtgtcttttgccttgcagaaactttggagtttcattaggtcccatttgtcgattctcgatcttacagcacaagcccttgctgttctgttcaggaatttttcccctgtgcccatatcttcaaggcttttccccactttctcctctataagtttcagtgtctctggttttatgtgaagttccttgatccacttagatttgaccttagtacaaggagataagtatgg
>chr2:21598331-21598732
ttcaaggcttttccccactttctcctctataagtttcagtgtctctggttttatgtgaagttccttgatccacttagatttgaccttagtacaaggagataagtatggatcgattcgcattcttctacatgataacaaccagttgtgccagcaccaattgttgaaaatgctgtctttcttccactggatggttttagctcccttgtcgaagatcaagtgaccataggtgtgtgggttcatttctgggtcttcaattctataccattggtctacttgtctgtctctataccagtaccatgcagtttttatcacaattgctctgtagtaaagctttaggtctggcatggtgattccgccagaagttcttttatccttgagaagactttttgctatcctaggtt


chr5:102524331-102524732_chr2:21598331-21598732 





chr5:102524331-102524732_chr1:159027321-159027722     100    110        0
chr5:102524331-102524732_chr1:17964631-17965032       100    123        0
chr5:102524331-102524732_chr1:65413431-65413832       100    135        0
chr5:102524331-102524732_chr1:9734561-9734962         100    131        0
chr5:102524331-102524732_chr10:125821061-125821462    100    118        0
chr5:102524331-102524732_chr10:72734101-72734502      100    116        0
chr5:102524331-102524732_chr13:50130581-50130982      100    131        0
chr5:102524331-102524732_chr14:91801551-91801952      100    129        0
chr5:102524331-102524732_chr14:95271951-95272352      100    123        0
chr5:102524331-102524732_chr15:18319031-18319432      100    112        0
chr5:102524331-102524732_chr15:65606461-65606862      100    109        0
chr5:102524331-102524732_chr16:23753461-23753862      100    119        0
chr5:102524331-102524732_chr16:3389201-3389602        100    106        0
chr5:102524331-102524732_chr16:60738051-60738452      100    124        0
chr5:102524331-102524732_chr17:57653671-57654072      100    142        0
chr5:102524331-102524732_chr18:15948581-15948982      100    119        0
chr5:102524331-102524732_chr18:55901141-55901542      100    119        0
chr5:102524331-102524732_chr2:21598331-21598732       100    108        0
chr5:102524331-102524732_chr2:53780721-53781122       100    109        0
chr5:102524331-102524732_chr2:98447951-98448352       100    120        0
chr5:102524331-102524732_chr3:6711501-6711902         100    108        0
chr5:102524331-102524732_chr3:79638841-79639242       100    103        0
chr5:102524331-102524732_chr3:91021231-91021632       100    115        0
chr5:102524331-102524732_chr4:110471111-110471512     100    109        0
chr5:102524331-102524732_chr4:111238711-111239112     100    110        0
chr5:102524331-102524732_chr4:113210601-113211002     100    110        0
chr5:102524331-102524732_chr5:62033741-62034142       100    112        0
chr5:102524331-102524732_chr6:109646191-109646592     100    127        0
chr5:102524331-102524732_chr6:16924091-16924492       100    125        0
chr5:102524331-102524732_chr6:57057881-57058282       100    117        0
chr5:102524331-102524732_chr7:87550551-87550952       100    102        0
chr5:102524331-102524732_chr8:113099311-113099712     100    135        0
chr5:102524331-102524732_chr8:77886571-77886972       100    111        0
chr5:102524331-102524732_chr9:112620521-112620922     100    135        0
chr5:102524331-102524732_chr9:11726831-11727232       100    103        0
   

keys = unique(c(foo$sseqid,foo$qseqid))
data = matrix(0, length(keys), length(keys))
rownames(data) = colnames(data) = keys
dim(data)
data[1:6, 1:6]
for (k in idx) {
  i = foo[k,]$qseqid 
  j = foo[k,]$sseqid 
  data[i, j] = foo[k,]$length
}




data[1:6, 1:6]

# data[data==401] = 0
# plot(density(log2(data + 1)))
# heatmap(plot(density(log2(data + 1)))
#
#
#
# print(i)
# layout(matrix(1:2, 1), respect=TRUE)
# matrix_file = "tmp/matrix_spectral_10000.txt.gz"
# barplot(counts[[matrix_file]][,i], main=matrix_file, las=2, ylim=c(0,50), xaxt="n")
#
# heatmap


tmp_d = log2(data + 1)
tmp_d = data==401
sum(tmp_d)
# tmp_d[1:nrow(tmp_d), 1:nrow(tmp_d)] = 0
table(apply(tmp_d, 1, sum))







# Go!
normalization=FALSE
# normalization
# colnames(data) = s$exp_grp[colnames(data),]$tissue_group_level1
if (normalization=="zscore_rows" | normalization==TRUE) {
  data = data - apply(data, 1, mean)
  data = data / apply(data, 1, sd)    
} else if (normalization=="zscore_cols") {
  data = t(data)
  data = data - apply(data, 1, mean)
  data = data / apply(data, 1, sd)    
  data = t(data)
} else if (normalization=="rank_cols") {
  data = apply(data, 2, rank)
} else if (normalization=="qqnorm_cols") {
  data = apply(data, 2, function(c) {
    qqnorm(c, plot.it=FALSE)$x
  })
}

hcmeth_cols = FALSE
# clustering samples...
if (hcmeth_cols != FALSE) {
  tmp_d = t(data)
  if (hcmeth_cols == "cor") {
    # ... based on correlation
    tmp_d = tmp_d[!apply(is.na(tmp_d), 1, any), ]
    d = dist(1 - cor(t(tmp_d), method="pe"))
    hc_col = hclust(d, method="complete")
    Colv = as.dendrogram(hc_col)
  } else if (hcmeth_cols == "ordered") {
    # ... ordered by median
    data = data[,order(apply(tmp_d, 1, ordering_func, na.rm=TRUE), decreasing=TRUE)]
    hc_col = Colv = NULL
  } else {
    # ... based on eucl. dist.
    d = dist(tmp_d)
    hc_col = hclust(d, method="complete", members=members)
    Colv = as.dendrogram(hc_col)
  }
} else {
  hc_col = Colv = NULL
}

Colv = dd
ColSideColors = CSC
names(ColSideColors) = colnames(data)



hcmeth_rows = "eucl_dist"
hcmeth_rows = TRUE
# clustering features...
if (hcmeth_rows != FALSE) {
  tmp_d = data
  if (hcmeth_rows == "eucl_dist") {
    # ... based on eucl. dist.
    d = dist(tmp_d)
    hc_row = hclust(d, method="complete")
    Rowv = as.dendrogram(hc_row)
  } else if (hcmeth_rows == "ordered") {
    # ... ordered by median
    data = data[order(apply(tmp_d, 1, ordering_func, na.rm=TRUE), decreasing=TRUE),]
    hc_row = Rowv = NULL
  } else {
    # ... bases on correlation
    tmp_d = tmp_d[!apply(is.na(tmp_d), 1, any), ]
    d = dist(1 - cor(t(tmp_d), method="pe"))
    hc_row = hclust(d, method="complete")
    Rowv = as.dendrogram(hc_row)
  }
} else {
  hc_row = Rowv = NULL
}
RowSideColors = rep("white", nrow(data))
names(RowSideColors) = rownames(data)
```

```{r fig.width=9, fig.height=9, dpi=150}
colors = c("cyan", "black", "red")
# colors = c("cyan", "cyan", "black", "red", "red")
# colors = c("cyan", "cyan", "cyan", "black", "red", "red", "red")
# colors = c("blue", "yellow", "red")
# colors = rev(RColorBrewer::brewer.pal(n=11, "RdYlBu"))
cols = colorRampPalette(colors)(20)
main=""

dendrogram="row"
mgn = lapply(study_tcga_filenames, function(study_tcga_filename) {
  s = mcreate_study(study_tcga_filename)
  tmp_idx_features = rownames(features) #intersect(rownames(features), rownames(s$data))
  idx_nt = rownames(s$exp_grp)[s$exp_grp$tissue_status == "normal"]
  idx_kc = rownames(s$exp_grp)[s$exp_grp$tissue_status == "tumoral"]
  s$exp_grp[idx_kc,]$main_gse_number
})
baz = t(sapply(bar, function(foo) {
  c(foo$main_gse_number,foo$mid_indiv)
}))

data[data > 4] = 4
data[data < -4] = -4

cnd = colnames(data)
names(cnd) = colnames(data)
cnd[names(cnd)] = ""
cnd[baz[,2]] = baz[,1]
colnames(data) = cnd
# colnames(data)[duplicated(unlist(mgn))] = ""
foo = gplots::heatmap.2(data, Rowv=Rowv, Colv=Colv, dendrogram=dendrogram, trace="none", col=cols, main=paste0(main, " (", nrow(data), " features x ", ncol(data), " tissues)"), mar=c(8,8), useRaster=TRUE, RowSideColors=RowSideColors, ColSideColors=ColSideColors, cexRow=0.6, cexCol=0.6)

































 # sapply(counts,function(d) {
 #   # d = counts[[matrix_file]]
 #   t(d[,i])
 # })
 head(tmp_d)
 dim(tmp_d)
 q = sort(unique(quantile(tmp_d, probs=seq(0,1,length.out=20), na.rm=TRUE)))
 q = c(-1,q)
 colors=c("royalblue", "springgreen", "yellow", "red")
 cols = colorRampPalette(colors)(length(q)-1)
 # image(tmp_d, col=cols, breaks=q, xaxt="n", yaxt="n", main="", useRaster=FALSE)

 # idx = 1:ncol(counts)
 # idx = unique(c(1,floor(seq(1, ncol(counts), l=10))))
 # axis(2, ((1:ncol(counts)-1)/(ncol(counts)-1))[idx], colnames(counts)[idx], las=2)
 # idx = unique(floor((1:(nrow(counts)-1))/10) * 10) + 1
 # axis(1, ((1:nrow(counts)-1)/(nrow(counts)-1))[idx], signif(seq(0,20, length.out=nrow(counts))[idx], 2), las=2)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
     """
    


rule compile_blastdb:
    input: os.path.expanduser("~/projects/heatshock/data/{subject}.fasta")
    output: os.path.expanduser("~/projects/heatshock/data/{subject}.blast.db")
    threads: 1
    shell:"""
/summer/epistorage/miniconda3/bin/makeblastdb -in {input} -dbtype nucl -parse_seqids -out {output}
touch {output}
    """
    
rule blastn_ggaat:
    input:
      blast_db=os.path.expanduser("~/projects/heatshock/data/{subject}.blast.db"),
      query_fqgz="{prefix}/{sample}_1.fastq.gz",
    output: "{prefix}/{sample}_{subject}.blasted.txt.gz"
    threads: 1
    shell:"""
gunzip -c {input.query_fqgz} | /summer/epistorage/miniconda3/bin/seqtk seq -A | 
/summer/epistorage/miniconda3/bin/blastn -db {input.blast_db} -num_threads=1 -query - -outfmt "10 std sstrand" -evalue 10 -task blastn-short -word_size 8 -perc_identity 100 -qcov_hsp_perc 1  2>/dev/null | gzip  > {output}
    """


rule blastn_unmapped_ggaat:
    input:
      blast_db=os.path.expanduser("~/projects/heatshock/data/{subject}.blast.db"),
      query_fqgz="{prefix}/{sample}_{trim}_star_{species}_{index}_Unmapped.out.mate1.gz",
    output: "{prefix}/{sample}_{trim}_star_{species}_{index}_{subject}.unmapblasted.txt.gz"
    threads: 1
    shell:"""
cat {input.query_fqgz} | /summer/epistorage/miniconda3/bin/seqtk seq -A | 
/summer/epistorage/miniconda3/bin/blastn -db {input.blast_db} -num_threads=1 -query - -outfmt "10 std sstrand" -evalue 10 -task blastn-short -word_size 8 -perc_identity 100 -qcov_hsp_perc 1  2>/dev/null | gzip  > {output}
    """



rule trim_fastxtoolkit:
    input:
      fastq="{prefix}.fastq.gz", 
      fastqc="{prefix}_fastqc.zip",
    output: "{prefix}_fastxtrimf{trim}.fastq.gz"
    threads: 1
    shell:"""
tmpfile=$(mktemp /var/tmp/tmp_trimed_file_XXXXXXXXXX.fq.gz)
echo computing $tmpfile ...
gunzip -c  {input.fastq} | /summer/epistorage/miniconda3/envs/fastx-toolkit_env/bin/fastx_trimmer -l {wildcards.trim} -Q33 -z -o $tmpfile
echo move $tmpfile to output.
cp $tmpfile {output}
rm $tmpfile
    """

rule count_bowtie:
    input:
      bam_file="{prefix}/{sample}_{localendtoend}_trim{trim}.bam",
      gtf_file= "/scratch_r730/datashare/genomes/Mus_musculus/UCSC/mm10/Annotation/Genes/genes.gtf"
    output: "{prefix}/{sample}_{localendtoend}_trim{trim}_gene_counts.txt"
    priority: 50000
    threads: 1
    shell:"""
/summer/epistorage/miniconda3/bin/htseq-count -f bam -r name -s no -m intersection-nonempty \
  {input.bam_file} \
  {input.gtf_file} \
  > {output}
    """


          
rule bigwig_coverage_advanced:
    input: "{prefix}_srt.bam", 
    output: "{prefix}_srt_{mmq}_{binsize}_{norm}.bw"
    threads: 32
    shell:"""
PATH="/summer/epistorage/miniconda3/bin:$PATH"
export TMPDIR=/dev/shm
bamCoverage \
  -b {input} \
  --extendReads \
  --numberOfProcessors {threads} \
  --binSize {wildcards.binsize} \
  --minMappingQuality {wildcards.mmq} \
  --normalizeUsing {wildcards.norm} \
  -o {output}

    """

rule bigwig_coverage_advanced_SR:
    input: "{prefix}/{sample}_{localendtoend}_trim{trim}_srt.bam", 
    output: "{prefix}/{sample}_{localendtoend}_trim{trim}_srtsr_{mmq}_{binsize}_{norm}.bw"
    threads: 32
    shell:"""
export TMPDIR=/dev/shm
/summer/epistorage/miniconda3/bin/bamCoverage \
  -b {input} \
  --numberOfProcessors {threads} \
  --binSize {wildcards.binsize} \
  --minMappingQuality {wildcards.mmq} \
  --normalizeUsing {wildcards.norm} \
  -o {output}

    """

    
          
          
          
rule fastqc:
    input:  fastqgz="{prefix}.fastq.gz"
    output: zip="{prefix}_fastqc.zip",
            html="{prefix}_fastqc.html"
    threads: 1
    shell:"""
    PATH="/summer/epistorage/miniconda3/bin:$PATH"
    fastqc {input.fastqgz}
    """









rule index_genome:
    input:
      genome_fasta="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Sequence/WholeGenomeFasta/genome.fa", 
      gtf="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Annotation/Genes/genes.gtf",
    output: directory("/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Sequence/StarIndex")
    #priority: 0
    threads: 32
    shell:    """
mkdir -p {output}
/summer/epistorage/miniconda3/bin/STAR \
  --runThreadN `echo "$(({threads} * 2))"` \
  --runMode genomeGenerate \
  --genomeDir {output} \
  --genomeFastaFiles  {input.genome_fasta} \
  --sjdbGTFfile {input.gtf} \
  --sjdbOverhang 100
    """


      # "/home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn1_local_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.bam",
      #  /home/fchuffar/projects/datashare_epistorage/TGML_runs/bam_epimed/P_rn1_trimno_star_Mus_musculus_mm10_Aligned.sortedByCoord.out.info

rule align_trimed:
    input:
      # fqgz_file="{prefix}/{sample}_{trim}.fastq.gz",
      # fastqc_file="{prefix}/{sample}_{trim}_fastqc.zip",
      fastq_info="{prefix}/{sample}_{trim}_fqgz.info",
      star_index="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Sequence/StarIndex",
      # star_index_file="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Sequence/StarIndex/SAindex",
      gtf="/home/fchuffar/projects/datashare/genomes/{species}/UCSC/{index}/Annotation/Genes/genes.gtf",
    output:  "{prefix}/{sample}_{trim}_star_{species}_{index}_Aligned.sortedByCoord.out.bam"
    threads: 32
    shell:"""
cd {wildcards.prefix}
/summer/epistorage/miniconda3/bin/STAR \
  --runThreadN {threads} \
  --genomeDir  {input.star_index} \
  --sjdbGTFfile {input.gtf} \
  --readFilesCommand gunzip -c \
  --readFilesIn `cat {input.fastq_info}` \
  --outFileNamePrefix {wildcards.prefix}/{wildcards.sample}_{wildcards.trim}_star_{wildcards.species}_{wildcards.index}_ \
  --outReadsUnmapped Fastx \
  --outSAMtype BAM SortedByCoordinate
sleep 30
echo "indexing bam_file"
/summer/epistorage/miniconda3/bin/samtools index {output}
    """







rule count_classic:
    input:
      bam_file="{prefix}/{sample}_{sr_or_pe}_{trim}_star_{species}_{index}_Aligned.sortedByCoord.out.bam",
      gtf_file= "/scratch_r730/datashare/genomes/{species}/UCSC/{index}/Annotation/Genes/genes.gtf" 
    output: "{prefix}/{sample}_{sr_or_pe}_{trim}_star_{species}_{index}_gene_counts.txt"
    # priority: 50
    threads: 1
    shell:"""
/summer/epistorage/miniconda3/bin/htseq-count -f bam -r name -s no -m intersection-nonempty \
  {input.bam_file} \
  {input.gtf_file} \
  > {output}
    """

# rule bigwig_coverage:
#     input:
#       bam_file="{prefix}/{sample}_{sr_or_pe}_{trim}_star_{species}_{index}_Aligned.sortedByCoord.out.bam",
#     output: "{prefix}/{sample}_{sr_or_pe}_{trim}_star_{species}_{index}_Aligned.sortedByCoord.out.bw"
#     threads: 4
#     shell:"""
# /summer/epistorage/miniconda3/bin/bamCoverage \
#   -b {input.bam_file} \
#   --numberOfProcessors `echo "$(({threads} * 2))"` \
#   --binSize 10 \
#   --minMappingQuality 30 \
#   --normalizeUsingRPKM \
#   -o {output}
#
#     """