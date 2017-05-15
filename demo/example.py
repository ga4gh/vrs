import datetime
import json

from vmcdemo import models, computed_id, serialize


if __name__ == "__main__":
    i = models.Interval(start=42, end=42)

    p = models.Position(interval=i)

    l = models.Location(sequence_id="VMC:GS_01234", position=p)
    l.id = computed_id(l)
    print("{} -> {}".format(serialize(l), l.id))
    locations = {l.id: l.as_dict()}

    a = models.Allele(location_id=l.id, state="A")
    a.id = computed_id(a)
    print("{} -> {}".format(serialize(a), a.id))
    alleles = {a.id: a.as_dict()}

    h1 = models.Haplotype(allele_ids=[a.id], completeness="PARTIAL")
    h1.id = computed_id(h1)
    print("{} -> {}".format(serialize(h1), h1.id))

    h2 = models.Haplotype(allele_ids=[a.id], completeness="COMPLETE")
    h2.id = computed_id(h2)
    print("{} -> {}".format(serialize(h2), h2.id))
    haplotypes = {h.id: h.as_dict() for h in [h1, h2]}

    g = models.Genotype(haplotype_ids=[h1.id, h2.id], completeness="COMPLETE")
    g.id = computed_id(g)
    print("{} -> {}".format(serialize(g), g.id))

    genotypes = {g.id: g.as_dict()}

    identifiers = {
        "VMC:GS_01234": [
            models.Identifier(namespace="NCBI", accession="NM_0123.4"),
            models.Identifier(namespace="VMC", accession="GS_01234")
        ],
        "VMC:GL_72pn8Yi-9WyoreirKOH7bc-Vx_Jjkdp_": [
            models.Identifier(namespace="dbSNP", accession="rs12345"),
        ]
    }

    b = models.Vmcbundle(
        meta=models.Meta(
            generated_at=datetime.datetime.isoformat(datetime.datetime.now()),
            vmc_version=0,
        ),
        locations=locations,
        alleles=alleles,
        haplotypes=haplotypes,
        genotypes=genotypes,
        identifiers=identifiers
    )
    s = b.serialize()
    b2d = json.loads(s)
    b2 = models.Vmcbundle(**b2d)
    assert b == b2

    print(json.dumps(json.loads(b.serialize()), indent=4, sort_keys=True))
