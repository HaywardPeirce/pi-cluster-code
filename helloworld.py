from mpi4py import MPI

#get the total number of processes
size = MPI.COMM_WORLD.Get_size()

#get what process number this is
rank = MPI.COMM_WORLD.Get_rank()

#get the name of the processor running this process
name = MPI.Get_processor_name()

print("Hello, World! I am process {} of {} on {}.\n".format(rank, size, name))