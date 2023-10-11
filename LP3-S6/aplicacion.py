# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:04:43 2023

@author: Alumno
"""

import gestion_archivos

def menu():
    print("*****MENU PRINCIPAL*****")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Leer archivo")
    print("4. Mostrar contenido de archivo")
    print("5. Salir")
    
def crear():
    print("******CREAR ARCHIVO******")
    archivo= input("Archivo: ")
    contenido=input("Contenido: ")
    gestion_archivos.crear_archivo(archivo, contenido)
    
def eliminar():
    print("****Eliminar archivo****")
    archivo=input("Archivo: ")
    gestion_archivos.eliminar_archivo(archivo)
    
def agregar():
    print("****AGEGAR ARCHIVO****")
    archivo=input("Archivo: ")
    contenido=input("Contenido: ")
    gestion_archivos.agregar_contenido_archivo(archivo, contenido)
    
def listar():
    print("-- Mostrar contenido de un archivo -- ")
    archivo = input("Archivo: ")
    print(gestion_archivos.leer_archivo(archivo))

def salir():
    print("Gracias por su visita....")

def error():
    print("Opción incorrecta")
    

opcion = 1
while opcion!=5:
    menu()
    opcion = int(input("opcion: "))
    if opcion == 1:
        crear()
    elif opcion == 2:
        eliminar()
    elif opcion == 3:
        agregar()
    elif opcion == 4:
        listar()
    elif opcion == 5:
        salir()
    else:
        error()
        

    
    