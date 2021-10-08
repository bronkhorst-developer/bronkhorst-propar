# Bronkhorst Propar

The Bronkhorst Propar module provides an implementation of a propar master for communication with Bronkhorst (Mass) Flow Meters and Controllers (such as the EL-Flow, ES-Flow, (mini) CORI-FLOW, IQ+FLOW, and others), Pressure Meters and Controllers (EL-PRESS), and others using the default RS232/RS485 interface.

Using the Bronkhorst Propar module it is possible to directly communicate with a single instrument, or to multiple instruments when they are connected to a FLOW-BUS network. The Bronkhorst Propar module communicates directly with the instruments using Python, and does not require tools such as FlowDDE to be installed. Therefore the module is platform independent and has been tested on both Windows and Linux (the module depends on pyserial for serial communication and should work on all platforms that support it).

![Gas Flow](https://github.com/bronkhorst-developer/bronkhorst-propar/raw/master/docs/img/gas-flow.png "Gas Flow") ![Liquid Flow](https://github.com/bronkhorst-developer/bronkhorst-propar/raw/master/docs/img/liquid-flow-uc.png "Liquid Flow") ![Pressure](https://github.com/bronkhorst-developer/bronkhorst-propar/raw/master/docs/img/pressure.png "Pressure")

## Installation

```pip install bronkhorst-propar```

## Documentation

[bronkhorst-propar on Read the Docs](https://bronkhorst-propar.readthedocs.io/en/latest/introduction.html)

## Contact

If you have any questions about this module, our other products or services you can contact us by:

- email: info@bronkhorst.com
- website: www.bronkhorst.com
- phone: +31 573 45 88 00
- mail: Nijverheidsstraat 1A NL-7261 AK Ruurlo (The Netherlands)