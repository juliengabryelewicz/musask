from flask import (
    Blueprint, jsonify, render_template, request
)
from werkzeug.exceptions import abort
from elasticsearch import Elasticsearch

bp = Blueprint('musee', __name__, url_prefix="/musee")
es = Elasticsearch(["http://elasticsearch:9200/"])

@bp.route('/<int:id>', methods=['GET'])
def read(id):
    try:
        resp = es.get(index="musee", id=id)
        return jsonify(dict(resp["_source"]))
    except:
        abort(404, f"Donnée introuvable.")

@bp.route('/', methods=['GET'])
def get():
    resp = es.search(index="musee", query={"match_all": {}})
    return jsonify(dict(resp["hits"]))

@bp.route('/search', methods=['POST'])
def search():
    content = request.json
    resp = es.search(index="musee", body={"query": {"multi_match": {"query": content["search"]}}})
    return jsonify(dict(resp["hits"]))