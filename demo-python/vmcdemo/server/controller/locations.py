from ..db import db


def get(**kwargs):
    return kwargs, 200


def search():
    return [a.marshal() for a in db.alleles.values()], 200


def post(**kwargs):
    return None, 200
