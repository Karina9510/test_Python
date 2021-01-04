# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:11:29 2021

@author: karina999
"""

from textwrap import wrap
import numbers

s = "13.5.1967"

values = wrap(s, 1)

for _ in range(5):
    del values[-1]
    
print(values)

celek = 0

for i in values:  
    print(i)
    if i != ".":
        celek = celek + int(i)
        print("je to celek")
        print(celek)
    

year = "2004"
years = wrap(year, 1)
print(years)

celekYear = 0;
for i in years:  
    celekYear = celekYear + int(i)
    print(celekYear)
    
    
    
cislo = celek + celekYear
print(cislo)

if cislo <= 9:
    print("cislo je")
    print(cislo)
elif cislo ==  11:
    print("cislo je")
    print(cislo)
else:
    print("cislo je")
    list = [int(x) for x in str(cislo)]
    a = 0
    for i in list:  
        a = a + i
    
    print(a) 
    
    
    
    
    
    
    
    