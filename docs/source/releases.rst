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

  * ChromosomeLocation:
  * CytobandInterval
  * Haplotype
  * VariationSet

Other data model changes
########################

  * Interval was renamed to SequenceInterval. Interval is an abstract
    that is never directly instantiated, so this internal
    implementation change should not be visiable to users.

Documentation changes
#####################

  * Added relationships.rst
  * Normalization: generalization, ref alleles,  .  Design decisions, computed identifiers , 
  * Updated figures
  * Development process & release cycle



1.0
@@@

VRS 1.0 provides a machine-readable specification for:

  * Sequence Location
  * Alleles
  * Text (Variation)

