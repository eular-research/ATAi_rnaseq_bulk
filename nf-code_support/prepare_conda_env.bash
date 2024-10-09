#!/bin/bash

### Better to copy paste the following commands. 
# Adding bioconda and conda-forge channels
echo "Adding bioconda channel..."
conda config --add channels bioconda
echo "bioconda channel added."

echo "Adding conda-forge channel..."
conda config --add channels conda-forge
echo "conda-forge channel added."

# Creating a new conda environment named 'env_nf' with nextflow
echo "Creating conda environment 'env_nf' with nextflow..."
conda create --name env_nf nextflow -y
echo "Conda environment 'env_nf' created."

# Activating the new conda environment
echo " source ..."
source ~/.bashrc

# Initializing conda for bash
echo "Initializing conda for bash..."
conda init 
echo "Conda initialized for bash."

### IF you can't see "(base)" in the beginning of cli then start a new terminal! ###
# and activate:   
conda activate env_nf
echo "Conda environment 'env_nf' activated."

# Activate conda
echo "Activating conda environment 'env_nf'..."
source ~/.bashrc

conda env list

conda activate env_nf
echo "Conda environment 'env_nf' activated."


# Updating nextflow to the latest version
echo "Updating nextflow to the latest version..."
nextflow self-update
echo "Nextflow updated to the latest version."

echo "Script execution completed."

# conda env create -f /workspaces/ATAi/nf-code_support/conda_env_merge.yaml


