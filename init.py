from flask import Flask
from loadconfig import load_config
from models import database
from flask_cors import CORS
from flasgger import Swagger


def init_app(name: str, config: str = "development"):
    app = Flask(name)
    app = load_config(app=app, config_type=config)
    database.init_app(app)
    CORS(app)

    swagger = Swagger(app, template={
        "openapi": "3.0.0",
        "info": {
            "title": "crayon Task Backend API",
            "version": "1.0",
            "description": "API for Crayon",
            "contact": {
                "responsibleOrganization": "Praveen Kumar",
                "email": "praveenpkg8@gmaill.com",
                "url": "thepraveenpkg.firebaseapp.com",
            },
        },
        "produces": [
            "application/json",
        ],
    })

    with app.app_context():
        from modules.newsfeed.upload import nw

        app.register_blueprint(nw)


    return app

