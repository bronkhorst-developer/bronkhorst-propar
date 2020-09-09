# test serial injection functionality for special customer functionality
# for example Pressure Control Solutions which use modbus tcp to serial converter, but want to use the bronkhorst-propar package.

# To use serial injection provide a serial class with at least the folowing functions:
# __init__(self, comport, baudrate)
# open()
# close()
# read(nr_of_bytes=1)
# write(bytes_to_write)
# .in_waiting = nr of bytes in receive buffer.

import propar

import random
import string

class dummy_serial():
  def __init__(self, port, baudrate, **kwargs):
    print(f'dummy serial on port {port} with baudrate {baudrate}')
    self.read_data = None

  def close(self):
    print('dummy serial close')

  def open(self):
    print('dummy serial close')
    
  @property
  def in_waiting(self):
    if self.read_data:
      return len(self.read_data)
    else:
      return 0

  def read(self, size=1):
    """
      return a bytes object.
    """
    #print(f'dummy serial read {size} bytes')
    # If we have a dummy response, give the answer
    if self.read_data:
      retval = self.read_data
      self.read_data = None
      return retval
    else:
      return b''
    
  def write(self, data):
    #print(f'dummy serial write {data}')

    # Check if it is a read for serial number
    if b'\x80\x06\x04\x71\x63\x71\x63\x00\x10\x03' in data:
      # Copy start and sequence number from resquest to response
      self.read_data = data[:3]
      if data[2] == 0x10:
        self.read_data = data[:4]
      self.read_data += b'\x80\x0F\x02\x71\x63\x00'
     
      # Generate random serial number to check for correct functionality
      self.serial_number = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

      self.read_data += self.serial_number.encode('ascii')
      self.read_data += b'\x00\x10\x03'

    return len(data)

dut = propar.instrument('dummy_serial', serial_class=dummy_serial)

for i in range(20):
  serial = dut.readParameter(92)
  if serial == dut.master.propar.serial.serial_number:
    print('Ok!', serial)
  else:
    print('Error!', serial, '!=', dut.master.propar.serial.serial_number)
