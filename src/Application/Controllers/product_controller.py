from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService
from src.Infrastructure.Model.seller import Seller
from flask_jwt_extended import jwt_required, get_jwt_identity

class ProductController:
    @staticmethod
    def register_product():
        seller = seller_logado()

        if not seller:
            return make_response(jsonify({"erro": "Seller não autenticado"}), 404)
        
        data = request.get_json()
        name = data.get('nome')
        price = data.get('preco')
        quantity = data.get('quantidade')
        image = data.get('imagem')

        if not all([name, price, quantity, image]):
            return make_response(jsonify({"erro": "Missing required fields"}), 400)

        product = ProductService.create_product(name, price, quantity, image, seller)
        return make_response(jsonify({
            "mensagem": "Product salvo com sucesso",
            "Product": product.to_dict()
        }), 200)

    @staticmethod
    def update_product():
        seller_logado = seller_logado()

        if not seller_logado:
            return make_response(jsonify({"erro": "Seller não autenticado"}), 404)

        data = request.get_json()
        product_id = data.get('id')
        if not data:
            return make_response(jsonify({"erro": "Dados para atualização não fornecidos"}), 400)

        update_product = ProductService.update_product(product_id, data)
        if not update_product:
            return make_response(jsonify({"erro": "Não foi possível atualizar os dados"}), 400)
        return make_response(jsonify({
            "mensagem": "Produto atualizado!",
            "product": update_product.to_dict()
        }), 200)

    @staticmethod
    def list_products():
        seller_logado = seller_logado()

        if not seller_logado:
            return make_response(jsonify({"erro": "Seller não autenticado"}), 404)

        products = ProductService.select_all_products()
        if not products:
            return make_response(jsonify({"erro": "Nenhum produto encontrado"}), 404)
        return make_response(jsonify({"Produtos": products}), 200)

    @staticmethod
    def show_product(product_id):
        seller_logado = seller_logado()

        if not seller_logado:
            return make_response(jsonify({"erro": "Seller não autenticado"}), 404)

        product = ProductService.show_product(product_id)
        if not product:
            return make_response(jsonify({"erro": "Produto não encontrado"}), 404)
        return make_response(jsonify({"Produto": product}), 200)
        
    @staticmethod
    def deactivate_product(product_id):
        seller_logado = seller_logado()

        if not seller_logado:
            return make_response(jsonify({"erro": "Seller não autenticado"}), 404)

        deactivate_product = ProductService.deactivate_product(product_id)
        if deactivate_product:
            return make_response(jsonify({
                "mensagem": "Produto desativado com sucesso!"}), 200)
        return make_response(jsonify({"erro": "Produto não encontrado"}), 400)

    @staticmethod
    @jwt_required()
    def seller_logado():
        id_seller = get_jwt_identity()
        seller = Seller.query.get(id_seller)
        if seller:
            return id_seller
        else:
            return False