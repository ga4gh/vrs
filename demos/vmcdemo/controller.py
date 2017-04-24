import os
import uuid

from utils import build_models

models = build_models(os.environ["OPENAPI_SPEC_PATH"])

class DB:
    locations = {}
    alleles = {}
    haplotypes = {}
    genotypes = {}


db = DB()


def allele_get(**kwargs):
    return a.marshal(), 200

def alleles_get():
    return [a.marshal() for a in db.alleles.values()], 200

def alleles_post(**allele_data):
    allele = models.Allele(**allele_data)
    db.alleles[allele.id] = allele
    return allele.marshal(), 200

def locations_get():
    return [a.marshal() for a in db.alleles.values()], 200

def locations_post(**kwargs):
    return None, 200
