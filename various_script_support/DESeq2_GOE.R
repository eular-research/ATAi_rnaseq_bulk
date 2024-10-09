# Load necessary libraries
library(tidyverse)
library(DESeq2)
library(tximport)
library(GenomicFeatures)
library(AnnotationDbi)
library(org.Hs.eg.db) # Replace with the appropriate organism database

# Define file paths
salmon_dir <- "/workspaces/ATAi/tmp/star_salmon/"
gene_counts_file <- file.path(salmon_dir, "salmon.merged.gene_counts.tsv")
gene_tpm_file <- file.path(salmon_dir, "salmon.merged.gene_tpm.tsv")
tx2gene_file <- file.path(salmon_dir, "tx2gene.tsv")

# Load data
gene_counts <- read_tsv(gene_counts_file)
gene_tpm <- read_tsv(gene_tpm_file)
tx2gene <- read_tsv(tx2gene_file)

# Prepare tximport input
files <- list.files(salmon_dir, pattern = "quant.sf", full.names = TRUE)
names(files) <- gsub("_quant/quant.sf", "", files)
txi <- tximport(files, type = "salmon", tx2gene = tx2gene)

# Create sample information
sample_info <- data.frame(
  row.names = colnames(txi$counts),
  condition = c("RAP1_IAA_30M", "RAP1_UNINDUCED", "WT") # Modify as per your samples
)

# DESeq2 analysis
dds <- DESeqDataSetFromTximport(txi, colData = sample_info, design = ~ condition)
dds <- DESeq(dds)
res <- results(dds)

# Save results
write.csv(as.data.frame(res), file = "deseq2_results.csv")

# Plot results
plotMA(res, main = "DESeq2", ylim = c(-2, 2))

# Gene ontology enrichment analysis (optional)
library(clusterProfiler)
ego <- enrichGO(gene = rownames(res[which(res$padj < 0.05), ]),
                OrgDb = org.Hs.eg.db, # Replace with appropriate organism database
                keyType = "ENSEMBL",
                ont = "BP",
                pAdjustMethod = "BH",
                qvalueCutoff = 0.05,
                readable = TRUE)
barplot(ego, showCategory = 20)

# Save the R environment
save.image(file = "analysis.RData")




