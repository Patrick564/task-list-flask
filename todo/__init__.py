import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='mikey',
        DATABASE_HOST=os.environ.get('DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('DATABASE_USER'),
        DATABASE=os.environ.get('DATABASE')
    )

    from . import db

    db.init_app(app)

    from . import auth

    app.register_blueprint(auth.bp)

    @app.route('/hola')
    def hola():
        return 'Chanchito feliz'
    
    return app
