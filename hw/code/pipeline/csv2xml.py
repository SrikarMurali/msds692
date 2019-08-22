#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:07:46 2019

@author: srikarmurali
"""

import sys
import mycsv


def csv2xml(data):
    print("<?xml version=\"1.0\"?>")
    print("<file>")
    header, data = mycsv.readcsv(data)
    print("<headers>", end="")
    h = []
    for head in header:
        h.append(head)
    print(",".join(h), end="")
    print("</headers>")
        
    print("<data>")
    for row in data:
        print("<record>")
        for h, val in zip(header, row):
            r = "<" + h + ">" + val + "</" + h + ">\n"
            r = r.replace(" ", "_")
            print(r, end="")
        print("</record>")
          
    print("</data>")
    print("</file>")
    
    

csv2xml(mycsv.getdata())
