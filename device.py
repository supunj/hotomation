#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 17:13:00 2021

@author: Supun Jayathilake
"""

import tinytuya
import sys
from datetime import *


class Device:
    def __init__(self, device):
        self.index = device.device
        self.type = device.type
        self.name = device.name
        self.brand = device.brand
        self.version = device.version
        self.id = device.id
        self.ip = device.ip
        self.device_state = None
        self.current_time = datetime.now().time().strftime("%H:%M")

    def evaluate(self):
        print("No evaluate() implementation!")


class Switch:
    def __init__(self, switch, state):
        self.number = switch.switch
        self.on = None if not hasattr(switch, 'on') else switch.on
        self.off = None if not hasattr(switch, 'off') else switch.off
        self.random = False if not hasattr(switch, 'random') else switch.random
        self.switch_state = state


class TuyaDevice(Device):
    def __init__(self, device):
        Device.__init__(self, device)
        self.key = device.key
        self.dev = tinytuya.OutletDevice(self.id, self.ip, self.key)
        self.dev.set_version(self.version)


class SonoffDevice(Device):
    def __init__(self, device):
        Device.__init__(self, device)


class TuyaSwitch(TuyaDevice, Switch):
    def __init__(self, device, switch):
        TuyaDevice.__init__(self, device)
        Switch.__init__(self, switch, self.dev.status()
                        ['dps'][str(switch.switch)])

    def switch_on(self):
        self.dev.set_status(True, self.number)
        self.refresh()
        return

    def switch_off(self):
        self.dev.set_status(False, self.number)
        self.refresh()

    def switch_toggle(self):
        self.dev.set_status(not self.switch_state, self.number)
        self.refresh()

    def evaluate(self):
        self.refresh()
        if self.random:
            print("Random...")
        else:
            if self.switch_state == True:  # Switch is already on
                if self.off != None and self.current_time > self.off:
                    self.switch_off()
            else:  # Switch is already off
                if self.on != None and self.current_time > self.on:
                    self.switch_on()

    def refresh(self):
        self.current_time = datetime.now().time().strftime("%H:%M")
        self.switch_state = self.dev.status()['dps'][str(self.number)]


class SonoffSwitch(SonoffDevice, Switch):
    def __init__(self, device, switch):
        Device.__init__(self, device)
        Switch.__init__(self, switch, None)

    def on():
        return

    def off():
        return


def get_devices(devices_obj):
    device_list = []

    try:
        for lvl in devices_obj.home.levels:
            print("Level->" + str(lvl.level))
            for r in ([] if not hasattr(lvl, 'rooms') else lvl.rooms):
                print(" Room-->" + str(r.name))
                for d in ([] if not hasattr(r, 'devices') else r.devices):
                    print("  Device--->" + str(d.name))
                    for s in ([] if not hasattr(d, 'switches') else d.switches):
                        print("   Switch---->" + str(s.switch))
                        if d.brand == 'tuya' and d.type == 'switch':
                            device_list.append(TuyaSwitch(d, s))
                        if d.brand == 'sonoff' and d.type == 'switch':
                            device_list.append(SonoffSwitch(d, s))
    except AttributeError:
        raise AttributeError(sys.exc_info()[1])

    return device_list
