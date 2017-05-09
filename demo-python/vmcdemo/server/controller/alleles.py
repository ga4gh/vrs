from ..db import db
from ... import models
from ... import digest


def get(**kwargs):
    alleles = list(db.alleles.values())
    allele0 = alleles[0]
    return allele0.marshal(), 200


def search(**kwargs):
    return [a.marshal() for a in db.alleles.values()], 200


def post(**allele_data):
    allele = models.Allele(
        location_id=allele_data["allele"]["location_id"],
        type=allele_data["allele"]["type"],
        state=models.AlleleSequence(**allele_data["allele"]["state"])
        )
    allele.id = digest.format(digest.computed_identifier(allele))
    db.alleles[allele.id] = allele
    return allele.marshal(), 200
