import biocommons.seqrepo

_sr = biocommons.seqrepo.SeqRepo("/usr/local/share/seqrepo/master")


def get_vmc_sequence_id(ir):
    r = _sr.aliases.find_aliases(namespace=ir.namespace, alias=ir.accession).fetchone()
    if r is None:
        raise KeyError(ir)
    return "VMC:GS_" + r["seq_id"]
