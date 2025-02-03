# slurm_scripts
`compute-1x8_8G-debug.slurm`: Small allocation in "debug" partition for testing
`compute-1x8_8G-batch-debug.slurm`: Small allocation in "debug" partition for batch analysis
`container-1x8_8G-batch-debug.slurm`: Small debug allocation to run multi-thread-enabled analysis
`container-1x8_8G-parallel-batch-debug.slurm`: Small debug allocation to parallelize single-thread analysis
`compute-1x128_256G.slurm`: One Expanse compute node for interactive analysis (for your reference. not used in this tutorial)
`compute-2x128_256G-batch.slurm`: Two Expanse compute nodes for batch analysis (for your reference. not used in this tutorial)

## Scripts for setting up python environment
`launch-spark.sh`: Script for setting up environment variables
`bootstrap_env.sh`: Script for copying compiled python into your job and install python modules
`wait-worker.sh`: Script for detecting workers

## Data file 
`filelists.csv`: a list of files for the golang container example (`container-1x8_8G-parallel-batch-debug.slurm`)

## Basic Operations
### 1. Schedule your job
`sbatch <slurm script>` 

### 2. Query your scheduled tasks
`squeue -u <your username>`
Example output of a queuing job:

    $ squeue -u kmok 
    JOBID PARTITION NAME USER ST TIME NODES NODELIST(REASON) 
    36394308 compute spark-pi kmok PD 0:00 1 (Priority)

Example output of a running job

    $ squeue -u kmok 
    JOBID PARTITION NAME USER ST TIME NODES NODELIST(REASON) 
    36394498 debug spark-pi kmok R 0:01 1 exp-9-55
`exp-9-55` is the allocated Expanse node that you can login (i.e., `exp-9-55.expanse.sdsc.edu`)

### 3. Cancel a scheduled task
By jobid shown in squeue:
`scancel <jobid>`
By username
`scancel -u <username>`
