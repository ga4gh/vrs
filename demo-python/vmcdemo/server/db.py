import json

import pkg_resources
import sqlitedict

from .. import models
from .. import digest

cache_path = pkg_resources.resource_filename(__name__, "_data/testdb.sqlite")


class DB:
    def __init__(self):
        self.locations = sqlitedict.SqliteDict(
            cache_path, autocommit=True, encode=lambda o: json.dumps(o.marshal()),
            tablename="locations",  decode=lambda s: models.Location.unmarshal(json.loads(s)))
        self.alleles = sqlitedict.SqliteDict(
            cache_path, autocommit=True, encode=lambda o: json.dumps(o.marshal()),
            tablename="alleles",  decode=lambda s: models.Allele.unmarshal(json.loads(s)))
        self.haplotypes = sqlitedict.SqliteDict(
            cache_path, autocommit=True, encode=lambda o: json.dumps(o.marshal()),
            tablename="haplotypes",  decode=lambda s: models.Haplotype.unmarshal(json.loads(s)))
        self.genotypes = sqlitedict.SqliteDict(
            cache_path, autocommit=True, encode=lambda o: json.dumps(o.marshal()),
            tablename="genotypes",  decode=lambda s: models.Genotype.unmarshal(json.loads(s)))
        self.ididentifiermap = sqlitedict.SqliteDict(
            cache_path, autocommit=True, encode=lambda m: json.dumps([o.marshal() for o in m]),
            tablename="ididentifiers",  decode=lambda s: [models.Identifier.unmarshal(s) for s in json.loads(s)])

    def add_id_identifiers(self, id, identifiers):
        v = self.ididentifiermap.get(id, [])
        v.extend(identifiers)
        db.ididentifiermap[id] = v
        return v

    def commit(self):
        self.locations.commit()
        self.alleles.commit()
        self.haplotypes.commit()
        self.genotypes.commit()
        self.ididentifiermap.commit()


db = DB()


def load_test_data(db):
    import biocommons.seqrepo
    sr = biocommons.seqrepo.SeqRepo("/usr/local/share/seqrepo/master")

    def _nsa_to_gs(sr, ns, a):
        """return VMC GS identifier for namespace:alias string in seqrepo

        SeqRepo currently (0.3.x) uses lowercase namespaces. This was
        a mistake and will change to standardize identifier use.
        SeqRepo also doesn't currently have GS ids, so we synthesize
        it from the *internal* id (which we shouldn't do).

        """
        r = sr.aliases.find_aliases(namespace=ns.lower(), alias=a).fetchone()
        return models.Identifier(namespace="VMC", accession="GS_" + r["seq_id"])

    for nsa in ["NCBI:NC_000019.10"]:
        ns, a = nsa.split(":")
        vmc_ident = _nsa_to_gs(sr, ns, a)
        vmc_id = vmc_ident.namespace + ":" + vmc_ident.accession
        identifiers = [vmc_ident, models.Identifier(namespace=nsa, accession=a)]
        db.add_id_identifiers(vmc_id, identifiers)

    sid = digest.format(_nsa_to_gs(sr, "NCBI", "NC_000019.10"))
    l = models.Location(
        sequence_id = sid,
        position = models.Position(
            type = "INTERVAL",
            value = models.Interval(start=44908683, end=44908684)
            ))
    l.id = digest.format(digest.computed_identifier(l))
    db.locations[l.id] = l
    db.add_id_identifiers(l.id, [models.Identifier(namespace="dbSNP", accession="rs429358")])

    l = models.Location(
        sequence_id = sid,
        position = models.Position(
            type = "INTERVAL",
            value = models.Interval(start=44908821, end=44908822)
            ))
    l.id = digest.format(digest.computed_identifier(l))
    db.locations[l.id] = l
    db.add_id_identifiers(l.id, [models.Identifier(namespace="dbSNP", accession="rs7412")])
