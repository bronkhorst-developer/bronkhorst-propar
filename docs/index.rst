Welcome to bronkhorst-propar documentation
=============================================

The Bronkhorst propar module provides an implementation of a propar master for communication with 
Bronkhorst (Mass) Flow Meters and Controllers (such as the EL-Flow, ES-Flow, (mini) CORI-FLOW, IQ+FLOW, and others), 
Pressure Meters and Controllers (EL-PRESS), and others using the default RS232/RS485 interface.

Using the Bronkhorst propar module it is possible to directly communicate with a single instrument, 
or to multiple instruments when they are connected to a FLOW-BUS network. The Bronkhorst propar module 
communicates directly with the instruments using Python, and does not require tools such as FlowDDE to be installed. 
Therefore the module is platform independent and has been tested on both Windows and Linux 
(the module depends on pyserial for serial communication and should work on all platforms that support it).

.. image::/img/flexi-flow.png
  :alt: Gas Flow and Pressure
  
.. image::/img/gas-flow.png
  :alt: Gas Flow

.. image::/img/liquid-flow-uc.png
  :alt: Liquid Flow

.. image::/img/pressure.png
  :alt: Pressure


Contents:

.. toctree::
   :maxdepth: 2
   
   introduction
   examples   
   propar
   changelog
   contact


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
