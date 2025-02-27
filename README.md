# AIMS 2025 Telescope data analysis on SDSC Expanse tutorial

This repository contains tutorial materials for analyzing UCSD network telescope data on SDSC Expanse HPC. 

# Prerequisite 
 1. Register an account on [ACCESS-CI](https://access-ci.org) 
 2. Apply for allocation on [ACCESS-CI](https://access-ci.org) 
 3. Exchange your credits into SDSC Expanse CPU and Project Storage credits
 4. Credential for accessing CAIDA's Swift object storage

**For AIMS 2025 participants, we have already prepared 2-4 for you.**

# Directory structure
`slurm_scripts`:
 - Sample scripts to initialize and configure your jobs on Expanse

`example_notebooks`:
 - Examples of functional research-grade notebooks for ad-hoc traffic analysis.

`example_ft_batch`:
 - Example scripts for a simple batch analysis using FlowTuple dataset

`example_golang_docker`:
 - Example Dockerfile for building containers for running analysis on Expanse

`ucsdnt-swift-utils`:
 - Sample scripts to generate parquet-formatted lists of available FlowTuple files
 
