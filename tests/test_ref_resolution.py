"""The GA4GH ``$ref`` fallback resolver must accept the hyphenated ballot
version token (e.g. ``2.1.1-ballot.2026-09.1``) for both VRS and imported
gkm-core refs.

Normal validation resolves ``$ref``s in-memory via each schema's ``$id``, so
``config.retrieve_rel_ref`` is otherwise never exercised. This guards it
directly against the version-token parser and the schema-directory lookup.
"""
import pytest

from config import retrieve_rel_ref


@pytest.mark.parametrize(
    "ref, expected_class",
    [
        # bare absolute-path ref (VRS, hyphenated ballot version)
        ("/ga4gh/schema/vrs/2.1.1-ballot.2026-09.1/json/SequenceReference",
         "SequenceReference"),
        # fully-qualified w3id URL form
        ("https://w3id.org/ga4gh/schema/vrs/2.1.1-ballot.2026-09.1/json/SequenceLocation",
         "SequenceLocation"),
        # imported module whose name AND version both contain hyphens
        ("/ga4gh/schema/gkm-core/1.3.0-ballot.2026-09.1/json/Extension",
         "Extension"),
    ],
)
def test_retrieve_rel_ref_accepts_ballot_version(ref, expected_class):
    resource = retrieve_rel_ref(ref)
    assert resource.contents["$id"].endswith(f"/json/{expected_class}")


def test_retrieve_rel_ref_rejects_non_ga4gh_ref():
    with pytest.raises(ValueError):
        retrieve_rel_ref("https://example.org/not/a/ga4gh/ref")
