# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:13:09 2023

@author: Alumno
"""
import camelcase

nombre = "Ayquipa Estrada Jheremy William"
print(nombre.upper())
print(nombre.title()) 

cam=camelcase.CamelCase()
print("Con Camelcase")

print(cam.hump(nombre))

cam2= camelcase.CamelCase('Ayquipa Estrada','Jheremy William')
print(cam2.hump(nombre))