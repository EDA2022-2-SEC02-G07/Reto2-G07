"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Examinar películas estrenadas en un año")
    print("3- Examinar programas de televisión agregados en un año")
    print("4- Encontrar contenido donde participa un actor")
    print("5- Encontrar contenido por un genero particular")
    print("6-Encontrar contenido producido en un país")
    print("7- Encontrar el contenido con un director involucrado")
    print("8- Listar TOP (N) de los géneros con más contenido")
    print("9- Listar TOP (N) de actores más populares para un género específico")

catalog = None
size = "-small"
type = "CHAINING"
FC = 1
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        if catalog == None:
            catalog = controller.newController(type,FC)
        time,memory = controller.loadData(catalog,size)
        print("Tiempo de ejecución:",str(time),"ms.")
        print("Memoria Usada:",str(memory),"kb.")
    elif int(inputs[0]) == 2:
        pass

    else:
        sys.exit(0)
sys.exit(0)
