from vmcdemo import models, computed_id, serialize


if __name__ == "__main__":
    id_identifier_map = {
        "VMC:GS_01234": [
            models.Identifier(namespace="NCBI", accession="NM_0123.4"),
            models.Identifier(namespace="VMC", accession="GS_01234")
        ]
    }

    # internal_id:ns_id map for givenen namespace
    # Not currently used -- intended for digest lookups
    iim = {id: serialize(ident)
           for id, idents in id_identifier_map.items()
           for ident in idents if ident.namespace == "VMC"}

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

    g = models.Genotype(haplotype_ids=[h.id], completeness="COMPLETE")
    g.id = computed_id(g)
    print("{} -> {}".format(serialize(g), g.id))
