
from utils.functions import *

from flask import Blueprint, jsonify, request

ficheroCountries = "../proyecto/ficheros/countries.json"
ficheroCities = "../proyecto/ficheros/cities.json"

countriesBP = Blueprint('countries', __name__)

def find_next_id():
    countries = leeFichero(ficheroCountries)
    max = countries[0]["id"]
    for country in countries:
        if country["id"] > max:
            max = country["id"]

    return max+1

@countriesBP.get('/')
def get_countries():
    countries = leeFichero(ficheroCountries)
    return jsonify(countries)

@countriesBP.get("/<int:id>")
def get_country(id):
    countries = leeFichero(ficheroCountries)
    for country in countries:
        if country['id'] == id:
            return country, 200
    return {"error": "Country not found"}, 404


@countriesBP.post("/")
# definimos la función correspondiente
def add_country():
    countries = leeFichero(ficheroCountries)
    # Comprobamos si la petición cumple con el formato json
    if request.is_json:
        # Guardamos el formato JSON
        country = request.get_json()
        # Le asignamos un nuevo id
        country["id"] = find_next_id()
        # Añadimos el nuevo país a nuestra lista
        countries.append(country)
        escribeFichero(ficheroCountries, countries)
        # Devolvemos el país en formato diccionario y 201
        return country, 201
    # Si la petición no cumple con el formato JSON
    return {"error": "Request must be JSON"}, 415

@countriesBP.put("/<int:id>")
@countriesBP.patch("/<int:id>")
# definimos la función correspondiente
def modify_country(id):
    countries = leeFichero(ficheroCountries)
    # Se comprueba si la petición que nos ha llegado cumple con el formato json
    if request.is_json:
        # Creamos una variable donde guardamos el formato JSON, que coincide con un diccionario
        newCountry = request.get_json()
        # Tenemos que coger de nuestra lista de países, el país concreto a modificar, para lo cual
        # habrá que buscarlo por su id
        for country in countries:
            if country["id"] == id:
                # Modificamos todos los atributos del país con los nuevos valores indicados en el json
                for element in newCountry:
                    country[element] = newCountry[element]
                escribeFichero(ficheroCountries, countries)
                # Devolvemos el país en formato diccionario y el código 200 para indicar que se ha modificado
                return country, 200
    # Si la petición no cumple con el formato JSON devuelve un mensaje de error y el código 415
    return {"error": "Request must be JSON"}, 415

@countriesBP.delete("/<int:id>")
# Se debe añadir como parámetro de entrada el id que se 
# indica en la dirección
def delete_country(id):
    countries = leeFichero(ficheroCountries)
    # Como hay que eliminar un país concreto, tendremos que buscar 
    # en la lista el id del país que se ha indicado en la petición
    for country in countries:
        if country['id'] == id:
            countries.remove(country)
            escribeFichero(ficheroCountries, countries)
            # Si se encuentra el país, se devuelve el país ya vacío más el código 200
            return {}, 200
    # Si no se encuentra, se devuelve mensaje de error y código 404
    return {"error": "Country not found"}, 404

@countriesBP.get("/<int:id>/cities")
def get_cities(id):
    list = []
    cities = leeFichero(ficheroCities)
    for city in cities:
        if city['countryId'] == id:
            list.append(city)
    if len(list) > 0:
        return list, 200
    else:
        return {"error": "No cities for this country"}, 404