from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from src.Application.Service.seller_service import SellerService

class SellerController:
    @staticmethod
    def register_seller():
        data = request.get_json()
        name = data.get('nome')
        cnpj = data.get('cnpj')
        email = data.get('email')
        password = data.get('senha')
        cellphone = data.get('celular')

        if not all([name, cnpj, email, password, cellphone]):
            return make_response(jsonify({"erro": "Todos os campos são obrigatórios: nome, cnpj, email, senha, celular"}), 400)

        if '@' not in email or '.' not in email.split('@')[-1]:
            return make_response(jsonify({"erro": "Formato de e-mail inválido."}), 400)

        if len(password) < 6:
            return make_response(jsonify({"erro": "A senha deve ter no mínimo 6 caracteres."}), 400)

        seller = SellerService.create_seller(name, cnpj, email, password, cellphone)
        return make_response(jsonify({
            "mensagem": "Seller salvo com sucesso",
            "Seller": seller.to_dict()
        }), 201)

    @staticmethod
    def activate_seller():
        data = request.get_json()
        cellphone = data.get('celular')
        code = data.get('codigo')

        if not cellphone or not code:
            return make_response(jsonify({"erro": "celular e/ou código são obrigatórios"}), 400)

        activated_seller = SellerService.active_seller(cellphone, code)
        if not isinstance(activated_seller, str):
            return make_response(jsonify({
                "mensagem": "conta ativada com sucesso!",
                "seller": activated_seller.to_dict()
            }), 200)
        elif activated_seller == "código inválido":
            return make_response(jsonify({"erro": "Código Inválido"}), 422)
        else:
            return make_response(jsonify({"erro": "celular não encontrado"}), 404)

    @staticmethod
    def login_seller():
        data = request.get_json()

        email = data.get("email")
        password = data.get("senha")

        if not email or not password:
            return make_response(jsonify({"erro": "Email e senha são obrigatórios"}), 400)

        seller = SellerService.authenticate_seller(email, password)

        if not seller:
            return make_response(jsonify({"erro": "Email ou senha inválidos"}), 401)

        if seller == "inativo":
            return make_response(jsonify({"erro": "Seller ainda não ativado"}), 403)

        token = create_access_token(identity=seller.id)

        return make_response(jsonify({
            "mensagem": "Login realizado com sucesso",
            "token": token,
            "seller": seller.to_dict()
        }), 200)

    @staticmethod
    @jwt_required()
    def update_seller():
        current_id = get_jwt_identity()
        data = request.get_json()
        if not data:
            return make_response(jsonify({"erro": "Dados para atualização não fornecidos"}), 400)

        update_seller = SellerService.update_seller(current_id, data)
        if not update_seller:
            return make_response(jsonify({"erro": "Seller não encontrado"}), 404)
        return make_response(jsonify({
            "mensagem": "perfil atualizado!",
            "seller": update_seller.to_dict()
        }), 200)