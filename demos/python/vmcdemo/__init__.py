# flake8: noqa
"""vmcdemo -- public interface to vmcdemo

Most callers should use something like this:

>>> from vmcdemo import models, computed_id, serialize

"""


from ._models import models, schema_path
from .digest import computed_id, computed_identifier, truncated_digest, serialize
from .seqrepo import get_vmc_sequence_id
