import propar
import time


db = propar.database()

dde_nrs = []

bt = time.perf_counter()
for i in range(1000):
  db.get_all_parameters()
et = time.perf_counter()
print("get_all_parameters:", (et-bt) / 1000)

all_parameters = db.get_all_parameters()
for p in all_parameters:
  dde_nrs.append(p['dde_nr'])

bt = time.perf_counter()
for i in range(1000):
  for dde_nr in dde_nrs:
    db.get_parameter(dde_nr)
et = time.perf_counter()
print("get_parameter for all dde_nrs", (et-bt) / 1000)

bt = time.perf_counter()
for i in range(1000):
  db.get_parameters_like('fieldbus')
et = time.perf_counter()
print("get_parameters_like('fieldbus')", (et-bt) / 1000)

bt = time.perf_counter()
for i in range(1000):
  for p in all_parameters:
    db.get_propar_parameter(p['proc_nr'], p['parm_nr'])
et = time.perf_counter()
print("get_propar_parameter for all parmeters", (et-bt) / 1000)