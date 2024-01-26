Datatypes & Classes
@@@@@@@@@@@@@@@@@@@

The VRS specification defines a set of datatypes that are used for the data class elements. There are four categories of datatypes:

1. The base abstract types that provide the foundation for all types.
2. Simple / primitive types, which are single elements with a primitive value.
3. General-purpose complex types, which are re-usable clusters of elements.
4. Special purpose datatypes - defined elsewhere in the specification for specific usages.

The VRS data classes are the identifiable entities that are used to represent biological entities. These are defined in the :ref:`data_classes` section.

These are the identifiable classes in scope for VRS:

* SequenceLocation
* Allele
* Haplotype
* CopyNumberCount
* CopyNumberChange
* Genotype

.. toctree::
  :maxdepth: 2
  :includehidden:

  base_types
  primitives
  general_purpose
  special_purpose
  classes
    