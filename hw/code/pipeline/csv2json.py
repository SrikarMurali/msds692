#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:58:34 2019

@author: srikarmurali
"""

import mycsv

def csv2json(data):
    print("{")
    
    header, data = mycsv.readcsv(data)
    print("\"headers\":", end="")
    h = []
    print("[", end="")
    for head in header:
        head = head.replace("'", "\"")
        h.append(head)
    print("\"", end="")
    print("\",\"".join(h), end="") 
    print("\"],")


    print("\"data\": [")
    count = 0
    for row in data:
        print("{")
        l = []
        for h, val in zip(header, row):
            l.append("\"" + h + "\":" + "\"" + val + "\"")
        print(",".join(l))
        count+=1
        if count != len(data):
            print("},")
        else:
            print("}")

            
        
    print("]")
    print("}")
        

csv2json(mycsv.getdata())
