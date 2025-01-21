#!/bin/bash
#SBATCH --job-name=spark-pi
#SBATCH --partition=compute
#SBATCH --account=<acct name>
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128
#SBATCH --mem-per-cpu=1900
#SBATCH --time=08:00:00
#SBATCH --output="joblogs/slurm-%A_%a.out"

cd /home/${USER}/expanse_spark/slurm_scripts
. launch-spark.sh
. bootstrap_env.sh

# Launch Jupyter and sleep forever
jupyter-lab --port 8135 --no-browser
sleep infinity
