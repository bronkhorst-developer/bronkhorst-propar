====================
 Introduction
====================

The Bronkhorst propar module provides an implementation of a propar
master for communication with Bronkhorst (Mass) Flow Meters and
Controllers (such as the FLEXI-FLOW, EL-FLOW, ES-FLOW, (mini) CORI-FLOW, IQ+FLOW,
and others), Pressure Meters and Controllers (EL-PRESS), and others
using the default USB/RS232/RS485 interface.

Using the Bronkhorst propar module it is possible to directly
communicate with a single instrument, or to multiple instruments when
they are connected to a FLOW-BUS network. The Bronkhorst propar module
communicates directly with the instruments using Python, and does not
require tools such as FlowDDE to be installed. Therefore the module is
platform independent and has been tested on both Windows and Linux (the
module depends on pyserial for serial communication and should work on
all platforms that support it).

|Gas Flow and Pressure| |Gas Flow| |Liquid Flow| |Pressure|

.. |Gas Flow and Pressure| image:: /img/flexi-flow.png
    :width: 225
.. |Gas Flow| image:: /img/gas-flow.png
    :width: 225
.. |Liquid Flow| image:: /img/liquid-flow-uc.png
    :width: 225
.. |Pressure| image:: /img/pressure.png
    :width: 225

Parameters
----------

For a list of common parameters and the associated functionality
available on Bronkhorst instruments, please consult document: 
`9.17.023 - Operating instructions for digital instruments 
<https://www.bronkhorst.com/getmedia/ad6a26ef-e33f-4424-b375-21d5811e3b04/917023-Manual-operation-instructions-digital-instruments>`__.

For a full list of parameters across most Bronkhorst instruments, as
well as technical information about the propar protocol, please consult
document: `9.17.0.27 - RS232 interface with propar protocol 
<https://www.bronkhorst.com/getmedia/77a1438f-e547-4a79-95ad-53e81fd38a97/917027-Manual-RS232-interface>`__.


Data Types
----------

The data types available in the propar module are:

-  PP\_TYPE\_INT8 (unsigned char)
-  PP\_TYPE\_INT16 (unsigned int)
-  PP\_TYPE\_SINT16 (signed int, -32767...32767)
-  PP\_TYPE\_BSINT16 (signed int, -23593...41942)
-  PP\_TYPE\_INT32 (unsigned long)
-  PP\_TYPE\_FLOAT (float)
-  PP\_TYPE\_STRING (string)

These types are automatically converted to data types in the propar
protocol, which only supports four basic data types:

-  1 byte value (char, unsigned char)
-  2 byte value (unsigned int, signed int, custom signed int)
-  4 byte value (float, unsigned long, long)
-  n byte value (string, char array)

When propar module data types are used, the module will perform the
required conversion for the specific data type. When using the
readParameter and writeParameter functions, the conversion between
database parameter type to the customized parameter type is performed
automatically (based on the type, and the minimal specified value).
