from flask import Blueprint, jsonify
import os

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return "<h1>Bienvenido a la App Flask Modular</h1>"

@main_bp.route('/info')
def info():
    container = os.getenv('HOSTNAME', 'local')
    port = os.getenv('PORT', '8000')
    return jsonify({"container": container, "port": port})
