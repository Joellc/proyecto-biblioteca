import os
from tabulate import tabulate
from conexion import *
from libro import *

con = conectar()

def iniciar():
    os.system('cls')
    while True:
        print('Seleccionar una de las opciones: ')
        print('\t1. Añadir un libro: ')
        print('\t2. Ver todos los libros: ')
        print('\t3. Buscar un libro: ')
        print('\t4. Modificar un libro: ')
        print('\t5. Eliminar un libro: ')
        print('\t6. Salir de la Aplicacion: ')
        opcion = input('Escoja la opcion: ')
        if opcion == '1':
            nuevo_libro()
        elif opcion == '2':
            ver_libros()
        elif opcion == '3':
            buscar_libro()
        elif opcion == '4':  # Change here: Use 'elif' instead of 'if'
            modificar_libro()
        elif opcion == '5':
            eliminar_libro()
        elif opcion == '6':
            break
        else:
            print('Escoja una opcion correcta')

def nuevo_libro():
    titulo = input('Ingrese el titulo: ')
    autor = input('Ingrese el autor: ')
    estado = 'Disponible'
    respuesta = registrar(titulo, autor, estado)
    print(respuesta)

def ver_libros():
    datos = mostrar()
    headers = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def buscar_libro():
    id = input('Ingrese el ID del libro: ')
    datos = buscar(id)
    headers = ['ID', 'TITULO', 'AUTOR', 'ESTADO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)

def modificar_libro():
    id = input("Ingrese el ID del libro a modificar: ")
    nuevo_valor = ''
    respuesta = ''
    campo = input('Seleccione el camop que desea modificar\n1. Titulo \n2 Autor \n3 Estado\n')
    if campo == '1':
        nuevo_valor = input('Ingrese el nuevo titulo del libro: ')
    elif campo == '2':
        nuevo_valor = input('Ingrese el nuevo Autor del libro: ')
    elif campo == '3':
        nuevo_valor = input('Ingrese el nuevo estado del libro: ')
    respuesta = modificar(id, campo, nuevo_valor)
    print(respuesta)

def eliminar_libro():
    id = input('Ingrese el id del libro a eliminar: ')
    respuesta = eliminar(id)
    print(respuesta)    

iniciar()