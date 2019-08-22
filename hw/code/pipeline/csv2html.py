#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:14:36 2019

@author: srikarmurali
"""

import mycsv



def csv2html(data):
    print("<html>")
    print("<body>")
    print("<table>")
    header, data = mycsv.readcsv(data)
    print("<tr>", end="")
    for head in header:
        print("<th>" + head + "</th>", end="")
    print("</tr>")    
    for row in data:
        print("<tr>", end="")
        for val in row:
            print("<td>" + val + "</td>", end="")
        print("</tr>")  
    print("</tr>" )    
    print("</body>")
    print("</table>")
    print("</html>")
   






csv2html(mycsv.getdata())

