import propar
import time
from datetime import datetime

dut = propar.instrument('com1')

# Get log file name with timestamp
dump_file_name = datetime.now().strftime('%Y%m%d_%H%M%S_Dump.csv')

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

# Main scipt.
while True:
  time.sleep(1)  

