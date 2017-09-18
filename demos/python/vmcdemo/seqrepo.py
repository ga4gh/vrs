"""Uses SeqRepo (https://github.com/biocommons/biocommons.seqrepo) to
translate assigned identifiers (e.g., NC_000019.10 assigned by NCBI)
to VMC sequence digests (e.g.,
VMC:GS_IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl).

Although the VMC proposal requires sequence digests of the form
'VMC:GS_...', implementers are free to write the code to generate
these ids themselves.  The VMC demo uses SeqRepo because it includes
VMC digests in a lookup table.

"""

import os

import biocommons.seqrepo


SEQREPO_ROOT_DIR = os.environ.get("SEQREPO_ROOT_DIR", "/usr/local/share/seqrepo")
SEQREPO_INSTANCE_NAME = os.environ.get("SEQREPO_INSTANCE", "master")
seqrepo_instance_path = os.path.join(SEQREPO_ROOT_DIR, SEQREPO_INSTANCE_NAME)

_sr = biocommons.seqrepo.SeqRepo(seqrepo_instance_path)


def get_vmc_sequence_id(ir):
    """return VMC sequence Id (string) for a given Identifier from another namespace

    >>> ir = models.Identifier(namespace="NCBI", accession="NC_000019.10")
    >>> get_vmc_sequence_id(ir)
    'VMC:GS_IIB53T8CNeJJdUqzn9V_JnRtQadwWCbl'

    """

    r = _sr.aliases.find_aliases(namespace=ir.namespace, alias=ir.accession).fetchone()
    if r is None:
        raise KeyError(ir)

    rows = _sr.aliases.find_aliases(seq_id=r["seq_id"], namespace="VMC").fetchall()
    if len(r) == 0:
        raise RuntimeError("No VMC digest for {ir}".format(ir=ir))
    r = rows[0]

    return "{r[namespace]}:{r[alias]}".format(r=r)
