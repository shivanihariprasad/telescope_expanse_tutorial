#!/usr/bin/bash
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <job_id>"
    exit 1
fi

SLURM_JOB_ID="$1"
%SLURM_JOB_ID="$(squeue -u $LOGNAME |grep $HOSTNAME | awk '{print $1}')"
cd "/scratch/${USER}/job_${SLURM_JOB_ID}"; 
#load ucsdnt s3 key into the environment 
source /expanse/lustre/projects/csd939/kmok/.ucsdnts3.key

python3.9 -m venv .venv;
. ./.venv/bin/activate;
python3 count-dstnet.py