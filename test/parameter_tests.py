import propar
import time
import random 

dut = propar.instrument('com5', baudrate=460800)

print()
print("Testing using propar @", propar.__file__)
print()

n = 10

all_parameters = dut.db.get_all_parameters()
bt = time.perf_counter()
for i in range(n):
  for p in all_parameters:
    dut.read_parameters([p])  
et = time.perf_counter()

print("{:<20}{:>8}".format("read all parameters", (et - bt)                       / n))
print("{:<20}{:>8}".format("read one parameter ", (et - bt) / len(all_parameters) / n))