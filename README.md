# Bacterial-NGS-Variant-Analysis
End-to-end variant calling pipeline and functional annotation of antibiotic resistance mutations in S. aureus.

# Bacterial NGS Variant Analysis Project

This project demonstrates an end-to-end bioinformatics pipeline for identifying antibiotic resistance mutations from raw NGS data.

## 🛠 Tools & Technologies
- **Language:** Python, Bash
- **Tools:** BWA, Samtools, BCFtools, FastQC
- **Visualization:** IGV (Integrative Genomics Viewer)
- **OS:** Linux (Ubuntu/WSL)

## 🧬 Analysis Workflow
1. **Quality Control:** Raw FASTQ files were inspected using FastQC.
2. **Alignment:** Reads were mapped to the reference genome using BWA-MEM.
3. **Variant Calling:** SNPs and Indels were identified using BCFtools.
4. **Functional Annotation:** Mutations were analyzed at the protein level using a custom Biopython script.

## 📊 Key Findings
- **Target Gene:** `mecR1`
- **Mutation Found:** g.47299T>A
- **Protein Effect:** Missense mutation (Cysteine -> Serine)
- **Insight:** This mutation potentially disrupts disulfide bonds in the MecR1 sensor protein, contributing to methicillin resistance.
