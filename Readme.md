# Pfeiffer MaxiGauge
pytango device server to communicate with a Pfeiffer MaxiGauge TPG366

## Installation
requires pyvisa

## Configuration
Only device property is the serial port. It's inserted in the following pyvisa
device string:

`f'ASRL::{serial_port}::INSTR'`

## Authors
M. Schneider, MBI Berlin
