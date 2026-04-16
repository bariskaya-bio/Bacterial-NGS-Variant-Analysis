#!/bin/bash
# ==========================================================
# Automated Variant Calling Pipeline for Bacterial Genomes
# Author: bariskaya-bio
# ==========================================================

# Configuration
REF="wildtype.fna"
READS="mutated_reads.fastq"
OUT_DIR="analysis_results"

mkdir -p $OUT_DIR

echo "[INFO] Running Quality Control (FastQC)..."
fastqc $READS -o $OUT_DIR

echo "[INFO] Mapping reads to reference (BWA-MEM)..."
bwa mem $REF $READS > $OUT_DIR/alignment.sam

echo "[INFO] Converting and sorting BAM files (Samtools)..."
samtools view -S -b $OUT_DIR/alignment.sam > $OUT_DIR/alignment.bam
samtools sort $OUT_DIR/alignment.bam -o $OUT_DIR/alignment_sorted.bam
samtools index $OUT_DIR/alignment_sorted.bam

echo "[INFO] Calling variants (BCFtools)..."
bcftools mpileup -f $REF $OUT_DIR/alignment_sorted.bam | bcftools call -mv -Ob -o $OUT_DIR/variants.bcf
bcftools view $OUT_DIR/variants.bcf > $OUT_DIR/final_variants.vcf

echo "[SUCCESS] Pipeline finished. Variants are saved in $OUT_DIR/final_variants.vcf"


