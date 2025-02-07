import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from flask_cors import CORS
from flask_caching import Cache

from werkzeug.utils import import_string

from interview.init_routes import init_routes

MIGRATION_DIR = os.path.join('migrations')
db = SQLAlchemy(session_options={"autoflush": True, 'expire_on_commit': False})
migrate = Migrate()
cache = Cache()


def create_app(config_class='DevConfig'):
    app = Flask(__name__)

    cfg = import_string('interview.config.{0}'.format(config_class))()
    app.config.from_object(cfg)
    app.config['CONFIG_CLASS'] = config_class

    db.init_app(app)
    cors = CORS(app, origins='{0}'.format(app.config.get('CORS_SUPPORTS_ORIGIN'))
                , allow_headers=['Content-Type', 'Authorization', 'Access-Control-Allow-Credentials']
                , methods=['GET', 'POST', 'DELETE']
                , supports_credentials=True)

    cache.init_app(app)
    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config["specs"] = [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ]

    swagger_config["static_url_path"] = "/api/flasgger_static"
    swagger_config["swagger_ui"] = True
    swagger_config["specs_route"] = "/api/apidocs/"
    swag = Swagger(app, config=swagger_config)

    init_routes(app)

    migrate.init_app(app, db, directory=MIGRATION_DIR)

    return app
