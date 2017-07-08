from flask import jsonify, request
from flask.views import MethodView
from flask_restful import Resource

from .models import Tag


class TagView(MethodView):

    def get(self, id=None, page=1):
        if not id:
            tags = Tag.query.paginate(page, 2).items
            print(tags)
            res = []
            for tag in tags:
                res.append(tag.as_dict())
            return jsonify(tags=res)
        else:
            tag = Tag.query.filter_by(id=id).first_or_404()
            return jsonify(tag.as_dict())

    def post(self):
        return 'post'

    def patch(self, id):
        return 'patch {}'.format(id)

    def delete(self, id):
        return 'delete {}'.format(id)


class TagApi(Resource):
    def get(self, id=None, page=1):
        if not id:
            tags = Tag.query.paginate(page, 2).items
            res = []
            for tag in tags:
                res.append(tag.as_dict())
            return jsonify(tags=res)
        else:
            tag = Tag.query.filter_by(id=id).first_or_404()
            tag = Tag.query.filter_by(id=id).first()
            if not tag: return '', 404
            return jsonify(tag.as_dict())

    def post(self):
        return 'post'

    def patch(self, id):
        return 'patch {}'.format(id)

    def delete(self, id):
        return 'delete {}'.format(id)
