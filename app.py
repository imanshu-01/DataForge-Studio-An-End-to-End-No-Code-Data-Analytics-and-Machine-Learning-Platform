import os
from flask import Flask
from controllers.code import code

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    
    # Secret key from environment variable, with a fallback for development only
    app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Register blueprint
    app.register_blueprint(code)
    
    return app

if __name__ == "__main__":
    app = create_app()
    # Debug mode controlled by environment variable (default False)
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
