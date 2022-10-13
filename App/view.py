﻿"""
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
from tabulate import tabulate
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
    print("6- Encontrar contenido producido en un país")
    print("7- Encontrar el contenido con un director involucrado")
    print("8- Listar TOP (N) de los géneros con más contenido")
    print("9- Listar TOP (N) de actores más populares para un género específico")
def printLoad(catalog):
    print_list = [["service_name","count"],["amazon",lt.size(catalog["amazon_prime"])],
    ["netflix",lt.size(catalog["netflix"])],["hulu",lt.size(catalog["hulu"])],["disney",lt.size(catalog["disney_plus"])]]
    total = lt.size(catalog["disney_plus"])+lt.size(catalog["netflix"])+lt.size(catalog["hulu"])+lt.size(catalog["amazon_prime"])
    print("Total de titulos cargados:",str(total)+".")
    print(tabulate(print_list,tablefmt="grid"))
    for i in ("amazon_prime","netflix","hulu","disney_plus"):
        print("Primeros y últimos 3 titulos cargados de",i+".")
        print_list = [["show_id","stream_service","type","release_year","title","director","cast",
                        "country","date_added","rating","duration","listed_in","description"]]
        first = lt.subList(catalog[i],1,3)
        last = lt.subList(catalog[i],lt.size(catalog[i])-2,3)
        for e in lt.iterator(first):
            print_list.append([e["show_id"],e["streaming_service"],e["type"],e["release_year"],
            e["title"],e["director"],e["cast"],e["country"],e["date_added"],e["rating"],e["duration"],
            e["listed_in"],e["description"][0:100]])
        for e in lt.iterator(last):
            print_list.append([e["show_id"],e["streaming_service"],e["type"],e["release_year"],
            e["title"],e["director"],e["cast"],e["country"],e["date_added"],e["rating"],e["duration"],
            e["listed_in"],e["description"][0:100]])
        print(tabulate(print_list,tablefmt="grid",maxcolwidths=17))
def printreq3(catalog,actor):
    list,movies,shows = controller.ContentByActor(catalog,actor)
    print_list = [["type","count"]]
    if movies != 0:
        print_list.append(["Movies",movies])
    if shows != 0:
        print_list.append(["TV Shows",shows])
    print(tabulate(print_list,tablefmt="grid"))
    print_list = [["release_year","title","duration","director","stream_service","type",
    "cast","country","rating","listed_in","description"]]
    if lt.size(list) < 6:
        print("\nHay menos de 6 participaciones de",actor,"en el catálogo.")
        for i in lt.iterator(list):
            print_list.append([i["release_year"],i["title"],i["duration"],
            i["director"],i["streaming_service"],i["type"],i["cast"],i["country"],
            i["rating"],i["listed_in"],i["description"][0:100]])
    else:
        print("\nEstas son las primeras y últimas 3 participaciones de",actor+".")
        first3 = lt.subList(list,1,3)
        last3 = lt.subList(list,lt.size(list)-2,3)
        for i in lt.iterator(first3):
            print_list.append([i["release_year"],i["title"],i["duration"],
            i["director"],i["streaming_service"],i["type"],i["cast"],i["country"],
            i["rating"],i["listed_in"],i["description"][0:100]])
        for i in lt.iterator(last3):
            print_list.append([i["release_year"],i["title"],i["duration"],
            i["director"],i["streaming_service"],i["type"],i["cast"],i["country"],
            i["rating"],i["listed_in"],i["description"][0:100]])
    print(tabulate(print_list,tablefmt="grid",maxcolwidths=20))
def printreq5(catalog,country):
    list,movies,shows = controller.ContentByCountry(catalog,country)
    print_list = [['type','count']]
    if movies != 0:
        print_list.append(["Movies",movies])
    if shows != 0:
        print_list.append(["TV Shows",shows])
    print(tabulate(print_list,tablefmt="grid"))
    print_list = [["release_year","title","duration","director","stream_service","type",
    "cast","country","rating","listed_in","description"]]
    if lt.size(list) < 6:
        print("\nHay menos de 6 participaciones de",country,"en el catálogo.")
        for i in lt.iterator(list):
            print_list.append([i["release_year"],i["title"],i["duration"],
            i["director"],i["streaming_service"],i["type"],i["cast"],i["country"],
            i["rating"],i["listed_in"],i["description"][0:100]])
    else:
        print("\nEstos son los primeros y últimos 3 contenidos producidos en",country+":")
        first3 = lt.subList(list,1,3)
        last3 = lt.subList(list,lt.size(list)-2,3)
        for i in lt.iterator(first3):
            print_list.append([i["release_year"],i["title"],i["duration"],
            i["director"],i["streaming_service"],i["type"],i["cast"],i["country"],
            i["rating"],i["listed_in"],i["description"][0:100]])
        for i in lt.iterator(last3):
            print_list.append([i["release_year"],i["title"],i["duration"],
            i["director"],i["streaming_service"],i["type"],i["cast"],i["country"],
            i["rating"],i["listed_in"],i["description"][0:100]])
    print(tabulate(print_list,tablefmt="grid",maxcolwidths=20))
def printreq7(catalog,N):
    genreList = controller.TopNGenres(catalog,N)
    rank = 1
    print_list1 = [["listed_in","count"]]
    print_list2 = [["rank","listed_in","count","type","stream_service"]]
    for i in lt.iterator(genreList):
        str1 = tabulate([["type","count"],["Movies",i["type"]["Movie"]],["TV Shows",i["type"]["TV Show"]]],tablefmt="plain")
        str2_list = [["stream_service","count"]]
        for key in i["stream"]:
            if i["stream"][key] > 0:
                str2_list.append([key,i["stream"][key]])
        str2 = tabulate(str2_list,tablefmt="plain")
        print_list1.append([i["genre"],i["size"]])
        print_list2.append([rank,i["genre"],i["size"],str1,str2])
        rank += 1
    print(tabulate(print_list1,tablefmt="grid"))
    print(tabulate(print_list2,tablefmt="grid"))
catalog = None
size = "-small"
type = "PROBING"
FC = 0.5
print('Tipo:', type, 'Factor de carga:', FC)
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
        #print("Tiempo de ejecución:",str(time),"ms.")
        #print("Memoria Usada:",str(memory),"kb.")
        printLoad(catalog["model"])
    elif int(inputs[0]) == 2:
        pass
    elif int(inputs[0]) == 4:
        actor = input("Ingrese el nombre del actor: ")
        printreq3(catalog,actor)
    elif int(inputs[0]) == 6:
        country = input("Ingrese el nombre del pais a consultar: ")
        printreq5(catalog,country)
    elif int(inputs) == 8:
        N = int(input("Ingrese el número N para el top: "))
        printreq7(catalog,N)
    else:
        sys.exit(0)
sys.exit(0)
