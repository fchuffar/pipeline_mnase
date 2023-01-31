get_nb_reads_core = function(bam_file, args) {
  cmd = "samtools"
  args = paste0(args, bam_file)
  print(paste(cmd, args))
  nb_reads = as.numeric(system2(cmd, args, stdout=TRUE))
  return(nb_reads)
}
if  (!exists("mget_nb_reads_core")) {
  mget_nb_reads_core = memoise::memoise(get_nb_reads_core)    
}

get_nb_reads = function(bam_file) {
  args = "view -c "
  mget_nb_reads_core(bam_file, args)
}

get_nb_mapped_reads_primary_aligned = function(bam_file) {
  args = "view -c -F 260 "
  mget_nb_reads_core(bam_file, args)
}




if (!exists("mread.fasta")) {
  mread.fasta = memoise::memoise(function(...) {
    fasta = seqinr::read.fasta(...)
    m_orig = as.matrix(do.call(rbind, fasta))
    m_orig[m_orig=="n"] = NA
    dim(m_orig)

    m = m_orig[,]
    # m = m_orig[,900:1000]
    pwm = apply(m, 2, function(c){
      # c = factor(c, levels=c("a", "c", "g", "t", "n"))
      prop.table(table(c))
    })
    return(pwm)
  })
}




draw_fig = function(signal) {
  layout(matrix(1:6, 2), respect=TRUE)
  alpha.f = 0.3
  pch = 1
  for (k in names(SSRP1_WT)) {
    xlim = ylim = c(
      min(c(signal[["HIRA__WT"]][[k]], signal[["SSRP1_WT"]][[k]], signal[["HIRA__KO"]][[k]], signal[["SSRP1_KO"]][[k]]), na.rm=TRUE),
      max(c(signal[["HIRA__WT"]][[k]], signal[["SSRP1_WT"]][[k]], signal[["HIRA__KO"]][[k]], signal[["SSRP1_KO"]][[k]]), na.rm=TRUE)
    )
    print(xlim)
    # mWT = MASS::rlm(signal[["SSRP1_WT"]][[k]]~signal[["HIRA__WT"]][[k]])
    # mKO = MASS::rlm(signal[["SSRP1_KO"]][[k]]~signal[["HIRA__KO"]][[k]])
    mWT = lm(signal[["SSRP1_WT"]][[k]]~signal[["HIRA__WT"]][[k]]) 
    mKO = lm(signal[["SSRP1_KO"]][[k]]~signal[["HIRA__KO"]][[k]]) 
    # layout(matrix(1:2, 1), respect=TRUE)
    plot(signal[["HIRA__WT"]][[k]], signal[["SSRP1_WT"]][[k]], pch=pch, col=adjustcolor(2, alpha.f=alpha.f), xlim=xlim, ylim=ylim, # xlim=c(-15,15), ylim=c(-15,15), #
      main=paste0(
        k, " ", 
        "SSRP1~HIRA" 
      ), 
      xlab="HIRA", 
      ylab="SSRP1"
    )
    abline(b=1, a=0, col="grey", lty=2)
    points(signal[["HIRA__KO"]][[k]], signal[["SSRP1_KO"]][[k]], pch=pch, col=adjustcolor(4, alpha.f=alpha.f))

    abline(mWT, col=2)
    pred =  predict(mWT, interval="predict", level=0.95)
    idx = order(mWT$model[,2])
    lines(range(mWT$model[idx,2]), range(pred[idx,2]), col=2, lty=2)
    lines(range(mWT$model[idx,2]), range(pred[idx,3]), col=2, lty=2)

    abline(mKO, col=4)
    pred =  predict(mKO, interval="predict", level=0.95)
    idx = order(pred[,1])
    lines(range(mKO$model[idx,2]), range(pred[idx,2]), col=4, lty=2)
    lines(range(mKO$model[idx,2]), range(pred[idx,3]), col=4, lty=2)
    legend("topleft", c(paste0("WT R^2=", signif(lm_r2(mWT),2)), paste0("KO R^2=", signif(lm_r2(mKO),2))), col=c(2,4), lty=1)
  
    # bw=0.5
    # # set1 = rnorm(100, 0, 1)
    # # set2 = rnorm(100, 0, 2)
    set1 = mKO$residuals
    set2 = mWT$residuals
    if (length(set1) != length(set2)) {stop("Hartley test.")}
    # pval = PMCMRplus::hartleyTest(c(set1, set2)~as.factor(rep(c("set1", "set2"), each=length(set1))))$p.value
    # # pval=1
    # pval
    fmax = var(mWT$residuals)/var(mKO$residuals)
    SuppDists::pmaxFratio(fmax, df=length(set1)-1, k=2)
    pval = SuppDists::pmaxFratio(fmax, df=length(set1)-1, k=2, lower.tail=FALSE)
    pval  
    plot( density(mKO$residuals), col=4, lwd=1, main=paste0("residuals distr. Hartley pval=", signif(pval,3)))
    lines(density(mWT$residuals), col=2, lwd=1)
    legend("topleft", c(paste0("WT"), paste0("KO")), col=c(2,4), lty=1)    
  }
  # https://webapps.fundp.ac.be/umdb/biostats2017/biostat/modules/module125/page2.html
  # https://stackoverflow.com/questions/8513433/how-to-perform-hartleys-test-in-r
  # https://cran.r-project.org/web/packages/SuppDists/index.html

  # Hartley, H.O. (1950) The maximum F-ratio as a short cut test for heterogeneity of variance, Biometrika 37, 308–312.


  # PMCMRplus::hartleyTest
  # SuppDists::pmaxFratio

  # set1 = rnorm(100, 0, 1)
  # set2 = rnorm(100, 0, 2)
  # pval = PMCMRplus::hartleyTest(c(set1, set2)~as.factor(rep(c("set1", "set2"), each=length(set1))))$p.value
  #
  #
  # hartleyTest(count ~ spray, data = InsectSprays)
}


rlm_r2 <- function(x){
  SSe <- sum(x$w*(x$resid)^2)
  observed <- x$resid+x$fitted
  SSt <- sum(x$w*(observed-weighted.mean(observed,x$w))^2)
  1-SSe/SSt
}

lm_r2 <- function(x){
  summary(x)$r.squared
}


normalize_counts = function (count_filename) {
  # raw
  counts = read.table(count_filename, header=TRUE)
  rownames(counts) = paste0(counts[,2], ":", counts[,3], "-", counts[,4])
  pf = counts[,1:6]
  head(pf)
  counts = counts[, -(1:6)]
  colnames(counts) = substr(colnames(counts), 63, 75)
  head(counts)
  dim(counts)
  d = as.matrix(counts)
  # plot(density(d))

  # RPM normalized
  d_rpm = t(t(d) / apply(d, 2, sum) * 1000000)
  d_lrpm = log2(d_rpm + 1)

  # DESeq2 normalized
  countData = d
  colData = data.frame(id=colnames(countData), lines=factor(substr(colnames(d), 1, 8)))
  dds = DESeq2::DESeqDataSetFromMatrix(countData=countData, colData=colData, design= ~ lines)
  dds = DESeq2::estimateSizeFactors(dds)
  sf = dds$sizeFactor
  sf
  norm_counts = DESeq2::counts(dds, normalized=TRUE)
  d_norm = norm_counts
  d_lnorm = log2(norm_counts + 1)

  return(list(
    pf = pf,
    raw_counts = d    ,
    d_rpm   = d_rpm   ,
    d_lrpm  = d_lrpm  ,
    d_norm  = d_norm  ,
    d_lnorm = d_lnorm ,
    NULL
  ))
}
if (!exists("mnormalize_counts")) {mnormalize_counts = memoise::memoise(normalize_counts)}
if (! exists("mread.table")) {mread.table = memoise::memoise(read.table)}
if (! exists("mread.tablegz")) {
  mread.tablegz = memoise::memoise(function(matrix_file, ...) {
    read.table(gzfile(matrix_file), ...)
  })  
}


fast_matrix_file = function(matrix_file, GRP=FALSE) {
  # matrix_file = "matrix_gene_profile.txt.gz"
  # raw_wig_signal = read.table(gzfile(matrix_file), skip=1, stringsAsFactors=FALSE)
  # dim(raw_wig_signal)

  system2(command="zcat", args=paste0(matrix_file, " ", 
    "| sed -e 's/end-to-end_trim30_srt_PESF_30_4_None_SF//g' ", 
    "| sed -e 's/end-to-end_trim30_srt_mmq30_PESF_30_4_None_SF//g' ", 
    "| sed -e 's/_end-to-end_trim30_srt_PE_30_4_RPKM//g' ", 
    "| sed -e 's/_end-to-end_trim30_srt_30_4_RPKM//g' ", 
    "| sed -e 's/_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM/_nuc/g' ", 
    "| sed -e 's/_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM/_ss/g' ", 
    "| sed -e 's/_srt_30_4_RPKM//g' ", 
    "| sed -e 's/SRR1019858/GSM1253297/g' ", 
    "| sed -e 's/SRR1019859/GSM1253298/g' ", 
    "| sed -e 's/SRR1019860/GSM1253299/g' ", 
    "| sed -e 's/SRR1019861/GSM1253300/g' ", 
    "| sed -e 's/SRR1019862/GSM1253301/g' ", 
    "| sed -e 's/SRR1019863/GSM1253302/g' ", 
    "| sed -e 's/S_bn3/S_nuc_4/g' ", 
    "| sed -e 's/S_bn1/S_nuc_12/g' ", 
    "| sed -e 's/S_bn6/S_nuc_12/g' ", 
    "| sed -e 's/S_bn5/S_sms_4/g' ", 
    "| sed -e 's/S_bn2/S_sms_12/g' ", 
    "| sed -e 's/S_pp2/S_WT_04/g' ", 
    "| sed -e 's/S_pp4/S_WT_08/g' ", 
    "| sed -e 's/S_pp6/S_WT_12/g' ", 
    "| sed -e 's/S_nn2/S_KO_04/g' ", 
    "| sed -e 's/S_nn4/S_KO_08/g' ", 
    "| sed -e 's/S_nn6/S_KO_12/g' ", 

    "| sed -e 's/nme2//g' ", 
    "| sed -e 's/wt/WT/g' ", 
    "| sed -e 's/ko/KO/g' ", 

    "| sed -e 's/_m301//g' ", 
    "| sed -e 's/_m302//g' ", 
    "| sed -e 's/_m300//g' ", 
    "| sed -e 's/_m303//g' ", 
    "| sed -e 's/_m291//g' ", 
    "| sed -e 's/_m293//g' ", 
    "| sed -e 's/_m273//g' ", 
    "| sed -e 's/_m292//g' ", 

    "| gzip > ", matrix_file, ".fast.txt.gz"))
    NULL

  # write.table(raw_wig_signal[,], paste0(matrix_file, ".fast.txt"), quote=FALSE, col.names=FALSE, row.names=FALSE, append=TRUE, sep="\t", na="nan")
  # system2(command="rm", args=paste0(matrix_file, ".fast.txt.gz"))
  # system2(command="gzip", args=paste0(matrix_file, ".fast.txt"))
  # ret = list(raw_wig_signal=raw_wig_signal)
  # return(ret)
}


sort_matrix_file = function(matrix_file, GRP=FALSE) {
  raw_wig_signal = read.table(gzfile(matrix_file), skip=1, stringsAsFactors=FALSE)
  dim(raw_wig_signal)
  # plot(apply(raw_wig_signal[,-(1:6)], 2, mean))
  # abline(v=c(131,150), col=2)

  # filter_according_to_column_nb = 5
  # idx = ((filter_according_to_column_nb-1) * (brsl + arsl)/bin_size + 1):(filter_according_to_column_nb*(brsl + arsl)/bin_size)
  # q = quantile(apply(as.matrix(raw_wig_signal[1:1000,-(1:6)][,idx]), 1, mean), probs=0.990)
  # idx = which(as.vector(apply(as.matrix(raw_wig_signal[1:1000,-(1:6)][,idx]), 1,mean) > q))
  # # raw_wig_signal[idx,1:6][]
  # raw_wig_signal[idx,-(1:6)] = 0

  sort_according_to_column_nb = 3
  idx = ((sort_according_to_column_nb-1) * (brsl + arsl)/bin_size + 1):(sort_according_to_column_nb*(brsl + arsl)/bin_size)
  score = apply(raw_wig_signal[,-(1:6)][,idx], 1, function(l){
    # l = raw_wig_signal[7427,-(1:6)][,idx]
    which(l%in%max(l, ra.rm=TRUE))[1]
  })
  mat_centred_on_peak = raw_wig_signal[,1:6]
  mat_centred_on_peak[,2] = mat_centred_on_peak[,2] - brsl + score*bin_size 
  mat_centred_on_peak[,3] = mat_centred_on_peak[,2] + 1 

  grps = raw_wig_signal[,5]
  system2(command="zcat", args=paste0(matrix_file, " | head -n1 ", 
    "| sed -e 's/_end-to-end_trim30_srt_PE_30_4_RPKM//g' ", 
    "| sed -e 's/_end-to-end_trim30_srt_30_4_RPKM//g' ", 
    "| sed -e 's/_end-to-end_trim30_fsmin125_fsmax175_srt_30_4_RPKM/_nuc/g' ", 
    "| sed -e 's/_end-to-end_trim30_fsmin025_fsmax075_srt_30_4_RPKM/_ss/g' ", 
    "| sed -e 's/_srt_30_4_RPKM//g' ", 
    "| sed -e 's/SRR1019858/GSM1253297/g' ", 
    "| sed -e 's/SRR1019859/GSM1253298/g' ", 
    "| sed -e 's/SRR1019860/GSM1253299/g' ", 
    "| sed -e 's/SRR1019861/GSM1253300/g' ", 
    "| sed -e 's/SRR1019862/GSM1253301/g' ", 
    "| sed -e 's/SRR1019863/GSM1253302/g' ", 
    "| sed -e 's/S_bn3/S_nuc_4/g' ", 
    "| sed -e 's/S_bn1/S_nuc_12/g' ", 
    "| sed -e 's/S_bn6/S_nuc_12/g' ", 
    "| sed -e 's/S_bn5/S_sms_4/g' ", 
    "| sed -e 's/S_bn2/S_sms_12/g' ", 
    "| sed -e 's/S_pp2/S_WT_04/g' ", 
    "| sed -e 's/S_pp4/S_WT_08/g' ", 
    "| sed -e 's/S_pp6/S_WT_12/g' ", 
    "| sed -e 's/S_nn2/S_KO_04/g' ", 
    "| sed -e 's/S_nn4/S_KO_08/g' ", 
    "| sed -e 's/S_nn6/S_KO_12/g' ", 
    "> ", matrix_file, ".sort.txt"))


  if (GRP) {
    o = order(grps, score)
  } else {
    o = order(score)
  }


  # write.table(raw_wig_signal[o,], paste0(matrix_file, ".sort.txt"), quote=FALSE, col.names=FALSE, row.names=FALSE, append=TRUE, sep="\t")
  write.table(raw_wig_signal[,], paste0(matrix_file, ".sort.txt"), quote=FALSE, col.names=FALSE, row.names=FALSE, append=TRUE, sep="\t", na="nan")
  system2(command="rm", args=paste0(matrix_file, ".sort.txt.gz"))
  system2(command="gzip", args=paste0(matrix_file, ".sort.txt"))  
  ret = list(raw_wig_signal=raw_wig_signal, ordered_wig_signal=raw_wig_signal[o,] , centred_on_peak_bed=mat_centred_on_peak[o,])
  return(ret)
}

get_danpos_out = function (prefix, danpos_out_dir, algo = "positions") {
  danpos_out_file = paste0(danpos_out_dir, "/pooled/", prefix, ".smooth.", algo, ".xls")
  print(danpos_out_file)
  danpos_out = read.table(danpos_out_file, head=TRUE, sep="\t")
  rownames(danpos_out) = paste0("nuc_", 1:nrow(danpos_out))
  danpos_out$len = danpos_out$end - danpos_out$start
  danpos_out
}


get_danpos_out_annot = function (prefix, danpos_out_dir, algo = "positions", genome = 'mm10') {
  danpos_out = mget_danpos_out(prefix, danpos_out_dir, algo=algo)
  feat = danpos_out
  # feat = feat[sample(1:nrow(feat), nb_rnd_feat),]
  feat[,2] = danpos_out$smt_pos
  feat[,3] = feat[,2] + 1
  feat[,4] = rownames(danpos_out)
  feat[,5] = danpos_out$smt_value
  feat[,6] = "+"
  # print(head(feat))
  dim(feat)
  regions_filename = paste0("danpos_out_as_feat_", prefix, ".bed")
  write.table(feat[,1:6], file=regions_filename, sep="\t", quote=FALSE,row.names=FALSE, col.names=FALSE)    

  dm_regions = annotatr::read_regions(con=regions_filename, genome = genome, format = 'bed')
  # Intersect the regions we read in with the annotations
  dm_annotated = annotatr::annotate_regions(
      regions = dm_regions,
      annotations = annotations,
      ignore.strand = TRUE,
      quiet = FALSE)
  # A GRanges object is returned
  df_dm_annotated = data.frame(dm_annotated)
  df_dm_annotated$annot.type = as.factor(df_dm_annotated$annot.type)
  ret = df_dm_annotated
  # dim(df_dm_annotated)
  # head(df_dm_annotated)
  # # df_dm_annotated = df_dm_annotated[!duplicated(paste0(df_dm_annotated$name, df_dm_annotated$annot.type)),]
  # dim(df_dm_annotated)
  # # See the GRanges column of dm_annotaed expanded
  # # print(head(df_dm_annotated))
  # ret = table(df_dm_annotated$annot.type)
  return(ret)
}

if (! exists("mget_danpos_out_annot")) {
  mget_danpos_out_annot = memoise::memoise(get_danpos_out_annot)
}

if (! exists("mget_danpos_out")) {
  mget_danpos_out = memoise::memoise(get_danpos_out)
}
