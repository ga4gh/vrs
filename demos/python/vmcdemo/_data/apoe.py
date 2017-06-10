# ApoE allele, haplotype, and genotype definitions
# from http://snpedia.com/index.php/APOE
#                              rs7412 
#                              NC_000019.10:g.44908822
#                              C          T
# rs429358                 C   APOE-ε4    APOE-ε1
# NC_000019.10:g.44908684  T   APOE-ε3    APOE-ε2


from .. import Allele, Genotype, Haplotype, Interval, Locus


sr = "NCBI:NC_000019.10"

intervals_by_name = {
    "rs429358": Interval(44908683, 44908684),
    "rs7412": Interval(44908821, 44908822),
}

loci_by_name = {
    "rs429358": Locus(sr, intervals_by_name["rs429358"]),
    "rs7412": Locus(sr, intervals_by_name["rs7412"]),
}

alleles_by_name = {
    "rs429358T": Allele(sr, intervals_by_name["rs429358"], "T", identifiers=["dbsnp:rs429358T"]),
    "rs429358C": Allele(sr, intervals_by_name["rs429358"], "C", identifiers=["dbsnp:rs429358C"]),
    "rs7412T"  : Allele(sr, intervals_by_name["rs7412"],   "T", identifiers=["dbsnp:rs7412T"  ]),
    "rs7412C"  : Allele(sr, intervals_by_name["rs7412"],   "C", identifiers=["dbsnp:rs7412C"  ]),
}
alleles = alleles_by_name.values()

haplotypes_by_name = {
    "ε1" : Haplotype([alleles_by_name["rs429358C"], alleles_by_name["rs7412T"]], identifiers=["ε1" ]),
    "ε2" : Haplotype([alleles_by_name["rs429358T"], alleles_by_name["rs7412T"]], identifiers=["ε2" ]),
    "ε3" : Haplotype([alleles_by_name["rs429358T"], alleles_by_name["rs7412C"]], identifiers=["ε3" ]),
    "ε4" : Haplotype([alleles_by_name["rs429358C"], alleles_by_name["rs7412C"]], identifiers=["ε4" ]),
}
haplotypes = haplotypes_by_name.values()

genotypes_by_name = {
    identifier: Genotype([h1, h2], identifiers=[identifier])
    for identifier, h1, h2 in (
            ("{}/{}".format(h1n, h2n), h1, h2)
            for h1n, h1 in haplotypes_by_name.items()
            for h2n, h2 in haplotypes_by_name.items()
    )
}
genotypes = genotypes_by_name.values()
