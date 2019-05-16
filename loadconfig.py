import os
import yaml

from typing import Dict
from flask import Flask


def load_config(app, config_type: str = "development") -> Flask:
    file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.yml')
    config_file = open(file=file_name)
    all_config_file: Dict = yaml.load(config_file)
    config_file.close()

    config = {
        'development': all_config_file['DevelopmentConfig'],
        'production': all_config_file['ProductionConfig']
    }

    app.config['SQLALCHEMY_DATABASE_URI'] = config[config_type]["SQLALCHEMY_DATABASE_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config[config_type]["SQLALCHEMY_TRACK_MODIFICATIONS"]
    app.config['UPLOAD_FOLDER'] = config[config_type]['UPLOAD_FOLDER']

    return app

