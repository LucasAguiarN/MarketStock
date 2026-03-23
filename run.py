from flask import Flask
from flask_jwt_extended import JWTManager
from src.config.data_base import init_db
from src.routes import init_routes
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint 

load_dotenv

def create_app():
    """
    Função que cria e configura a aplicação Flask.
    """
    app = Flask(__name__)

    # chave usada para gerar os tokens
    app.config["JWT_SECRET_KEY"] = "super-secret-key"

    # inicializa o JWT
    jwt = JWTManager(app)

    init_db(app)

    init_routes(app)
    
    swaggerui_blueprint = get_swaggerui_blueprint(
        '/docs',
        '/static/swagger.yaml',
    )
    app.register_blueprint(swaggerui_blueprint)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
