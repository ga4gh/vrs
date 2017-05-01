import json

import pkg_resources
import sqlitedict

from .. import models


cache_path = pkg_resources.resource_filename(__name__, "_data/testdb.sqlite")


class DB:
    pass


db = DB()
db.locations = sqlitedict.SqliteDict(
    cache_path, autocommit=True, encode=lambda o: json.dumps(o.marshal()),
    tablename="locations",  decode=lambda s: models.Allele.unmarshal(json.loads(s)))
db.alleles = sqlitedict.SqliteDict(
    cache_path, autocommit=True, encode=lambda o: json.dumps(o.marshal()),
    tablename="alleles",  decode=lambda s: models.Allele.unmarshal(json.loads(s)))
db.haplotypes = sqlitedict.SqliteDict(
    cache_path, autocommit=True, encode=lambda o: json.dumps(o.marshal()),
    tablename="haplotypes",  decode=lambda s: models.Haplotype.unmarshal(json.loads(s)))
db.genotypes = sqlitedict.SqliteDict(
    cache_path, autocommit=True, encode=lambda o: json.dumps(o.marshal()),
    tablename="genotypes",  decode=lambda s: models.Genotype.unmarshal(json.loads(s)))
