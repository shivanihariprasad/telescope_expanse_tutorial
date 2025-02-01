#!/bin/bash
#SBATCH --job-name=spark-pi
#SBATCH --partition=debug
#SBATCH --account=csd939
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=1000
#SBATCH --time=00:30:00
#SBATCH --output="joblogs/slurm-%A_%a.out"

module purge
module load slurm
module load cpu/0.15.4
module load singularitypro

JOB_OUTPUT_DIR=/expanse/lustre/projects/csd939/${USER}/golang_container_output
mkdir -p $JOB_OUTPUT_DIR


# Submit batch job
singularity exec --env-file /expanse/lustre/projects/csd939/kmok/.ucsdnts3.env \
    --bind /expanse/lustre/projects/csd939/${USER}/golang_container_output:/output \
    /expanse/lustre/projects/csd939/kmok/shared_data/expanse-uscdnt-golang.sif \
    cat /output/filelists.csv | parallel \
        -j 5 \
        --joblog /output/joblog_{#}/ \
        --results /output/results_{#} \
        /go/bin/ucsdntexample -o /output -c 100 -f {} 