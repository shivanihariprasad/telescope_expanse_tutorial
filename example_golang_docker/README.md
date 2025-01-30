# Running your docker container on Expanse
This example shows you how to create a singularity container to execute a simple analysis code implemented in Golang. The code directly streams UCSD-NT pcap files from CAIDA's Swift object storage (via S3).

## Step 1: Implement your analysis
We created an example analysis on 

## Step 2: Build the Docker image
`docker built <your docker hub>/<your dockerhub repo>``

## Step 3: Build singularity image (on your machine)
## 3.1 Install singularity
For debian/Ubuntu, generate the command using the following web page
https://neuro.debian.net/install_pkg.html?p=singularity-container
For example, on Ubuntu 20.04
```
$ wget -O- http://neuro.debian.net/lists/focal.us-ca.full | sudo tee /etc/apt/sources.list.d/neurodebian.sources.list
$ sudo apt-key adv --recv-keys --keyserver hkps://keyserver.ubuntu.com 0xA5D32F012649A5A9
$ sudo apt-get update
$ sudo apt-get install singularity-container
```
## 3.2 Build singularity image from your dockerhub image
`sudo singularity build <singularity_image_name>.sif docker://<path to your dockerhub image>`
Our example: 
`sudo singularity build expanse-uscdnt-golang.sif docker://caidaricky/expanse-uscdnt-golang:0.1`

## 3.3 Transfer the image to Expanse
You can use the Lustre storage on SDSC Expanse to store your image. 
For example, we uploaded the image we built to this project's folder.
`scp expanse-uscdnt-golang.sif expanse:/expanse/lustre/projects/csd939/kmok/shared_data/`

## Step 4. Execute the singularity image
Similar to FlowTuple batch analysis, we use slurm to schedule the execution of the image. We prepared a sample script (`slurm_scipts/container-1x8_8G-batch-debug.slurm` ). To schedule this job, run
`sbatch container-1x8_8G-batch-debug.slurm`
After the job is executed, you will be able to find the results in the output directory.
`/expanse/lustre/projects/csd939/<your username>/golang_container_output`