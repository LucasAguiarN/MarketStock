from src.Application.Controllers.user_controller import UserController
from src.Application.Controllers.seller_controller import SellerController
from flask import jsonify, make_response

def init_routes(app):    
    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
    @app.route('/api/sellers', methods=['POST'])
    def register_seller():
        return SellerController.register_seller()

    # LOGIN DO SELLER (AUTENTICAÇÃO JWT)
    @app.route('/api/sellers/login', methods=['POST'])
    def login_seller():
        return SellerController.login_seller()

    @app.route('/api/sellers/activate', methods=['POST'])
    def activate_seller():
        return SellerController.activate_seller()

    @app.route('/api/sellers/me', methods=['PUT'])
    def update_seller():
        return SellerController.update_seller()

    @app.route('/api/products', methods=['POST'])
    def register_product():
        return ProductController.register_product()

    @app.route('/api/products/{product_id}', methods=['PUT'])
    def update_product():
        return ProductController.update_product(product_id)

    @app.route('/api/products', methods=['GET'])
    def list_products():
        return ProductController.list_products()

    @app.route('/api/products/{product_id}', methods=['GET'])
    def select_product():
        return ProductController.select_product(product_id)

    @app.route('/api/products/{product_id}/inactivate', methods=['GET'])
    def deactivate_product():
        return ProductController.deactivate_product(product_id)