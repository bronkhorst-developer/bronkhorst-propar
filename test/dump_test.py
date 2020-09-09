import propar
import time

dut = propar.instrument('com1')

dut.master.dump(2)

while True:
  time.sleep(1)
  v = dut.readParameter(11)
  #print(v)