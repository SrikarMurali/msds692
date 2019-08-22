#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:10:43 2019

@author: srikarmurali
"""

import mycsv
import json
import csv
import os

def json2csv(data):
    
    jsondata = json.loads(data)
    header = jsondata["headers"]
    file = open("temp.csv", 'a').close()
    file = open("temp.csv", "w")
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    nodes = jsondata["data"]
    for node in nodes:
        vals = []
        for key, value in node.items():
            vals.append(value)
        csv_writer.writerow(vals)
    file.close()
    file = open("temp.csv", 'r')
    print(file.read(),end="")
    file.close()
    os.remove("temp.csv")

    
json2csv(mycsv.getdata())