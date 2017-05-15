import biocommons.seqrepo

_sr = biocommons.seqrepo.SeqRepo("/usr/local/share/seqrepo/master")


def get_vmc_sequence_id(ir):
    # TODO: seqrepo will switch to no case squashing at somepoint :-(

    # TODO: This uses the fact that we know that seqrepo uses a
    # truncated digest (SHA512/24) for sequence identfiers.  This
    # should be treated as a private implementation detail.  For that
    # to happen, seqrepo needs to rename the `sh` namespace to
    # `sha512t24` or somesuch.

    r = _sr.aliases.find_aliases(namespace=ir.namespace.lower(), alias=ir.accession).fetchone()
    return "VMC:GS_" + r["seq_id"]
