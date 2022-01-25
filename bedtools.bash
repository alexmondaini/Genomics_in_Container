#!/usr/bin/env bash

mkdir -p sorted 
# sort exon file and target file for faster process in bedtools
# awk 'NR==1 {print}' grch37.exon_info_refseq.bed > grch37.exon_sorted.bed
awk 'NR>1 {print}' grch37.exon_info_refseq.bed | sort -k1,1 -k2,2n > sorted/grch37.exon_sorted.bed
sort -k1,1 -k2,2n grch37.testregion.bed > sorted/grch37.testregion_sorted.bed

# Summary statistics
# Question 1 
mkdir -p stats
mkdir -p temp
# Genes/Regions located between in range chr13:26000000-36000000
bedtools intersect -a sorted/grch37.exon_sorted.bed -b sorted/grch37.testregion_sorted.bed > temp/grch37.exon_intersection.bed
# summary stats of the target file coverage on the genes/regions desired
bedtools coverage -a sorted/grch37.testregion_sorted.bed -b temp/grch37.exon_intersection.bed > stats/grch37.testregion_stats.bed

# fraction of exonic bases covered by target
bedtools annotate -i temp/grch37.exon_intersection.bed -files sorted/grch37.testregion_sorted.bed > stats/grch37.exonic_fraction.bed
# fraction of target file covered by exonic bases
bedtools annotate -i sorted/grch37.testregion_sorted.bed -files temp/grch37.exon_intersection.bed > stats/grch37.target_fraction.bed


# Question 3 generate input file (clinvar_chr_intersect.vcf.gz)
# Inconsistent chr notation in clinvar file and refseq exon bed file, add chr to clinvar field so we can intersect with bedtools.
gzip -d -k clinvar.vcf.gz
awk 'NR<29 {print }' clinvar.vcf > clinvar_chr.vcf 
awk 'NR>=29 {print "chr"$0}' clinvar.vcf | sort -k1,1 -k2,2n >> clinvar_chr.vcf
bedtools intersect -a clinvar_chr.vcf -b sorted/grch37.testregion_sorted.bed -sorted | cat <(head -28 clinvar_chr.vcf) -  > clinvar_chr_intersect.vcf
rm clinvar_chr.vcf clinvar.vcf
gzip -k clinvar_chr_intersect.vcf