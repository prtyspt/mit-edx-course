#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:59:34 2017

@author: prtyspt
"""

import math

def polysum(n, s):
    area = (0.25*n*(s**2)/math.tan(math.pi/n))
    perimeter = n*s
    return round(area + perimeter**2, 4)