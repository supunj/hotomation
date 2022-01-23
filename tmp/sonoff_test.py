#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 20:56:41 2021

@author: eternity
"""

from sonoff import Sonoff
import config

s = Sonoff('supunj@gmail.com', '1qaz2wsx!', 'as')
devices = s.get_devices()
if devices:
    # We found a device, lets turn something on
    device_id = devices[0]['deviceid']
    s.switch('on', device_id, None)

# update config
#config.api_region = s.get_api_region
#config.user_apikey = s.get_user_apikey
#config.bearer_token = s.get_bearer_token