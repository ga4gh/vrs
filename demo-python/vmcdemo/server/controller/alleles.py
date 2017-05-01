from ..db import db
from ... import models


def get(**kwargs):
    alleles = list(db.alleles.values())
    allele0 = alleles[0]
    return allele0.marshal(), 200


def search(**kwargs):
    return [a.marshal() for a in db.alleles.values()], 200


def post(**allele_data):
    allele = models.Allele(**allele_data["allele"])
    db.alleles[allele.id] = allele
    return allele.marshal(), 200
