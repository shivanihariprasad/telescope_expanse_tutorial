#!/bin/bash
#SBATCH --job-name=spark-pi
#SBATCH --partition=shared
#SBATCH --account=csd939
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=1000
#SBATCH --time=00:30:00
#SBATCH --output="joblogs/slurm-%A_%a.out"

REPO_DIR=/home/${USER}/telescope_expanse_tutorial
cd ${REPO_DIR}/slurm_scripts

/bin/bash launch-spark.sh
/bin/bash bootstrap_env.sh

#load ucsdnt s3 key into the environment 
source /expanse/lustre/projects/csd939/kmok/.ucsdnts3.key
# Submit batch job
cd ${REPO_DIR}/example_ft_batch/
batch_script="count-dstnet.py"
#batch_script="run_batch.sh ${SLURM_JOB_ID}"


source /expanse/lustre/projects/csd939/kmok/.ucsdnts3.key

cd "/scratch/${USER}/job_${SLURM_JOB_ID}"; 

python3.9 -m venv .venv;
. ./.venv/bin/activate;

/expanse/lustre/scratch/${USER}/temp_project/spark-3.2.1/bin/spark-submit --packages org.apache.spark:spark-avro_2.12:3.2.1,org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk-bundle:1.12.262 "$batch_script"
