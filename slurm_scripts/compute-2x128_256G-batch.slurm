#!/bin/bash
#SBATCH --job-name=spark-pi
#SBATCH --partition=compute
#SBATCH --account=<acct name>
#SBATCH --nodes=2
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=128
#SBATCH --mem-per-cpu=1900
#SBATCH --time=0:45:00
#SBATCH --output="joblogs/slurm-%A_%a.out"

cd /home/${USER}/expanse_spark/slurm_scripts
. launch-spark.sh
. bootstrap_env.sh

# Submit batch job
batch_script=~/spark_env/count-sources.py
spark-submit --packages org.apache.spark:spark-avro_2.12:3.2.1,org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk-bundle:1.12.262 "$batch_script"
