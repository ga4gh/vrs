import datetime
import json

from vmcdemo import models, computed_id, serialize


if __name__ == "__main__":
    identifiers = {
        "VMC:GS_01234": [
            models.Identifier(namespace="NCBI", accession="NM_0123.4"),
            models.Identifier(namespace="VMC", accession="GS_01234")
        ]
    }

    i = models.Interval(start=42, end=42)

    l = models.Location(sequence_id="VMC:GS_01234", position=i)
    l.id = computed_id(l)
    print("{} -> {}".format(serialize(l), l.id))

    a = models.Allele(location_id=l.id, state="A")
    a.id = computed_id(a)
    print("{} -> {}".format(serialize(a), a.id))

    h = models.Haplotype(allele_ids=[a.id], completeness="PARTIAL")
    h.id = computed_id(h)
    print("{} -> {}".format(serialize(h), h.id))

    h2 = models.Haplotype(allele_ids=[a.id], completeness="COMPLETE")
    h2.id = computed_id(h2)
    print("{} -> {}".format(serialize(h2), h2.id))

    g = models.Genotype(haplotype_ids=[h.id, h2.id], completeness="COMPLETE")
    g.id = computed_id(g)
    print("{} -> {}".format(serialize(g), g.id))

    b = models.Vmcbundle(
        meta=models.Meta(
            generated_at=datetime.datetime.isoformat(datetime.datetime.now()),
            vmc_version=0,
            ),
        locations=[l.as_dict()],
        alleles=[a.as_dict()],
        haplotypes=[h.as_dict(), h2.as_dict()],
        genotypes=[g.as_dict()],
        identifiers=identifiers
    )
    s = b.serialize()
    b2d = json.loads(s)
    b2 = models.Vmcbundle(**b2d)
    assert b == b2

    print(json.dumps(json.loads(b.serialize()), indent=4, sort_keys=True))
