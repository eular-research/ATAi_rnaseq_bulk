# Welcome to ATAi
This repository is dedicated to the analysis of bulk NGS data, with a focus on RMD-related diseases and experiments. It is part of the [EULAR ATAi](https://www.eular.org/eular-atai) project. 

## Design your RNAseq experiment
Design your RNAseq experiment and consider: 
* Biological question.
* How many samples and replicates. 
* What sequencing Depth. 
* This notebook helps with Power analysis: [design rnaseq notebook](rnaseq_analysis/design_considerations/01_experimental_design_rnaseq.ipynb)

## Fetch public data
The notebook [fetch_data notebook](rnaseq_analysis/data_fetch/00_fetch_data.ipynb) will help to fetch data from ENA. 

## Fetch annotation of genes you are interested in ensembl
The notebook [fetch gene annotation from Ensembl](rnaseq_analysis/data_fetch/00_fetch_geneset_annotation.ipynb) will help to get Ensembl annotation. 

## Run pipeline
* help documents for nf-code rnaseq pipeline. https://nf-co.re/rnaseq/3.14.0 and https://igb.mit.edu/mini-courses/advanced-utilization-of-igb-computational-resources/running-nextflow-nf-core-pipelines

* script to prepare env for running the nf-rnaseq pipeline - open file and run commands manually, if not working: 
[prepare env bash](nf-code_support/prepare_conda_env.bash)
* activate the nf conda env: 
$ conda activate env_nf
* quick start test command: 
$ nextflow run nf-core/rnaseq  -profile test,docker --outdir ./tmp/
* if there are issue with the previous command try to change profile to conda or adding version -r: 
$ nextflow run nf-core/rnaseq  -profile test,conda  --outdir ./tmp/ -r 3.12.0
* run pipeline for the data prepared: 
$ nextflow run nf-core/rnaseq  -profile conda --input ./nextflow_samples.csv  --outdir ./tmp/ -r 3.12.0  --genome GRCh38

## Analysis of rnaseq data example workflows  
Results of the pipeline can be found in " --outdir " parameter. In this example, the dir should be named: " ./tmp/ " . To expore (mocked and real) data:  
* [First look of nf output](rnaseq_analysis/data_analysis/01_basic_explore.ipynb)
* [Gene expression analysis R](rnaseq_analysis/data_analysis/02_GeneExpression.ipynb)
* [Single cell analysis R](rnaseq_analysis/data_analysis/03_GeneExpressionSingleCellR.ipynb)

## conda enviroments
* Information about conda env are in [conda support](nf-code_support)
* Notebooks require a conda env, this can be created: conda env create -f ./nf-code_support/env_merged_env.yml 

## Clean afterwards 
rm -rf ./work/
rm -rf ./tmp/

