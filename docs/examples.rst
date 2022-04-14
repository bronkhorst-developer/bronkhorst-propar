========
Examples
========

Connecting to a single instrument
---------------------------------

.. code:: python

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

Connecting to an instrument with multiple channels
--------------------------------------------------

Some instruments are a single node (one address) but contain multiple channels (for multiple sensors).
To connect to a specific channel, specify the channel when creating an instrument instance.
If no channel is specified the first channel will be used.

.. code:: python

    # Import the propar module
    import propar

    # Connect to an instrument by specifying the channel number to connect to
    flow = propar.instrument('COM1', channel=1)
    pressure = propar.instrument('COM1', channel=2)

    # Alternatively, pass channel to parameter functions
    instrument = propar.instrument('COM1')
    p_upstream = instrument.readParameter(205, channel=2)

Connecting to multiple instruments
---------------------------------- 

When instruments are connected to a FLOW-BUS network, the localhost function an instrument can be 
used to connect to other instruments on the network (by specifying the node address). 

.. code:: python

    # Import the propar module
    import propar

    # Connect to an instrument by specifying the instrument node address to connect to
    el_flow = propar.instrument('COM1', 3)
    cori_flow = propar.instrument('COM1', 4)
    es_flow   = propar.instrument('COM1', 5)

Custom baudrate
---------------

It is also possible to connect to an instrument with a different
baudrate than the default of 38400 baud. Note that it is only possible
to connect using the baudrate that is configured in the instrument.

.. code:: python

    # Import the propar module
    import propar

    # Connect to the local instrument, with a different baudrate than the default (38400)
    el_flow = propar.instrument('COM1', baudrate=115200)

Scanning for instruments
------------------------

To check all connected instruments on the network, the propar modules
master can be used. When creating an instrument on a specific com port,
a propar master is automatically created for that comport. Using the
get\_nodes function of the master, a list of all nodes on the network is
collected and returned. This list can be used to check if all expected
instruments are connected, or to get an overview of your network.

The nodes list will also include the number of channels that are present
on that device. Use this in combination with the channel functionality
to create instances of each device and for the seperate device channels.

.. code:: python

    # Import the propar module
    import propar

    # Connect to the local instrument.
    el_flow = propar.instrument('COM1')

    # Use the get_nodes function of the master of the instrument to get a list of instruments on the network
    nodes = el_flow.master.get_nodes()

    # Display the list of nodes
    for node in nodes:
      print(node)

Using a master
--------------

It is also possible to only create a master. This removes some
abstraction offered by the instrument class, such as the setpoint and
measure properties, the readParameter and writeParameter functions, and
having to supply the node number on each read/write parameter call.

.. code:: python

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

Chaining
--------

Finally the propar module offers the possibility of using the chaining
mechanism of the propar protocol to read or write multiple parameters
using a single propar message. This is advanced functionality and has
some downsides, especially when it comes to error handling. As the
read\_parameters and write\_parameters functions do not return True or
False to indicate success, but instead rely on the underlying propar
status codes to indicate the result of the action.

.. code:: python

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

Database
--------

To easily generate a list of parameters for use with chaining, and the
read\_parameters and write\_parameters functions, the propar database
can be used. This component is automatically available on all instrument
instances or can be instantiated separately.

.. code:: python

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

Custom serial class
-------------------

To use a custom serial data provider (instead of pySerial), the
serial\_class can be passed to the instrument and master classes.

.. code:: python

    # Import the propar module
    import propar

    # A dummy serial port class with the required functions and attributes.
    class dummy_serial():

      def __init__(self, port, baudrate, **kwargs):
        # Initialize the port, port and baudrate can be controlled
        # in instrument and master initialization.
        print(port, baudrate)

      def close(self):
        # Close the port
        print('close')

      def open(self):
        # Open the port
        print('open')

      def read(self, size=1):
        # Read data from port, return bytes object
        return b'dummy'

      def write(self, data):
        # Write data to port, bytes object as input
        print(data)

      @property
      def in_waiting(self):
        # Return number of bytes available for reading
        return 5

    # Instrument instance with dummy serial port.
    dut = propar.instrument('dummy_port', serial_class=dummy_serial)