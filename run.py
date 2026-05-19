import os
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager
from src.config.data_base import init_db
from src.routes import init_routes
from dotenv import load_dotenv
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint 

load_dotenv()

def create_app():
    app = Flask(__name__)

    CORS(app)

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    if not app.config["JWT_SECRET_KEY"]:
        raise ValueError("JWT_SECRET_KEY não definida no .env")

    JWTManager(app)

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
