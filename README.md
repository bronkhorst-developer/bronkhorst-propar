# Bronkhorst Propar

The Bronkhorst Propar module provides an implementation of a propar master for communication with Bronkhorst (Mass) Flow Meters and Controllers (such as the EL-Flow, ES-Flow, (mini) CORI-FLOW, IQ+FLOW, and others), Pressure Meters and Controllers (EL-PRESS), and others using the default RS232/RS485 interface.

Using the Bronkhorst Propar module it is possible to directly communicate with a single instrument, or to multiple instruments when they are connected to a FLOW-BUS network. The Bronkhorst Propar module communicates directly with the instruments using Python, and does not require tools such as FlowDDE to be installed. Therefore the module is platform independent and has been tested on both Windows and Linux (the module depends on pyserial for serial communication and should work on all platforms that support it).

![Gas Flow](https://www.bronkhorst.com/getmedia/c91cbf1b-7192-4672-8d50-8aa5a7e3afbe/gas-flow.png "Gas Flow") ![Liquid Flow](https://www.bronkhorst.com/getmedia/3d742400-c9e8-418b-a940-8cb8177a7d57/liquid-flow-uc.png "Liquid Flow") ![Pressure](https://www.bronkhorst.com/getmedia/05212869-5b3f-45ac-ab24-bb1f1d9ccb9e/pressure.png "Pressure")

## Parameters

For a list of common parameters and the associated functionality available on Bronkhorst instruments, please consult document: [9.17.023 - Operating instructions for digital instruments](https://www.bronkhorst.com/getmedia/ad6a26ef-e33f-4424-b375-21d5811e3b04/917023-Manual-operation-instructions-digital-instruments).
For a full list of parameters across most Bronkhorst instruments, as well as technical information about the propar protocol, please consult document: [9.17.0.27 - RS232 interface with ProPar protocol](https://www.bronkhorst.com/getmedia/77a1438f-e547-4a79-95ad-53e81fd38a97/917027-Manual-RS232-interface).

## Examples

Connecting to a single instrument.

```python
# Import the propar module
import propar

# Connect to the local instrument, when no settings provided
# defaults to locally connected instrument (address=0x80, baudrate=38400)
el_flow = propar.instrument('COM1')

# The setpoint and measure parameters are available
# as properties, for ease of use.
el_flow.setpoint = 16000
print(el_flow.measure)
el_flow.setpoint = 0

# All parameters can be read using the process and parameter numbers,
# as well as the parameters data type.
el_flow.read(1, 1, propar.PP_TYPE_INT16)

# Most parameters can also be read by their FlowDDE number,
# for example the user tag parameter.
el_flow.writeParameter(115, "Hello World!")
print(el_flow.readParameter(115))
```

Connecting to multiple instruments on the FLOW-BUS using the instruments localhost functionality.

```python
# Import the propar module
import propar

# Connect to an instrument, however as there are multiple instruments
# we now supply the instrument node number to connect to a specific instrument.
el_flow = propar.instrument('COM1', 3)

# Now connect to other instruments via the same instrument localhost (same serial port)
cori_flow = propar.instrument('COM1', 4)
es_flow   = propar.instrument('COM1', 5)
```

It is also possible to connect to an instrument with a different baudrate than the default of 38400 baud. Note that it is only possible to connect using the baudrate that is configured in the instrument.

```python
# Import the propar module
import propar

# Connect to the local instrument, with a different baudrate than the default (38400)
el_flow = propar.instrument('COM1', baudrate=115200)
```

To check all connected instruments on the network, the propar modules master can be used. When creating an instrument on a specific com port, a propar master is automatically created for that comport. Using the get_nodes function of the master, a list of all nodes on the network is collected and returned. This list can be used to check if all expected instruments are connected, or to get an overview of your network.

```python
# Import the propar module
import propar

# Connect to the local instrument.
el_flow = propar.instrument('COM1')

# Use the get_nodes function of the master of the instrument to get a list of instruments on the network
nodes = el_flow.master.get_nodes()

# Display the list of nodes
for node in nodes:
  print(node)
```

It is also possible to only create a master. This removes some abstraction offered by the instrument class, such as the setpoint and measure properties, the readParameter and writeParameter functions, and having to supply the node number on each read/write parameter call.

```python
# Import the propar module
import propar

# Create the master
master = propar.master('COM1', 38400)

# Get nodes on the network
nodes = master.get_nodes()

# Read the usertag of all nodes
for node in nodes:
  user_tag = master.read(node['address'], 113, 6, propar.PP_TYPE_STRING)
  print(user_tag)
```

Finally the propar module offers the possibility of using the chaining mechanism of the propar protocol to read or write multiple parameters using a single propar message. This is advanced functionality and has some downsides, especially when it comes to error handling. As the read_parameters and write_parameters functions do not return True or False to indicate success, but instead rely on the underlying propar status codes to indicate the result of the action.

```python
# Import the propar module
import propar

# Connect to the local instrument.
el_flow = propar.instrument('COM1')

# Prepare a list of parameters for a chained read containing:
# fmeasure, fsetpoint, temperature, valve output
params = [{'proc_nr':  33, 'parm_nr': 0, 'parm_type': propar.PP_TYPE_FLOAT},
          {'proc_nr':  33, 'parm_nr': 3, 'parm_type': propar.PP_TYPE_FLOAT},
          {'proc_nr':  33, 'parm_nr': 7, 'parm_type': propar.PP_TYPE_FLOAT},
          {'proc_nr': 114, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT32}]

# Note that this uses the read_parameters function.
values = el_flow.read_parameters(params)

# Display the values returned by the read_parameters function. A single 'value' includes
# the original fields of the parameters supplied to the request, with the data stored in
# the value['data'] field.
for value in values:
  print(value)

# For writes the parameter must have the 'data' field set with the value to write when
# passing it to the write_parameters function.
params = [{'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16, 'data': 32000}]

# Write parameters returns a propar status code.
status = el_flow.write_parameters(params)

# Also, note that when using the master directly the address of the node must be set in the
# parameter object that is passed to the read_parameters or write_parameters function
params = [{'node': 3, 'proc_nr': 1, 'parm_nr': 1, 'parm_type': propar.PP_TYPE_INT16}]

# Read from the master directly
values = el_flow.master.read_parameters(params)
```

To easily generate a list of parameters for use with chaining, and the read_parameters and write_parameters functions, the propar database can be used. This component is automatically available on all instrument instances or can be instantiated separately.

```python
# Import the propar module
import propar

# Create a database instance
db = propar.database()

# or access the instruments database instance
el_flow = propar.instrument('COM1')
db      = el_flow.db

# Get parameter objects for chained read (read_parameters) from list of FlowDDE numbers
parameters = db.get_parameters([8, 9, 11, 142])

# Get a single parameter object
setpoint = db.get_parameter(8)

# It is also possible to search the database, using the string name of the parameter
valve_parameters = db.get_parameters_like('valve')
```

## Data Types

The data types available in the propar module are:

* PP_TYPE_INT8  (unsigned char)
* PP_TYPE_INT16 (unsigned int)
* PP_TYPE_SINT16 (signed int, -32767 - 32767)
* PP_TYPE_BSINT16 (signed int, -23593 - 41942)
* PP_TYPE_INT32 (unsigned long)
* PP_TYPE_FLOAT (float)
* PP_TYPE_STRING (string)

These types are automatically converted to data types in the propar protocol, which only supports four basic data types:

* 1 byte value (char, unsigned char)
* 2 byte value (unsigned int, signed int, custom signed int)
* 4 byte value (float, unsigned long, long)
* n byte value (string, char array)

When propar module data types are used, the module will perform the required conversion for the specific data type. When using the readParameter and writeParameter functions, the conversion between database parameter type to the customized parameter type is performed automatically (based on the type, and the minimal specified value).

## Changelog

### 0.5.2

* Add IP Address parameters to database.
* Added mechanism to reduce CPU load with the new serial port handling.
* Add basic usage counting, should automatically stop and start master serial ports.
  
### 0.5.1

* Fixed dump mode (broken due to new serial port handling).
* Fixed bug in string handling.
* Return parameters now contain the requested type when they are custom types (PP_TYPE_FLOAT, PP_TYPE_SINT16, PP_TYPE_BSINT16).
* Changed database to return copy of dict, so modifcations to a parameter won't influence 'new' request of that parameter.

### 0.5.0

* Added support for propar broadcast messages (using ```master.broadcast_callback```).
* Improved database performance upto ~400 times.
* Data will now be read from serial port in chunks, when there is more data available. This speeds up the processing and keeps buffers clear.
* Support for unchained multiple parameter propar read messages.

### 0.4.0

* Added ```__version__``` attribute.
* Added ```dde_nr``` and ```parm_name``` fields to output parameters of ```read_parameters```, when they are present in the request parameters.
* Added experimental support for Propar ASCII. Can be enabled with ```master.propar.mode = propar.PP_MODE_ASCII``` (mode is set to ```propar.PP_MODE_BINARY``` by default).
* Changed formatting for debug messages to: ```TX/RX (Length): Data```.
* Fixed bug in reading strings from response message (in a chained read).
* Fixed bug in request/response matching where when re-using a master after aborting a running action (for example CTRL+C in an interactive python session), sometimes the old response to that action would match the new request.

### 0.3.4

* Reduced CPU load (set timeout of serial port in propar provider).

### 0.3.3

* Fixed issue with matching requests to responses in master. Improved compatibility for ```master.get_nodes```.

### 0.3.2

* Changed debug message to only show when flag is set.

### 0.3.1

* Compatibility improved in ```master.get_nodes``` function on propar master.

### 0.3.0

* Improved propar performance, added additional dump mode.
  
### 0.2.3

* Fix some errors in the project description and examples.

### 0.2.1

* Initial public release.
