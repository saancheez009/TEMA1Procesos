from flask import *


app = Flask(__name__)

def _find_next_id():
    return max(country["id"] for country in countries) + 1

countries = [
    {"id":1, "name": "Bolivia", "capital":"La Paz", "Area":51320},
    {"id":2, "name": "Colombia", "capital":"Bogotá", "Area":56897},
    {"id":3, "name": "Venezuela", "capital":"Caracas", "Area":42563},
    {"id":14, "name": "España", "capital":"Madrid", "Area":19766}
]

nombreFichero= "servidor\\countries.json"

#@app.route("/")

def index():
    return 'Hola a todos! :) '

#listado entero de paises
@app.get("/countries")
def getCountries():
    
    return jsonify(countries)


#listar pais especifico
@app.get("/countries/<int:id>")

def getCountry(id):
    
  
    for country in countries:
        if country['id']==id:
            return country,200
    return{"error":"country not found"},404

#añadir un nuevo recurso


@app.post("/countries")
def addCountry():

    if request.is_json:
        country = request.get_json()
        
        country["id"]= _find_next_id()
        countries.append(country)
        
        return country,201
    return {"error" : "No valid format"},415

@app.put("/countries/<int:id>")
@app.patch("/countries/<int:id>")

def modify_country(id):
    if request.is_json:
        newCountry = request.get_json()
        
        for country in countries:
            if country["id"] == id:
                for element in newCountry:
                    country[element] = newCountry[element]
                return country,200
        return {"error" : "Country not found"}
    return {"error" : "No valid format "},415


@app.delete("/countries/<int:id>")
def delete_country(id):
    for country in countries:
        if country["id"]==id:
            countries.remove(country)
            return"{}",200
    return {"error":" Country not found "},404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=5050)
    
