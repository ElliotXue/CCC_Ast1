#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4

module load mpi4py/3.0.2-timed-pingpong

mpiexec -np 8 python main.py

my-job-stats -a -n -s

