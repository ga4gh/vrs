from ..models import Interval, Location, Allele, Haplotype, Genotype


class DB:
    locations = {}
    alleles = {}
    haplotypes = {}
    genotypes = {}


db = DB()


l = Location(id="L1", position=Interval(start=5, end=6))
a = Allele(id="A1", location_id=l.id, replacement="A")
h = Haplotype(id="H1", completeness="COMPLETE", allele_ids=[a.id, a.id])
g = Genotype(id="G1", completeness="PARTIAL", haplotype_ids=[h.id, h.id])

db.locations[l.id] = l
db.alleles[a.id] = a
db.haplotypes[h.id] = h
db.genotypes[g.id] = g


