from flask import (
    Blueprint, flash, g, jsonify, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from elasticsearch import Elasticsearch
from datetime import datetime
from musask.forms import SearchForm

bp = Blueprint('musee', __name__)
es = Elasticsearch(["http://elasticsearch:9200/"])

@bp.route('/', methods=['GET'])
def index():
    form = SearchForm(request.form)
    return render_template('index.html', form=form)

@bp.route('/musee/<int:id>', methods=['GET'])
def read(id):
    try:
        resp = es.get(index="musee", id=id)
        return jsonify(dict(resp["_source"]))
    except:
        abort(404, f"Donnée introuvable.")

@bp.route('/musee', methods=['GET'])
def get():
    resp = es.search(index="musee", query={"match_all": {}})
    return jsonify(dict(resp["hits"]))

@bp.route('/musee/search', methods=['POST'])
def search():
    content = request.json
    resp = es.search(index="musee", body={"query": {"multi_match": {"query": content["search"]}}})
    return jsonify(dict(resp["hits"]))