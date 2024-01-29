#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of the PfeifferMaxigauge project
#
#
#
# Distributed under the terms of the MIT license.
# See LICENSE.txt for more info.

""" Pfeiffer Maxigauge

Reads the six pressure channels of a Pfeiffer Maxigauge controller.
"""

# PyTango imports
import tango
from tango import DebugIt
from tango.server import run
from tango.server import Device
from tango.server import attribute, command
from tango.server import device_property
from tango import AttrQuality, DispLevel, DevState
from tango import AttrWriteType, PipeWriteType
# Additional import
# PROTECTED REGION ID(PfeifferMaxigauge.additionnal_import) ENABLED START #
import pyvisa
from math import nan

ACK = "\x06"
NAK = "\x15"
ENQ = "\x05"
ETX = "\x03"

# PROTECTED REGION END #    //  PfeifferMaxigauge.additionnal_import

__all__ = ["PfeifferMaxigauge", "main"]

def hexformat(text):
    """Format text as hex character string"""
    hexstr = [f"{ord(s):02X}" for s in text]
    return " ".join(hexstr)


class PfeifferMaxigauge(Device):
    """
    Reads the six pressure channels of a Pfeiffer Maxigauge controller.

    **Properties:**

    - Device Property
        visa_resource
            - VISA resource name
            - Type:'DevString'
    """
    # PROTECTED REGION ID(PfeifferMaxigauge.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  PfeifferMaxigauge.class_variable

    # -----------------
    # Device Properties
    # -----------------

    visa_resource = device_property(
        dtype='DevString',
        default_value="/dev/ttyS0"
    )

    # ----------
    # Attributes
    # ----------

    pressure1 = attribute(
        dtype='DevDouble',
        format='8.3e',
    )

    pressure2 = attribute(
        dtype='DevDouble',
        format='8.3e',
    )

    pressure3 = attribute(
        dtype='DevDouble',
        format='8.3e',
    )

    pressure4 = attribute(
        dtype='DevDouble',
        format='8.3e',
    )

    pressure5 = attribute(
        dtype='DevDouble',
        format='8.3e',
    )

    pressure6 = attribute(
        dtype='DevDouble',
        format='8.3e',
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        """Initialises the attributes and properties of the PfeifferMaxigauge."""
        Device.init_device(self)
        # PROTECTED REGION ID(PfeifferMaxigauge.init_device) ENABLED START #
        self._pressure1 = 0.0
        self._pressure2 = 0.0
        self._pressure3 = 0.0
        self._pressure4 = 0.0
        self._pressure5 = 0.0
        self._pressure6 = 0.0
        self.rm = pyvisa.ResourceManager("@py")
        self.inst = self.rm.open_resource(f"ASRL/{self.visa_resource}::INSTR")
        self.inst.write_termination = '\r'
        self.inst.read_termination = '\r\n'
        self.inst.timeout = 1000
        self.set_state(DevState.ON)

        # PROTECTED REGION END #    //  PfeifferMaxigauge.init_device

    def always_executed_hook(self):
        """Method always executed before any TANGO command is executed."""
        # PROTECTED REGION ID(PfeifferMaxigauge.always_executed_hook) ENABLED START #
        # PROTECTED REGION END #    //  PfeifferMaxigauge.always_executed_hook

    def delete_device(self):
        """Hook to delete resources allocated in init_device.

        This method allows for any memory or other resources allocated in the
        init_device method to be released.  This method is called by the device
        destructor and by the device Init command.
        """
        # PROTECTED REGION ID(PfeifferMaxigauge.delete_device) ENABLED START #
        self.inst.close()
        self.rm.close()
        # PROTECTED REGION END #    //  PfeifferMaxigauge.delete_device
    # ------------------
    # Attributes methods
    # ------------------

    def read_pressure1(self):
        # PROTECTED REGION ID(PfeifferMaxigauge.pressure1_read) ENABLED START #
        """Return the pressure1 attribute."""
        return self.read_sensor(1)
        # PROTECTED REGION END #    //  PfeifferMaxigauge.pressure1_read

    def read_pressure2(self):
        # PROTECTED REGION ID(PfeifferMaxigauge.pressure2_read) ENABLED START #
        """Return the pressure2 attribute."""
        return self.read_sensor(2)
        # PROTECTED REGION END #    //  PfeifferMaxigauge.pressure2_read

    def read_pressure3(self):
        # PROTECTED REGION ID(PfeifferMaxigauge.pressure3_read) ENABLED START #
        """Return the pressure3 attribute."""
        return self.read_sensor(3)
        # PROTECTED REGION END #    //  PfeifferMaxigauge.pressure3_read

    def read_pressure4(self):
        # PROTECTED REGION ID(PfeifferMaxigauge.pressure4_read) ENABLED START #
        """Return the pressure4 attribute."""
        return self.read_sensor(4)
        # PROTECTED REGION END #    //  PfeifferMaxigauge.pressure4_read

    def read_pressure5(self):
        # PROTECTED REGION ID(PfeifferMaxigauge.pressure5_read) ENABLED START #
        """Return the pressure5 attribute."""
        return self.read_sensor(5)
        # PROTECTED REGION END #    //  PfeifferMaxigauge.pressure5_read

    def read_pressure6(self):
        # PROTECTED REGION ID(PfeifferMaxigauge.pressure6_read) ENABLED START #
        """Return the pressure6 attribute."""
        return self.read_sensor(6)
        # PROTECTED REGION END #    //  PfeifferMaxigauge.pressure6_read

    # --------
    # Commands
    # --------

    @command(
        dtype_in='DevLong64',
    )
    @DebugIt()
    def enable_sensor(self, argin):
        # PROTECTED REGION ID(PfeifferMaxigauge.enable_sensor) ENABLED START #
        """
        enable sensor number (1-6)

        :param argin: 'DevLong64'

        :return:None
        """
        mask = 6 * [0]
        mask[argin - 1] = 2
        mask_str = ','.join([str(d) for d in mask])
        self.query(f"SEN,{mask_str}")
        # PROTECTED REGION END #    //  PfeifferMaxigauge.enable_sensor

    @command(
        dtype_in='DevULong',
    )
    @DebugIt()
    def disable_sensor(self, argin):
        # PROTECTED REGION ID(PfeifferMaxigauge.disable_sensor) ENABLED START #
        """
        disable sensor number (1-6)

        :param argin: 'DevULong'

        :return:None
        """
        mask = 6 * [0]
        mask[argin - 1] = 1
        mask_str = ','.join([str(d) for d in mask])
        self.query(f"SEN,{mask_str}")
        # PROTECTED REGION END #    //  PfeifferMaxigauge.disable_sensor

    @command(
        dtype_in='DevString',
        dtype_out='DevString',
    )
    def query(self, argin):
        # PROTECTED REGION ID(PfeifferMaxigauge.query) ENABLED START #
        """
        send and receive strings

        :param argin: 'DevString'

        :return:'DevString'
        """
        self.debug_stream(f"query: {argin}")
        ans = self.inst.query(argin)
        ans_hex = hexformat(ans)
        self.debug_stream(f"reply: {ans} ({ans_hex})")
        reply = ''
        if ACK in ans:
            self.debug_stream(f"Received ACK, proceeding with ENQ")
            self.inst.write_raw(ENQ.encode())
            reply = self.inst.read()
            ans_hex = hexformat(reply)
            self.debug_stream(f"reply: {reply} ({ans_hex})")
        elif NAK in ans:
            self.error_stream(f"Query resulted in NAK: {argin}")
        else:
            self.error_stream(f"Did not receive ACK on message, got {ans_hex} instead")
        return reply

        # PROTECTED REGION END #    //  PfeifferMaxigauge.query

    @command(
        dtype_in='DevLong',
        dtype_out='DevDouble',
    )
    def read_sensor(self, argin):
        # PROTECTED REGION ID(PfeifferMaxigauge.read_sensor) ENABLED START #
        """
        return pressure for given sensor

        :param argin: 'DevLong'

        :return:None
        """
        ans = self.query(f"PR{argin}")
        try:
            status, pressure = ans.split(',')
            pressure = float(pressure)
        except Exception:
            pressure = nan
        return pressure
        # PROTECTED REGION END #    //  PfeifferMaxigauge.read_sensor

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    """Main function of the PfeifferMaxigauge module."""
    # PROTECTED REGION ID(PfeifferMaxigauge.main) ENABLED START #
    return run((PfeifferMaxigauge,), args=args, **kwargs)
    # PROTECTED REGION END #    //  PfeifferMaxigauge.main


if __name__ == '__main__':
    main()
