"""

"""

import json
import uuid

import biocommons.seqrepo

class DemoApp:
    def __init__(self):
        self.sequences = []
        self.alleles = []
        self.haplotypes = []
        self.genotypes = []
        self.relationship_classes = {}
        self.relationships = {}
        self._digest_map = {}   # digest -> object
        self._sr = biocommons.seqrepo.SeqRepo("/usr/local/share/seqrepo/master")

    def add_allele(self, allele):
        digest = allele.digest()
        if digest not in self._digest_map:
            self.alleles.append(allele)
            self._digest_map[digest] = allele
        return allele

    def add_haplotype(self, haplotype):
        self.haplotypes.append(haplotype)

    def add_genotype(self, genotype):
        self.genotypes.append(genotype)

    def assign_ids(self):
        """assign ids to any object where id is None"""
        for o in self.alleles + self.haplotypes + self.genotypes:
            if o.id is None:
                o.id = str(uuid.uuid4())

    def to_vmc(self):
        self.assign_ids()
        identifier_id_map = {idr: o.id
                             for o in self.alleles + self.haplotypes + self.genotypes
                             for idr in o.identifiers}

        doc = {
            "vmc": {
                "version": 1,
            },
            "alleles": [o.as_dict() for o in self.alleles],
            "haplotypes": [o.as_dict() for o in self.haplotypes],
            "genotypes": [o.as_dict() for o in self.genotypes],
            "identifier_id_map": identifier_id_map,
            "relationships": {
                "classes": {},
                "relations": {
                    "<class>": []
                }
            }
        }
        return doc


    def from_vmc(self):
        pass


    def scratch(self):
        b1 = Allele(seq_id(sr, a1.seqref), a1.location, a1.replacement)
        b2 = Allele(seq_id(sr, a2.seqref), a2.location, a2.replacement)
        
        import uuid
        s = 0
        def faa():
            """fetch-and-add"""
            global s
            s += 1
            return s

        id_functions = {
            'uuid': lambda o: str(uuid.uuid4()),
            'digest': lambda o: str(o.digest())[-10:],
            'ci': lambda o: str(o.computed_identifier()),
            'serial': lambda o: "VMC_{:06d}".format(faa())
        }
        id_function = "uuid"
