#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1

module load mpi4py/3.0.2-timed-pingpong

mpiexec -np 1 python main.py

my-job-stats -a -n -s

