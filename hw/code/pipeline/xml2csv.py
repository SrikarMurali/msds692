#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:38:40 2019

@author: srikarmurali
"""

import mycsv
import xmltodict
import untangle
from xml.etree import ElementTree as ET
import csv
import os



def xml2csv(data):
    xml = untangle.parse(data)
    headers = xml.file.data.record[0].get_elements()
    
    
    head = []
    file = open("temp.csv", 'a').close()
    file = open("temp.csv", "w")
    csv_writer = csv.writer(file)
    for node in headers:
        name = node._name.replace("_", " ")
        head.append(name)
    csv_writer.writerow(head)

    
    xmldata = xml.file.data.record
    for node in xmldata:
        curr = node.get_elements()
        vals = []
        for v in curr:
            vals.append(v.cdata)
        csv_writer.writerow(vals)

    file.close()
    file = open("temp.csv", 'r')
    print(file.read(),end="")
    file.close()
    os.remove("temp.csv")


xml2csv(mycsv.getdata())



