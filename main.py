from Utils import integration, output_print
from WorkUnit import WorkUnit
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

work_unit = WorkUnit(rank, size, "language.json", "sydGrid.json")


if rank == 0:
    my_grids = work_unit.process_data("bigTwitter.json")
    for task in range(1, size):
        other_grids = comm.recv(source=task)
        integration(my_grids, other_grids)
    output_print(my_grids)
else:
    my_grids = work_unit.process_data("bigTwitter.json")
    comm.send(my_grids, dest=0)
