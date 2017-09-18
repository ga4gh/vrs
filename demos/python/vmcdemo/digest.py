"""Provides format and digest functions for VMC objects

A VMC digest is computed using a "truncated digest" (see below) on a
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


The computed_identifier is functionally this:

  ci = computed_identifier(obj)

The pseudocode for computed_identifier is:

def computed_identifier(obj):
  ser = serialize( obj )
  digest = base64_urlsafe( sha512( ser )[:24] )
  prefix = vmc_type_prefix[type(obj)]
  accession = prefix + "_" + digest
  ir = Identifier(namespace="VMC", accession=accession)

"""

import base64
import hashlib

from . import models

abc = models

enc = "ASCII"

vmc_namespace = "VMC"
vmc_model_prefixes = {
    # GS: Sequence does not have a model
    models.Allele: "GA",
    models.Genotype: "GG",
    models.Haplotype: "GH",
    models.Location: "GL",
}


def computed_id(o):
    """return the VMC computed identifier for the object, as a CURIE
    (string)

    """

    return "{i.namespace}:{i.accession}".format(i=computed_identifier(o))


def computed_identifier(o):
    """return the VMC computed identifier for the object, as an Identifier

    """

    pfx = vmc_model_prefixes[type(o)]
    dig = truncated_digest(o)
    accession = "{pfx}_{dig}".format(pfx=pfx, dig=dig)
    return models.Identifier(namespace=vmc_namespace, accession=accession)


def id_to_ir(id):
    """Convert internal id to identifier string.

    For the VMC demo, we're going to assume that the computed
    identifier is used as the id, and therefore we can just assert
    that the id begins with the "VMC:" and then return a synthesized
    Identifier.

    If an implementation uses a different internal id, this function
    needs to be changed.

    """
    assert id.startswith(vmc_namespace + ":"), "Must be a VMC id for this demo"
    ns, acc = id.split(":")
    return models.Identifier(namespace=ns, accession=acc)


def serialize(o, namespace="VMC"):
    """convert object to canonical serialized representation

    Serialization is the core of the VMC digest algorithm.  All of the
    magic occurs here.

    Two wrinkles:

    * The digest must be based on VMC (external) identifiers. For this
      demo, the VMC identifiers and internal ids are equivalent, but
      that need not be true generally.  For example, an implementation
      might choose to use uuids for ids, with VMC identifiers
      attached.  (See id_to_ir for shortcut used in this demo.)

    * Alleles need to be reliably ordered.  Unfortunately, URL-safe
      Base 64 encodings use characters that are subject to
      locale-dependent sort differences.  So, we sort here by the
      ASCII-encoded form (essentially, binary sorted).

    """

    # isinstance() fails here because nested classes built with
    # python_jsonschema_objects are coerced into the `abc` namespace.
    # So, we'll use the class "basename".
    t = o.__class__.__name__

    if t == "Identifier":
        return "<{t}:{o.namespace}:{o.accession}>".format(t=t, o=o)

    if t == "Interval":
        return "<{t}:{o.start}:{o.end}>".format(t=t, o=o)

    if t == "Location":
        ir = id_to_ir(o.sequence_id)
        return "<{t}:{ir}:{ival}>".format(t=t, ir=serialize(ir), ival=serialize(o.interval))

    if t == "Allele":
        ir = id_to_ir(o.location_id)
        return "<{t}:{ir}:{o.state}>".format(t=t, ir=serialize(ir), o=o)

    if t == "Haplotype":
        # sort as well-defined binary encoding to circumvent locale-dependent sorting differences
        ids = sorted(serialize(id_to_ir(str(i))).encode(enc) for i in o.allele_ids)
        return "<{t}:{o.completeness}:[{irss}]>".format(t=t, o=o, irss=";".join(i.decode(enc) for i in ids))

    if t == "Genotype":
        # sort as well-defined binary encoding to circumvent locale-dependent sorting differences
        ids = sorted(serialize(id_to_ir(str(i))).encode(enc) for i in o.haplotype_ids)
        return "<{t}:{o.completeness}:[{irss}]>".format(t=t, o=o, irss=";".join(i.decode(enc) for i in ids))

    raise Exception("Unknown type: " + t)


def truncated_digest(o):
    """For a VMC object o, return the URL-safe, Base64 encoded, 24-byte
    truncated SHA512 digest as unicode

    """
    ser = serialize(o)
    digest = hashlib.sha512(ser.encode(enc)).digest()
    tdigest_b64us = base64.urlsafe_b64encode(digest[:24]).decode(enc)
    return tdigest_b64us
