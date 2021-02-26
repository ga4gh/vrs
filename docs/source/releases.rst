Releases
!!!!!!!!

.. note:: VRS follows `Semantic Versioning 2.0 <http://semver.org/>`_.  For a version
   number MAJOR.MINOR.PATCH:

     * MAJOR version is incremented for incompatible API changes.
     * MINOR version is incremented for new, backwards-compatible
       functionality. For VRS, this means changes that add support for
       new types of variation or extend existing types.
     * PATCH version is incremented for bug fixes. For VRS, examples
       are clarifications of documentation and bug fixes on property
       constraints.  No changes to information models will occur in
       PATCH releases.

   All planned work The `VRS Roadmap
   <https://github.com/orgs/ga4gh/projects/5>`__ for upcoming
   developments. All currently planned work will be MINOR updates
   according to the guidelines above.


1.1
@@@


1.1.2
#####

This patch version makes the following corrections and clarifications:

  * Adds the intended ChromosomeLocation prefix to the Computed Identifiers
    table.
  * Revises the Cytoband information model to align with ISCN conventions.
  * Updates the Cytoband regex to match the specified model.


1.1.1
#####

This patch version makes the following corrections and clarifications:

  * Correct styling / indexing of CytobandLocation in restructuredText to match
    the current Schema and ER Diagram.
  * Remove erroneous bracket notation after CURIE from the `locations` attribute
    in the :ref:`Allele` information model.
  * Added citation for sha512t24u and truncated digest collision analysis.
  * Revised Note in inter-residue design decision to acknowledge community terms.

1.1.0
#####

1.1.0 is the second release of VRS.

New classes
$$$$$$$$$$$

  * ChromosomeLocation: A region of a chromosomed specified by species
    and name using cytogenetic naming conventions
  * CytobandInterval: A contiguous region specified by chromosomal bands features.
  * Haplotype: A set of zero or more Alleles.
  * VariationSet: A set of Variation objects.

Other data model changes
$$$$$$$$$$$$$$$$$$$$$$$$

  * Interval was renamed to SequenceInterval. Interval was an internal
    class that was never instantiated, so this change should not be
    visiable to users.

Documentation changes
$$$$$$$$$$$$$$$$$$$$$

  * Added :ref:`relationships` to describe how VRS relates to other
    standards.
  * Updated :ref:`normalization` to clarify handling of reference
    alleles and generalize terminology to apply to all VRS objects.
  * Updated current and future schema diagrams.
  * Included a discussion of the :ref:`release-cycle`.



1.0
@@@

1.0.0
#####

VRS 1.0.0 was the first public release of the Variation Representation Specification.
