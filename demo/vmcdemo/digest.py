from biocommons.seqrepo import SeqRepo
from bioutils.digests import truncated_digest

from . import models

namespace = "VMC"
namespacec = namespace + ":"


def _get_identifier(iim, id):
    if id not in iim:
        raise RuntimeError("referenced id {id} not in IdIdentitiferMap".format(id=id))
    identifiers = [i for i in iim[id] if i.namespace == namespace]
    if len(identifiers) == 0:
        raise RuntimeError("No identifiers for {id} in namespace {ns}".format(id=id, ns=namespace))
    if len(identifiers) > 1:
        raise RuntimeError("Multiple identifiers for {id} in namespace {ns}".format(id=id, ns=namespace))
    return identifiers[0]


def format(o):
    if isinstance(o, models.Identifier):
        return "{o.namespace}:{o.accession}".format(o=o)

    if isinstance(o, models.Interval):
        return "{o.start}:{o.end}".format(o=o)

    if isinstance(o, models.Position):
        return "{o.type}:{ov}".format(o=o, ov=format(o.value))

    if isinstance(o, models.Location):
        return "{o.sequence_id}:{op}".format(o=o, op=format(o.position))

    if isinstance(o, models.AlleleSequence):
        return o.sequence

    if isinstance(o, models.Allele):
        return "{o.location_id}:{o.type}:{s}".format(o=o, s=format(o.state))

    raise Exception("Unknown type " + str(type(o)))


def digest(s):
    return truncated_digest(s.encode("UTF-8"), digest_size=24)



def computed_identifier(o):
    """return the VMC computed identifier for the object

    """

    if o.id is not None and o.id.startswith(namespacec):
        return o.id

    model_prefixes = {
        models.Location: "GL",
        models.Allele: "GL",
        models.Haplotype: "GL",
        models.Genotype: "GL",
    }

    return models.Identifier(namespace=namespace,
                             accession="{}_{}".format(model_prefixes[type(o)], digest(format(o))))


if __name__ == "__main__":
    iim = {
        "VMC:GS01234": [
            models.Identifier(namespace="NCBI", accession="NM_0123.4"),
            models.Identifier(namespace="VMC", accession="GS01234")
        ],
        "VMC:GS0": [
            models.Identifier(namespace="VMC", accession="GS0"),
            models.Identifier(namespace="VMC", accession="GS00")
        ],
    }
        
    i = models.Interval(start=42, end=42)
    p = models.Position(type="INTERVAL", value=i)
    l = models.Location(sequence_id="VMC:GS01234", position=p)
    a = models.Allele(location_id=l, type="SEQUENCE", state=models.AlleleSequence(sequence="A"))

    import IPython; IPython.embed()	  ### TODO: Remove IPython.embed()
