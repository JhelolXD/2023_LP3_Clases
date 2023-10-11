# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 09:52:48 2023

@author: Alumno
"""

archivo=open("archivo_de_prueba.txt","wt")
contenido="Linea1 hola amigos como estan?\nLinea2 Bienvenido a la untels"
archivo.write(contenido)
archivo.close()