import propar
import time

db = propar.database()

n = 200
print()
print("propar database performance test")
print()
print("testing with n =", n)
print()

bt = time.perf_counter()
for i in range(n):
  db.get_all_parameters()
et = time.perf_counter()
print("{:<50}{:>8}".format("get_all_parameters"                              , '{:3.2f}ns'.format((et-bt) / n * 1000000               )))

dde_nrs        = []
all_parameters = db.get_all_parameters()
for p in all_parameters:
  dde_nrs.append(p['dde_nr'])

bt = time.perf_counter()
for i in range(n):
  for dde_nr in dde_nrs:
    db.get_parameter(dde_nr)
et = time.perf_counter()
print("{:<50}{:>8}".format("get_parameter for all dde_nrs"                   , '{:3.2f}ns'.format((et-bt) / n * 1000000               )))
print("{:<50}{:>8}".format("get_parameter one parameter (average)"           , '{:3.2f}ns'.format((et-bt) / n * 1000000 / len(dde_nrs))))

bt = time.perf_counter()
for i in range(n):
  db.get_parameters_like('fieldbus')
et = time.perf_counter()
print("{:<50}{:>8}".format("get_parameters_like('fieldbus')"                  , '{:3.2f}ns'.format((et-bt) / n * 1000000               )))

bt = time.perf_counter()
for i in range(n):
  for p in all_parameters:
    db.get_propar_parameter(p['proc_nr'], p['parm_nr'])
et = time.perf_counter()
print("{:<50}{:>8}".format("get_propar_parameter for all parmeters"          , '{:3.2f}ns'.format((et-bt) / n * 1000000               )))
print("{:<50}{:>8}".format("get_propar_parameter for one parameter (average)", '{:3.2f}ns'.format((et-bt) / n * 1000000 / len(dde_nrs))))

print()