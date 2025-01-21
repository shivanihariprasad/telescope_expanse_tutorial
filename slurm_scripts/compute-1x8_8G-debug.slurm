#!/bin/bash
#SBATCH --job-name=spark-pi
#SBATCH --partition=debug
#SBATCH --account=<acct name>
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=1000
#SBATCH --time=00:30:00
#SBATCH --output="joblogs/slurm-%A_%a.out"

cd /home/${USER}/expanse_spark/slurm_scripts
. launch-spark.sh
. bootstrap_env.sh

# Launch Jupyter and sleep forever
jupyter-lab --port 8135 --no-browser
sleep infinity
