# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:58:58 2023

@author: Alumno
"""


import os

def crear_archivo(nombre,contenido):
    archivo=open(nombre, "wt")
    archivo.write(contenido)
    archivo.close

def eliminar_archivo(nombre):
    os.remove(nombre)
    
def agregar_contenido_archivo(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()

def leer_archivo(nombre):
    archivo = open(nombre,"rt",encoding='utf8')
    contenido = archivo.read()
    return contenido
