import propar

dut = propar.instrument('com1')

parms = [{'proc_nr': 97, 'parm_nr': 1, 'parm_type': 32, 'data': 2000, 'parm_name': 'Alarm limit maximum'}, 
         {'proc_nr': 97, 'parm_nr': 2, 'parm_type': 32, 'data': 3000, 'parm_name': 'Alarm limit minimum'},
         {'proc_nr': 97, 'parm_nr': 3, 'parm_type':  0, 'data':    1, 'parm_name': 'Alarm mode'}, 
         {'proc_nr': 97, 'parm_nr': 5, 'parm_type':  0, 'data':    1, 'parm_name': 'Alarm setpoint mode'},
         {'proc_nr': 97, 'parm_nr': 6, 'parm_type': 32, 'data': 4000, 'parm_name': 'Alarm new setpoint'}, 
         {'proc_nr': 97, 'parm_nr': 9, 'parm_type':  0, 'data':   16, 'parm_name': 'Reset alarm enable'},
         {'proc_nr': 97, 'parm_nr': 7, 'parm_type':  0, 'data':   60, 'parm_name': 'Alarm delay'},
         {'proc_nr':  1, 'parm_nr': 1, 'parm_type': 32, 'data': 7000, 'parm_name': 'Setpoint'},
         {'proc_nr':  1, 'parm_nr': 2, 'parm_type': 32, 'data': 8000, 'parm_name': 'Setpoint Slope'},
         {'proc_nr':  1, 'parm_nr': 4, 'parm_type':  0, 'data':    9, 'parm_name': 'Control Mode'},
         {'proc_nr': 33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT, 'data': 0.10, 'parm_name': 'fSetpoint'}]

#dut.writeParameter(7, 64)

dut.master.propar.debug = True

print('\n================================================')
for p in parms: print(p['parm_name'], p['parm_type'])

z = dut.write_parameters(parms)
print('\n================================================')
print(z)

print('\n================================================')
for p in parms: print(p['parm_name'], p['parm_type'])

resp = dut.read_parameters(parms)

print('\n================================================')
for p in resp: print(p['parm_name'], p['parm_type'], p['data'])
