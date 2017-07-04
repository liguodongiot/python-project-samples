#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Describe: 
# Author: guodong.li 
# DateTime: 2017/7/4 18:36
# PythonVersion: 3.6

import re

p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

print("p.pattern:", p.pattern)

print("p.flags:", p.flags)

print("p.groups:", p.groups)

print("p.groupindex:", p.groupindex)

