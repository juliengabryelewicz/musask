import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from musask import musee
    app.register_blueprint(musee.bp)
    #app.add_url_rule('/', endpoint='index')
    
    return app
