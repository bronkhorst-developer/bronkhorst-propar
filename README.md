# Bronkhorst Propar

The Bronkhorst Propar module provides an implementation of a propar master for communication with Bronkhorst (Mass) Flow Meters and Controllers (such as the EL-Flow, ES-Flow, (mini) CORI-FLOW, IQ+FLOW, and others), Pressure Meters and Controllers (EL-PRESS), and others using the default RS232/RS485 interface.

Using the Bronkhorst Propar module it is possible to directly communicate with a single instrument, or to multiple instruments when they are connected to a FLOW-BUS network. The Bronkhorst Propar module communicates directly with the instruments using Python, and does not require tools such as FlowDDE to be installed. Therefore the module is platform independent and has been tested on both Windows and Linux (the module depends on pyserial for serial communication and should work on all platforms that support it).

![Gas Flow](https://www.bronkhorst.com/getmedia/c91cbf1b-7192-4672-8d50-8aa5a7e3afbe/gas-flow.png "Gas Flow") ![Liquid Flow](https://www.bronkhorst.com/getmedia/3d742400-c9e8-418b-a940-8cb8177a7d57/liquid-flow-uc.png "Liquid Flow") ![Pressure](https://www.bronkhorst.com/getmedia/05212869-5b3f-45ac-ab24-bb1f1d9ccb9e/pressure.png "Pressure")

## Parameters

For a list of common parameters and the associated functionality available on Bronkhorst instruments, please consult document: [9.17.023 - Operating instructions for digital instruments](https://www.bronkhorst.com/getmedia/ad6a26ef-e33f-4424-b375-21d5811e3b04/917023-Manual-operation-instructions-digital-instruments).
For a full list of parameters across most Bronkhorst instruments, as well as technical information about the propar protocol, please consult document: [9.17.0.27 - RS232 interface with ProPar protocol](https://www.bronkhorst.com/getmedia/77a1438f-e547-4a79-95ad-53e81fd38a97/917027-Manual-RS232-interface).

## Installation
```pip install bronkhorst-propar```

## Documentation
https://bronkhorst-propar.readthedocs.io/