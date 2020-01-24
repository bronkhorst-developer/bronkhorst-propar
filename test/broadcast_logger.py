import propar
import time
import random 
from datetime import datetime

dut = propar.instrument('com5')

# Get log file name with timestamp
dump_file_name = datetime.now().strftime('%Y%m%d_%H%M%S_MEMS_Dump.csv')

# Callback function for receiving the broadcast dump data
first = True
def broadcast_receive(parms):
  global first  
  t = time.perf_counter() # gets highest resolution timestamp
  with open(dump_file_name, 'a') as f:
    if first: # Log header
      data = 'Time;' + ';'.join([str(p['parm_name']).replace(' ', '_') for p in parms]) + '\n'            
      first = False
    else:     # Log data
      data = str(t) + ';' + ';'.join([str(p['data']) for p in parms]) + '\n'    
    f.write(data)

# Set the callback to log broadcast data
dut.master.broadcast_callback = broadcast_receive

# Start the dump / broadcast
dut.writeParameter(7, 64)
dut.writeParameter(328, 460800)
dut.writeParameter(104, 1)
dut.master.set_baudrate(460800)

# get parameter object for setpoint, we need this to call write_parameters, where we can write without ack
parm_setpoint = dut.db.get_parameter(9)

# Main scipt.
while True:
  time.sleep(1)  
  # write new setpoint without ack
  parm_setpoint['data'] = random.randint(0, 32001)
  dut.write_parameters([parm_setpoint], command=propar.PP_COMMAND_SEND_PARM)  

