from flask import Flask
from .models import db
from .departments import bp as departments_bp
from .roles import bp as roles_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    db.init_app(app)
    
    app.register_blueprint(departments_bp)
    app.register_blueprint(roles_bp)

    with app.app_context():
        db.create_all()

    return app
