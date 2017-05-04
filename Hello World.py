#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 00:04:11 2017

@author: pratyus
"""
def genPrimes():
    yield 2
    listOfPrimes = [2]
    currentNo = 3
    
    while True:
        isPrime = True
        for x in listOfPrimes:
            if currentNo % x == 0:
                isPrime = False
        
        if isPrime == False:
            currentNo += 1
        else:
            listOfPrimes.append(currentNo)
            yield currentNo
        
    
