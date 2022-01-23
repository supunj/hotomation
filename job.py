#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:59:26 2021

@author: Supun Jayathilake
"""


class Job:
    def __init__(self, device_list):
        self.device_list = device_list

    def evaluate_devices(self):
        for d in self.device_list:
            d.evaluate()
