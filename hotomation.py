#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:39:09 2021

@author: Supun Jayathilake
"""


from ruamel.yaml import YAML
from ruamel.yaml.scanner import ScannerError
from pathlib import Path
from util import dict_to_object
from device import get_devices
import schedule
import time
from job import Job
import sys


def main():
    try:
        devices_dict = YAML(typ='safe').load(Path('devices.yaml'))
        devices_obj = dict_to_object(devices_dict)
        device_list = get_devices(devices_obj)
        job = Job(device_list)

        schedule.clear()
        schedule.every(devices_obj.home.interval).seconds.do(
            job.evaluate_devices)

        while True:
            schedule.run_pending()
            time.sleep(1)
    except (ScannerError, AttributeError):
        print("Invalid configuration file!" + "\n" + str(sys.exc_info()[1]))


if __name__ == "__main__":
    main()
