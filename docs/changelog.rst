=========
Changelog
=========

1.1.0
-----

-  Updated parameter database.
-  Updated examples.

1.0.2
-----

-  Fix install from .tar.gz package.

1.0.1
-----

-  Updated parameter database.

1.0.0
-----

-  Updated parameter database.
-  Add support for devices with multiple channels.
-  Add support for automatically reopening serial port.
-  Add support for callback on read and write parameters of instrument instances.
-  Update string handling.

0.5.5
-----

-  Fix database json loading using deprecated keyword encoding.

0.5.4
-----

-  Add support for externally provides serial class, this enables
   solutions that do not use a pySerial compatible serial port. The
   given serial class must support in\_waiting, read, write, open,
   close.
-  Fix issue that write would modify parameter type of passed
   parameters.

0.5.3
-----

-  Fix issues with write chaining.
-  Support receiving strings that exceed MAX\_PP\_PARM\_LEN.

0.5.2
-----

-  Add IP Address parameters to database.
-  Added mechanism to reduce CPU load with the new serial port handling.

0.5.1
-----

-  Fixed dump mode (broken due to new serial port handling).
-  Fixed bug in string handling.
-  Return parameters now contain the requested type when they are custom
   types (PP\_TYPE\_FLOAT, PP\_TYPE\_SINT16, PP\_TYPE\_BSINT16).
-  Changed database to return copy of dict, so modifcations to a
   parameter won't influence 'new' request of that parameter.

0.5.0
-----

-  Added support for propar broadcast messages (using
   ``master.broadcast_callback``).
-  Improved database performance upto 400 times.
-  Data will now be read from serial port in chunks, when there is more
   data available. This speeds up the processing and keeps buffers
   clear.
-  Support for unchained multiple parameter propar read messages.

0.4.0
-----

-  Added ``__version__`` attribute.
-  Added ``dde_nr`` and ``parm_name`` fields to output parameters of
   ``read_parameters``, when they are present in the request parameters.
-  Added experimental support for Propar ASCII. Can be enabled with
   ``master.propar.mode = propar.PP_MODE_ASCII`` (mode is set to
   ``propar.PP_MODE_BINARY`` by default).
-  Changed formatting for debug messages to: ``TX/RX (Length): Data``.
-  Fixed bug in reading strings from response message (in a chained
   read).
-  Fixed bug in request/response matching where when re-using a master
   after aborting a running action (for example CTRL+C in an interactive
   python session), sometimes the old response to that action would
   match the new request.

0.3.4
-----

-  Reduced CPU load (set timeout of serial port in propar provider).

0.3.3
-----

-  Fixed issue with matching requests to responses in master. Improved
   compatibility for ``master.get_nodes``.

0.3.2
-----

-  Changed debug message to only show when flag is set.

0.3.1
-----

-  Compatibility improved in ``master.get_nodes`` function on propar
   master.

0.3.0
-----

-  Improved propar performance, added additional dump mode.

0.2.3
-----

-  Fix some errors in the project description and examples.

0.2.1
-----

-  Initial public release.