# Pfeiffer MaxiGauge
pytango device server to communicate with a Pfeiffer MaxiGauge TPG366

## Installation
requires pyvisa

## Configuration
Only device property is the serial port. It's inserted in the following pyvisa
device string:

`f'ASRL::{gpib_address}::INSTR'`

## Authors
M. Schneider, MBI Berlin
