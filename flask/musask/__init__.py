import os
from musask.forms import SearchForm
from flask import Flask, request, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/', methods=['GET'])
    def index():
        form = SearchForm(request.form)
        return render_template('index.html', form=form)

    from musask import musee
    app.register_blueprint(musee.bp)
    
    return app
