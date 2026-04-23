from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService
from flask_jwt_extended import jwt_required, get_jwt_identity

class ProductController:
    @staticmethod
    @jwt_required()
    def register_product():
        seller_id = get_jwt_identity()
        
        data = request.get_json()
        name = data.get('nome')
        price = data.get('preco')
        quantity = data.get('quantidade')
        image = data.get('imagem')

        if not all([name, price is not None, quantity is not None, image]):
            return make_response(jsonify({"erro": "Todos os campos são obrigatórios: nome, preco, quantidade, imagem"}), 400)

        try:
            price = float(price)
            quantity = int(quantity)
            if price <= 0 or quantity < 0:
                raise ValueError()
        except (ValueError, TypeError):
            return make_response(jsonify({"erro": "O preço deve ser um número positivo e a quantidade um número não-negativo."}), 400)

        product = ProductService.create_product(name, price, quantity, image, seller_id)
        return make_response(jsonify({
            "mensagem": "Product salvo com sucesso",
            "Product": product.to_dict()
        }), 200)

    @staticmethod
    @jwt_required()
    def update_product(product_id):
        seller_id = get_jwt_identity()

        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "Dados para atualização não fornecidos"}), 400)
        
        updated_product = ProductService.update_product(product_id, data, seller_id)
        if not updated_product:
            return make_response(jsonify({"erro": "Não foi possível atualizar o produto. Verifique se o produto existe e pertence a você."}), 404)
        return make_response(jsonify({
            "mensagem": "Produto atualizado com sucesso!",
            "product": updated_product.to_dict()
        }), 200)

    @staticmethod
    @jwt_required()
    def list_products():
        seller_id = get_jwt_identity()

        products = ProductService.select_all_products(seller_id)
        return make_response(jsonify({"Produtos": [p.to_dict() for p in products]}), 200)

    @staticmethod
    @jwt_required()
    def show_product(product_id):
        seller_id = get_jwt_identity()

        product = ProductService.show_product(product_id, seller_id)
        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado ou não pertence a este seller"}), 404)
        return make_response(jsonify({"Produto": product.to_dict()}), 200)
        
    @staticmethod
    @jwt_required()
    def deactivate_product(product_id):
        seller_id = get_jwt_identity()

        deactivate_product = ProductService.deactivate_product(product_id, seller_id)
        if deactivate_product:
            return make_response(jsonify({
                "mensagem": "Produto desativado com sucesso!"
            }), 200)
        return make_response(jsonify({"erro": "Não foi possível desativar o produto. Verifique se o produto existe e pertence a você."}), 404)