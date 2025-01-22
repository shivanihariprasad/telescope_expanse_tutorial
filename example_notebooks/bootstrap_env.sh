#!/usr/bin/bash
SLURM_JOB_ID=squeue -u $LOGNAME |grep $HOSTNAME | awk '{print $1}'

cd "/scratch/${USER}/job_${SLURM_JOB_ID}"
cp -r ~/telescope_expanse_tutorial "/scratch/${USER}/job_${SLURM_JOB_ID}/"
python3.9 -m venv .venv
. ./.venv/bin/activate
pip install --upgrade pip
pip install jupyter pyspark==3.2.1 pandas matplotlib seaborn scipy findspark pyarrow fastparquet

# 1 day of flowtuples
# compute-1x128_128G.slurm   3min 51s
# compute-2x128_256G.slurm   2min 18s

# zeus
#default local cluster cfg  10min 2s
#default client cluster cfg  11min 51
