#import uuid

from ..db import db
from ... import models


def get(**kwargs):
    return list(db.alleles.values())[0].marshal(), 200


def search(**kwargs):
    return [a.marshal() for a in db.alleles.values()], 200


def post(**allele_data):
    allele = models.Allele(**allele_data)
    db.alleles[allele.id] = allele
    return allele.marshal(), 200
