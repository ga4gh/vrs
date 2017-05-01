# -*- coding: utf-8 -*-

# Questions:
# - identifiers in A, H, G? Def not in DTO, but in rich models?
#   Pro: "feels" natural to refer to allele.identifers
#   Con: don't want allele to become grab bag of annotations (I think)
# - Should richmodels compute ids or should they be assigned?
# - Should richmodels compute digests?


from __future__ import unicode_literals

import attr
from attr.validators import instance_of, optional
import six

from vmc.digest import vmc_digest


@attr.s
class Location(object):
    pass


@six.python_2_unicode_compatible
class Identifier(six.text_type):
    def _parse(self):
        return self.partition(":")[0:3:2]  # first and last elements

    @property
    def scheme(self):
        return self._parse()[0]

    @property
    def path(self):
        return self._parse()[1]


@attr.s
@six.python_2_unicode_compatible
class Interval(Location):
    start = attr.ib(validator=instance_of(int))
    end = attr.ib(validator=instance_of(int))

    def __bytes__(self):
        return self.__str__().encode("UTF-8")

    def __str__(self):
        return "{self.start}:{self.end}".format(self=self)

    def as_dict(self):
        return attr.asdict(self)

    def validate(self):
        attr.validate(self)
        assert 0 <= self.start <= self.end

    def overlaps(self, other):
        assert isinstance(other, Interval)
        return self.end > other.start and other.end > self.start


@attr.s
class Locus(object):
    seqref = attr.ib(validator=instance_of(str))
    location = attr.ib(validator=instance_of(Location))
    id = attr.ib(default=None, validator=optional(instance_of(str)),  cmp=False)

    def __bytes__(self):
        return self.__str__().encode("UTF-8")

    def __str__(self):
        return "{self.seqref}:{self.location}".format(self=self)

    def as_dict(self):
        return attr.asdict(self)

    def computed_identifier(self):
        return "GL:" + self.digest()

    def digest(self):
        return vmc_digest(bytes(self))

    def validate(self):
        attr.validate(self)
        self.seqref.validate()
        self.location.validate()


@attr.s
class Allele(object):
    seqref = attr.ib(validator=instance_of(str))
    location = attr.ib(validator=instance_of(Location))
    replacement = attr.ib(validator=instance_of(six.text_type))
    id = attr.ib(default=None, validator=optional(instance_of(str)), cmp=False)
    identifiers = attr.ib(default=[], validator=instance_of(list), cmp=False)

    def __bytes__(self):
        return self.__str__().encode("UTF-8")

    def __str__(self):
        return "{self.seqref}:{self.location}:{self.replacement}".format(self=self)

    def as_dict(self):
        return {
            "seqref": self.seqref,
            "location": self.location,
            "replacement": self.replacement,
            "id": self.id
        }

    def computed_identifier(self):
        return "GA:" + self.digest()

    def digest(self):
        return vmc_digest(bytes(self))

    def validate(self):
        attr.validate(self)
        self.locus.validate()
        self.validate()


@attr.s
class Haplotype(object):
    alleles = attr.ib(validator=instance_of(list))
    id = attr.ib(default=None, validator=optional(instance_of(str)), cmp=False)
    identifiers = attr.ib(default=[], validator=instance_of(list), cmp=False)

    def allele_ids(self):
        # return unicode allele identifiers in UTF-8 encoded order
        # encoding eliminates effects of locale-specific collation order 
        ids = [a.id for a in self.alleles]
        ids.sort(key=lambda e: e.encode("UTF-8"))
        return ids

    def as_dict(self):
        return {
            "allele_ids": self.allele_ids(),
            "id": self.id
        }

    def computed_identifier(self):
        return "GH:" + self.digest()

    def digest(self):
        return vmc_digest(";".join(self.allele_ids()).encode("UTF-8"))

    def validate(self):
        attr.validate(self)
        if len(set(a.locus.seqref for a in self.alleles)) != 1:
            raise ValueError("Haplotype alleles must be defined on exactly one sequence")
        # TODO: validate that alleles do not overlap



@attr.s
class Genotype(object):
    haplotypes = attr.ib(validator=instance_of(list))
    id = attr.ib(default=None, validator=optional(instance_of(str)), cmp=False)
    identifiers = attr.ib(default=[], validator=instance_of(list), cmp=False)

    def as_dict(self):
        return {
            "haplotype_ids": self.haplotype_ids(),
            "id": self.digest()
        }

    def computed_identifier(self):
        return "GG:" + self.digest()

    def digest(self):
        return vmc_digest(";".join(self.haplotype_ids()).encode("UTF-8"))

    def haplotype_ids(self):
        # return unicode haplotype identifiers in UTF-8 encoded order
        # encoding eliminates effects of locale-specific collation order 
        ids = [h.id for h in self.haplotypes]
        ids.sort(key=lambda e: e.encode("UTF-8"))
        return ids

    def validate(self):
        attr.validate(self)


if __name__ == "__main__":
    import json

    import vmc.codecs.json

    def to_json(o):
        return json.dumps(o, indent=2, sort_keys=True, cls=vmc.codecs.json.JSONEncoder, ensure_ascii=False)


    sr = "NCBI:NC_000019.10"
    intervals = {
        "rs429358": Interval(44908683, 44908684),
        "rs7412": Interval(44908821, 44908822),
    }
    o = intervals["rs429358"]
    print("r={o!r}\ns={o}\nj={j}".format(o=o, j=to_json(o)))


    loci = {
        "rs429358": Locus(sr, intervals["rs429358"]),
        "rs7412": Locus(sr, intervals["rs7412"]),
    }
    o = loci["rs429358"]
    print("r={o!r}\ns={o}\nid={o.id}\nj={j}".format(o=o, j=to_json(o)))


    alleles = {
        "rs429358T": Allele(seqref=sr, location=intervals["rs429358"], replacement="T"),
        "rs429358C": Allele(seqref=sr, location=intervals["rs429358"], replacement="C"),
        "rs7412T":   Allele(seqref=sr, location=intervals["rs7412"],   replacement="T"),
        "rs7412C":   Allele(seqref=sr, location=intervals["rs7412"],   replacement="C"),
    }
    o = alleles["rs429358C"]
    print("r={o!r}\ns={o}\nid={o.id}\nj={j}".format(o=o, j=to_json(o)))

    haplotypes = {
        "ε1":  Haplotype(alleles=[alleles["rs429358C"], alleles["rs7412T"]]),
        "ε2":  Haplotype(alleles=[alleles["rs429358T"], alleles["rs7412T"]]),
        "ε3":  Haplotype(alleles=[alleles["rs429358T"], alleles["rs7412C"]]),
        "ε4":  Haplotype(alleles=[alleles["rs429358C"], alleles["rs7412C"]]),
        "ε4r": Haplotype(alleles=[alleles["rs7412C"], alleles["rs429358C"]]),
    }
    o = haplotypes["ε1"]
    print("r={o!r}\ns={o}\nid={o.id}\nj={j}".format(o=o, j=to_json(o)))

    genotypes = {
        "{}/{}".format(h1n, h2n): Genotype([h1, h2])
        for h1n, h1 in haplotypes.items()
        for h2n, h2 in haplotypes.items()
        }
    o = genotypes["ε1/ε1"]
    print("r={o!r}\ns={o}\nid={o.id}\nj={j}".format(o=o, j=to_json(o)))


    doc = {
        "meta": {
            "schema_version": 1
        },
        "alleles": [a.as_dict() for a in alleles.values()],
        "haplotypes": [h.as_dict() for h in haplotypes.values()],
        "genotypes": [g.as_dict() for g in genotypes.values()],
    }
