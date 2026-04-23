from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.Application.Service.sale_service import SaleService

class SaleController:
    @staticmethod
    @jwt_required()
    def register_sale():
        seller_id = get_jwt_identity()
        data = request.get_json()

        product_id = data.get('produtoId')
        quantity = data.get('quantidade')

        if not product_id or not quantity:
            return make_response(jsonify({"erro": "produtoId e quantidade são obrigatórios"}), 400)
        
        if not isinstance(quantity, int) or quantity <= 0:
            return make_response(jsonify({"erro": "A quantidade deve ser um número inteiro positivo."}), 400)
        
        result = SaleService.create_sale(product_id, quantity, seller_id)

        if "error" in result:
            return make_response(jsonify({"erro": result["error"]}), result["status"])

        return make_response(jsonify({
            "mensagem": "Venda registrada com sucesso!",
            "venda": result["data"].to_dict()
        }), result["status"])