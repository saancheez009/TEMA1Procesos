from flask import Blueprint, request
from flask_jwt_extended import jwt_required

from functions import*

rutaClientes="ficheros/clientes.json"
rutaPedidos="ficheros/pedidos.json"

pedidosBP=Blueprint('pedidos',__name__)

@pedidosBP.post('/')
@jwt_required()
def agregarPedido():
    if request.is_json:
        pedidos= leeFichero(rutaPedidos)
        clientes=leeFichero(rutaClientes)
        nuevo_pedido=request.get_json()
        for cliente in clientes:
            if cliente["id_cliente"]==nuevo_pedido["id_cliente"]:
                nuevo_pedido["id_cliente"]=nuevo_id(pedidos)
                pedidos.append(nuevo_pedido)
                escribeFichero(pedidos,rutaPedidos)
                return(nuevo_pedido),201
        return {"error": "El pedido no existe"},404
    return {"error": "JSON no correcto"},415

