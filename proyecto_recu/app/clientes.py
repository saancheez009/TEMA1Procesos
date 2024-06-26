from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from functions import*

rutaClientes="ficheros/clientes.json"
rutaPedidos="ficheros/pedidos.json"

clientesBP =Blueprint('clientes',__name__)

@clientesBP.get('/<int:id_cliente>/pedidos/<int:id_pedido>')
def obtener_pedido(id_cliente, id_pedido):
    pedidos= leeFichero(rutaPedidos)
    
    for pedido in pedidos:
        if pedido["id_pedido"]== id_pedido:
            if pedido["id_cliente"]==id_cliente:
                return pedido,200
            else:
                return {"error":"No existe ese pedido para ese cliente"},404
    return {"error":"Pedido no encontrado"},404

#def obtener_pedido(id_cliente, id_pedido):
#    clientes = leeFichero(rutaClientes)
#    pedidos = leeFichero(rutaPedidos)

#    cliente_encontrado = None
#    for cliente in clientes:
#        if cliente["id_cliente"] == id_cliente:
#            cliente_encontrado = cliente
    
#    pedidos_cliente = []
#    for pedido in pedidos:
#        if pedido["id_pedido"] == id_pedido and pedido["id_cliente"] == id_cliente:
#            pedidos_cliente.append(pedido)
    
#    if cliente_encontrado and pedidos_cliente:
#        return jsonify(pedidos_cliente), 200
#    else:
#        return jsonify({"error": "Pedido no encontrado"}), 404

@clientesBP.get('/<int:id_cliente>/total')
def total(id_cliente):
    clientes=leeFichero(rutaClientes)
    pedidos=leeFichero(rutaPedidos)
    sumaTotal=0
    encontrado=False
    
    for cliente in clientes:
        if cliente["id-cliente"]== id_cliente:
            encontrado=cliente
    
    if not encontrado:
        return jsonify({"error": "Cliente no encontrado"}), 404
   
    
    for pedido in pedidos:
        if pedido["id_cliente"]==id_cliente:
            sumaTotal+=pedido["total_pedido"]
            
    if sumaTotal>0:
        return {"total": sumaTotal},200
    else:
        return {"error":"El cliente no ha realizado pedidos"},404
    
#def obtener_total(id_cliente):
#    clientes = leeFichero(rutaClientes)
#    pedidos = leeFichero(rutaPedidos)
#    
#    total_gastado = 0
#    cliente_encontrado = None
#    for cliente in clientes:
#        if cliente["id_cliente"] == id_cliente:
#            cliente_encontrado = cliente
            
#    if not cliente_encontrado:
#        return jsonify({"error": "Cliente no encontrado"}), 404
#    
#    for pedido in pedidos:
#        if pedido["id_cliente"] == id_cliente:
#            total_gastado += pedido["total_pedido"]
    
#    return jsonify({"total_gastado": total_gastado}), 200
            
@clientesBP.put('/<int:id_cliente>')
@jwt_required()
def modificarCliente(id_cliente):
    clientes= leeFichero(rutaClientes)
    if request.is_json:
        nuevo_cliente=request.get_json()

        for cliente in clientes:
            if cliente["id_cliente"]==id_cliente:
                cliente.update(nuevo_cliente)
                escribeFichero(clientes,rutaClientes)
                return cliente,200
            
        nuevo_cliente["id_cliente"]= id_cliente
        clientes.append(nuevo_cliente)
        escribeFichero(clientes,rutaClientes)
        return nuevo_cliente,201
    
    else:
        return{"error":"JSON erróneo"},404
    
@clientesBP.delete('/<int:id_cliente>')
@jwt_required()
def eliminarCliente(id_cliente):
    clientes=leeFichero(rutaClientes)
    pedidos=leeFichero(rutaPedidos)

    for cliente in clientes:
        if cliente["id_cliente"]==id_cliente:
            clientes.remove(cliente)
            for pedido in pedidos:
                if pedido["id_cliente"]==id-cliente:
                    pedidos.remove(pedido)
            escribeFichero(cliente,rutaClientes)
            escribeFichero(pedidos,rutaPedidos)
            return {},200
    return {"error": "Cliente no encontrado"},404