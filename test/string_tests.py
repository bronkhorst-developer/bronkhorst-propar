import propar

dut = propar.instrument('com5')

parms = [p for p in dut.db.get_all_parameters() if p['parm_type'] == propar.PP_TYPE_STRING]

valid = []

for p in parms:
  res = dut.read_parameters([p])[0]
  if res['status'] == propar.PP_STATUS_OK:
    valid.append(p)
    print('{:<40}{:}'.format(res['parm_name'], res['data']))    


print()
print()

resp = dut.read_parameters(valid[6:12])
if resp[0]['status'] == propar.PP_STATUS_OK:
  for res in resp:
    print('{:<40}{:}'.format(res['parm_name'], res['data']))


print()
print()

p = valid[10:12]
p[1]['parm_size'] = 6

resp = dut.read_parameters(p)
if resp[0]['status'] == propar.PP_STATUS_OK:
  for res in resp:
    print(res)
    #print('{:<40}{:}'.format(res['parm_name'], res['data']))

