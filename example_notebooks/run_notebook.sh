#!/usr/bin/bash
SLURM_JOB_ID="$(squeue -u $LOGNAME |grep $HOSTNAME | awk '{print $1}')"
cd "/scratch/${USER}/job_${SLURM_JOB_ID}"; 
python3.9 -m venv .venv;
. ./.venv/bin/activate;
jupyter-lab --port 9000 --no-browser