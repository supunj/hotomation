#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 23:04:29 2021

@author: eternity
"""


def dict_to_object(d):
    # checking whether object d is a
    # instance of class list
    if isinstance(d, list):
        d = [dict_to_object(x) for x in d]

    # if d is not a instance of dict then
    # directly object is returned
    if not isinstance(d, dict):
        return d

    # declaring a class
    class C:
        pass

    # constructor of the class passed to obj
    obj = C()

    for k in d:
        obj.__dict__[k] = dict_to_object(d[k])

    return obj
