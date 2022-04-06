from Utils import integration, output_print
from WorkUnit import WorkUnit
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# initialise the WorkUnit for current process
work_unit = WorkUnit(rank, size, "language.json", "sydGrid.json")

# if process is rank 0, the process is responsible 
# for aggregating the final result from other processes
if rank == 0:
    my_grids = work_unit.process_data("bigTwitter.json")
    # receive result from other processes
    for task in range(1, size):
        other_grids = comm.recv(source=task)
        integration(my_grids, other_grids)
    output_print(my_grids)
else:
    my_grids = work_unit.process_data("bigTwitter.json")
    # sent result to the process rank 0
    comm.send(my_grids, dest=0)
