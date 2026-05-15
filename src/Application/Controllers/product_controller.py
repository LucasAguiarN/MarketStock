import os
from uuid import uuid4
from werkzeug.utils import secure_filename
from flask import request, jsonify, make_response
from src.Application.Service.product_service import ProductService
from flask_jwt_extended import jwt_required, get_jwt_identity

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class ProductController:
    @staticmethod
    @jwt_required()
    def register_product():
        seller_id = get_jwt_identity()
        
        # 1. Pegar dados do formulário
        name = request.form.get('nome')
        price = request.form.get('preco')
        quantity = request.form.get('quantidade')

        # 2. Processar arquivo
        file = request.files.get('imagem')

        if not all([name, price is not None, quantity is not None, file]):
            return make_response(jsonify({"erro": "Todos os campos são obrigatórios: nome, preco, quantidade, imagem"}), 400)

        if not allowed_file(file.filename):
            return make_response(jsonify({"erro": "Extensão de arquivo não permitida. Use: png, jpg, jpeg, webp"}), 400)

        try:
            price = float(price)
            quantity = int(quantity)
            if price <= 0 or quantity < 0:
                raise ValueError()
        except (ValueError, TypeError):
            return make_response(jsonify({"erro": "O preço deve ser um número positivo e a quantidade um número não-negativo."}), 400)

        # Salvar o arquivo
        filename = f"{uuid4()}_{secure_filename(file.filename)}"
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
            
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        
        # Gerar URL (usando host_url para ser dinâmico)
        image_url = f"{request.host_url}static/uploads/{filename}"

        product = ProductService.create_product(name, price, quantity, image_url, seller_id)
        return make_response(jsonify({
            "mensagem": "Product salvo com sucesso",
            "Product": product.to_dict()
        }), 201)

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
        product, status_disabled = deactivate_product

        if not product:
            return make_response(jsonify({"erro": "Não foi possível desativar o produto. Verifique se o produto existe e pertence a você."}), 404)

        if status_disabled:
            return make_response(jsonify({"mensagem": "O produto já está inativo."}), 409)
        
        return make_response(jsonify({
            "mensagem": "Produto desativado com sucesso!"
        }), 200)