from flask import Flask
import logging
from app.api.endpoints import api_bp
from app.routes import main_bp

# Configurar logging
logging.basicConfig(filename='logs/app.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

def create_app():
    app = Flask(__name__)
    
    # Registrar Blueprints
    app.register_blueprint(main_bp)      # Rutas web
    app.register_blueprint(api_bp, url_prefix='/api')  # Rutas API
    
    # Logging de todas las peticiones
    @app.before_request
    def log_request():
        logging.info(f"{Flask.request.method} {Flask.request.path}")
    
    return app
