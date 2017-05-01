from biocommons.seqrepo import SeqRepo
from bioutils.digests import truncated_digest

from . import models


def format(o):
    if isinstance(o, models.Identifier):
        return "{o.namespace}:{o.accession}".format(o=o)
    elif isinstance(o, models.Interval):
        return "{o.start}:{o.end}".format(o=o)
    elif isinstance(o, models.Location):
        return "{o.sequence_id}:{position}".format(o=o, position=format(o.position))
    elif isinstance(o, models.Allele):
        return "{o.location_id}:{o.replacement}".format(o=o)
    elif isinstance(o, models.Haplotype):
        return "{o.completeness}:{ids}".format(o=o, ids=",".join(sorted(o.allele_ids)))
    elif isinstance(o, models.Genotype):
        return "{o.completeness}:{ids}".format(o=o, ids=",".join(sorted(o.haplotype_ids)))
    else:
        raise Exception("Unknown type " + type(o))


def digest(o):
    return truncated_digest(format(o).encode("UTF-8"), digest_size=24)


def digest_identifier(o):
    if isinstance(o, models.Location):
        return models.Identifier(namespace="VL", accession=digest(o))
    if isinstance(o, models.Allele):
        return models.Identifier(namespace="VA", accession=digest(o))
    if isinstance(o, models.Haplotype):
        return models.Identifier(namespace="VH", accession=digest(o))
    if isinstance(o, models.Genotype):
        return models.Identifier(namespace="VG", accession=digest(o))
    
