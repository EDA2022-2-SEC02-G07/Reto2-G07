"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo
def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': model.newCatalog()
    }
    return control
# Funciones para la carga de datos
def loadData(control,size):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    catalog = control['model']
    amazonPrimeContent = loadContentData(catalog,size,"amazon_prime")
    disneyPlusContent = loadContentData(catalog,size,"disney_plus")
    huluContent = loadContentData(catalog,size,"hulu")
    netflixContent = loadContentData(catalog,size,"netflix")
    
    return amazonPrimeContent, disneyPlusContent, huluContent, netflixContent
def loadContentData(catalog,size,platform):
    file = 'Streaming/'+platform+'_titles-utf8'+size+'.csv'
    contentfile = cf.data_dir + file
    input_file = csv.DictReader(open(contentfile, encoding='utf-8'))
    for content in input_file:
        content["streaming_service"] = platform
        for key in content:
            if content[key] == "":
                content[key] = "unknown"
        model.add_content(catalog, content)
    return catalog
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def ContentByActor(catalog,actor): #Requerimiento 3
    return model.ContentByActor(catalog["model"],actor)
def TopNGenres(catalog,N): #Requerimiento 7
    return model.TopNGenres(catalog["model"],N)