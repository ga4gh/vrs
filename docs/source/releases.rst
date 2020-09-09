Releases
!!!!!!!!

.. note:: VRS follows `Semantic Versioning 2.0 <http://semver.org/>`_.  For a version
   number MAJOR.MINOR.PATCH:

     * MAJOR version is incremented for incompatible API changes;
     * MINOR version is incremented for new, backwards-compatible functionality;
     * PATCH version is incremented for bug fixes.

   The `VRS Roadmap <https://github.com/orgs/ga4gh/projects/5>`__ for
   upcoming developments.


1.1
@@@

1.1 is the second release of VRS.


New classes
############

  * ChromosomeLocation: A region of a chromosomed specified by species
    and name using cytogenetic naming conventions
  * CytobandInterval: A contiguous region specified by chromosomal bands features.
  * Haplotype: A set of zero or more Alleles.
  * VariationSet: A set of Variation objects.

Other data model changes
########################

  * Interval was renamed to SequenceInterval. Interval was an internal
    class that was never instantiated, so this change should not be
    visiable to users.

Documentation changes
#####################

  * Added :ref:`relationships` to describe how VRS relates to other
    standards.
  * Updated :ref:`normalization` to clarify handling of reference
    alleles and generalize terminology to apply to all VRS objects.
  * Updated current and future schema diagrams.
  * Included a discussion of the :ref:`release-cycle`.



1.0
@@@

VRS 1.0 was the first public release of the Variation Representation Specification.
