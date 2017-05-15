"""Provides format and digest functions for VMC objects

A VMC digest is computed using a `truncated_digest` (see below) on a
well-prescribed serialization of an object.

To compute the digest of an object:

* If an object has an id and it begins with "VMC:", it is assumed to
  be a VMC digest; that id is returned as is.

* If the object has an id that does not begin with "VMC:", the VMC
  digest is computed using the truncated_digest on the serialization
  of the current object.

* If the object does not have an id propoerty, the fields are
  serialized and returned (not 

To serialize an object, all properties except the `id` field are
formatted as strings and concatenated, separated by a colon.  When a
property to be serialized is an object, 

"""


from bioutils.digests import truncated_digest

from . import models

abc = models

namespace = "VMC"
namespacec = namespace + ":"
model_prefixes = {
    # GS: Sequence does not have a model
    models.Location: "GL",
    models.Allele: "GA",
    models.Haplotype: "GH",
    models.Genotype: "GG",
}



def computed_id(o):
    if o.id is not None and o.id.startswith(namespacec):
        return o.id
    ident = computed_identifier(o)
    return serialize(ident)


def computed_identifier(o):
    """return the VMC computed identifier for the object

    """

    if o.id is not None and o.id.startswith(namespacec):
        return models.Identifier(o.id.split(":"))

    accession = "{ns}_{d}".format(ns=model_prefixes[type(o)], d=digest(o))
    return models.Identifier(namespace=namespace, accession=accession)


def digest(o):
    s = serialize(o)
    return truncated_digest(s.encode("UTF-8"), digest_size=24)


def serialize(o, namespace="VMC"):
    def _map_id(id):
        assert id.startswith(namespace + ":")
        return id

    # isinstance() fails here because nested classes are coerced into
    # the `abc` namespace.  (I don't completely understand why this
    # happens. We'll use the class "basename".
    t = o.__class__.__name__

    if t == "Identifier":
        return "{o.namespace}:{o.accession}".format(o=o)

    if t == "Position":
        if o.interval is not None:
            return serialize(o.interval)
        raise Exception("Position isn't an interval ?!")

    if t == "Interval":
        return "<{t}:{o.start}:{o.end}>".format(t=t, o=o)

    if t == "Location":
        return "<{t}:{id}:{pos}>".format(t=t, id=_map_id(o.sequence_id), pos=serialize(o.position))

    if t == "Allele":
        return "<{t}:{id}:{o.state}>".format(t=t, id=_map_id(o.location_id), o=o)

    if t == "Haplotype":
        ids = sorted(_map_id(str(i)).encode("UTF-8") for i in o.allele_ids)
        return "<{t}:{o.completeness}:[{ids}]>".format(t=t, o=o, ids=";".join(i.decode("UTF-8") for i in ids))

    if t == "Genotype":
        ids = sorted(_map_id(str(i)).encode("UTF-8") for i in o.haplotype_ids)
        return "<{t}:{o.completeness}:[{ids}]>".format(t=t, o=o, ids=";".join(i.decode("UTF-8") for i in ids))

    raise Exception("Unknown type: " + t)




