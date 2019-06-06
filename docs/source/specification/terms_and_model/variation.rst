.. _variation:

Variation
!!!!!!!!!

**Biological definition**

In biology, variation is often used to mean `genetic variation`_, describing the differences observed in DNA among individuals.

**Computational definition**

The *Variation* abstract class is the top-level object in the :ref:`VR Object Graph <vr-object-graph>` and represents the concept of a molecular state observation. The representation and types of molecular states are widely varied, and there are several :ref:`planned-variation` currently under consideration to capture this diversity. The primary Variation subclass defined by the VR |version| specification is the :ref:`Allele`, with the :ref:`text` subclass for capturing other Variations that are not yet covered.

.. _allele:

Allele
@@@@@@

**Biological definition**

One of a number of alternative forms of the same gene or same genetic locus. In the context of biological sequences, “allele” refers to a set of specific changes within a :ref:`Sequence`, including sets with zero (no change), one change (a simple allele), or multiple changes (:ref:`var-sets`). In the context of VR, Allele refers to a Sequence or Sequence change with respect to a reference sequence.

**Computational definition**

An Allele is a specific, single, and contiguous :ref:`Sequence` at a :ref:`Location`. Each alternative Sequence may be empty, shorter, longer, or the same length as the interval (e.g., due to one or more indels).

**Information model**

.. csv-table::
   :header: Field, Type, Label, Description
   :align: left
   :widths: 12, 9, 10, 30

   id, :ref:`Id`, optional, Allele identifier; must be unique within document
   location, :ref:`Location`, required, Where Allele is located
   state, :ref:`State`, required, Sequence at location

**Implementation guidance**

* Implementations MUST require that interval.end ≤ sequence_length when the Sequence length is known.
* The implementation MAY infer the Sequence by location_id and the Sequence State type, and ensure compatibility between them. This behavior is not included in the specification.
* Alleles are equal only if the component fields are equal: at the same location and with the same state.
* Alleles may have multiple related representations on the same Sequence type due to shifting (aka shuffling, normalization). A future version of VMC will provide a general framework for flexibly declaring various notions of pairwise Allele relationships.

**Notes**

* When the alternate Sequence is the same length as the interval, the lengths of the reference Sequence and imputed Sequence are the same. (Here, imputed sequence means the sequence derived by applying the Allele to the reference sequence.) When the replacement Sequence is shorter than the length of the interval, the imputed Sequence is shorter than the reference Sequence, and conversely for replacements that are larger than the interval.
* When the replacement is “” (the empty string), the Allele refers to a deletion at this location.
* The Allele entity is based on Sequence and is intended to be used for intragenic and extragenic variation. Alleles are not explicitly associated with genes or other features.
* Alleles may have multiple representations on the same Sequence type due to shifting (aka shuffling, normalization). Fully resolving such equivalences is beyond the scope of the first phase of this specification.
* Biologically, referring to Alleles is typically meaningful only in the context of empirical alternatives. For modelling purposes, Alleles may exist as a result of biological observation or computational simulation, i.e., virtual Alleles.
* “Single, contiguous” refers the representation of the Allele, not the biological mechanism by which it was created. For instance, two non-adjacent single residue Alleles could be represented by a single contiguous multi-residue Allele.
* The terms "allele" and "variant" are often used interchangeably, although this use may mask subtle distinctions made by some users.
   * In the genetics community, "allele" may also refer to a haplotype.
   * "Allele" connotes a state whereas "variant" connotes a change between states. This distinction makes it awkward to use variant to refer to the concept of an unchanged position in a Sequence and was one of the factors that influenced the preference of “Allele” over “Variant” as the primary subject of annotations.
   * See :ref:`Use “Allele” rather than “Variant” <use-allele>` for further details.
* When a trait has a known genetic basis, it is typically represented computationally as an association with an Allele.
* The VMC definition of Allele applies to all Sequence types (DNA, RNA, AA).


.. _text:

Text
@@@@

**Biological definition**

None

**Computational definition**

The *Text* subclass of :ref:`Variation` is intended to capture textual descriptions of variation that cannot be parsed by other Variation subclasses, but are still treated as variation.

**Implementation guidance**

* An implementation MUST represent Variation with subclasses other than Text if possible.
* An implementation SHOULD define or adopt conventions for defining the strings stored in Text.definition.
* If a future version of VR-Spec is adopted by an implementation and the new version enables defining existing Text objects under a different Variation subclass, the implementation MUST construct a new object under the other Variation subclass. In such a case, an implementation SHOULD persist the original Text object and respond to queries matching the Text object with the new object.

**Notes**

* Additional Variation subclasses are continually under consideration. Please open a `GitHub issue`_ if you would like to propose a Variation subclass to cover a needed variation representation.

.. _GitHub issue: https://github.com/ga4gh/vr-spec/issues
.. _genetic variation: https://en.wikipedia.org/wiki/Genetic_variation