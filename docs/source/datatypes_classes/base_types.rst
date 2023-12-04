VRS Type Framework
@@@@@@@@@@@@@@@@@@

The VRS Type Framework is a set of classes that can be used to create 
VRS data classes that can be used to represent variation and location
data. It uses core elements of the GKS Common Framework as a foundation.

    entity
    value_object


.. _Location:

Location
########

As used by biologists, the precision of "location" (or "locus") varies
widely, ranging from precise start and end numerical coordinates
defining a Location, to bounded regions of a sequence, to conceptual
references to named genomic features (e.g., chromosomal bands, genes,
exons) as proxies for the Locations on an implied reference sequence.

The most common and concrete Location is a :ref:`SequenceLocation`, i.e.,
a Location based on a named sequence and an Interval on that sequence. Other 
types of Location may be added based on community need.

.. include:: defs/Location.rst

**Implementation Guidance**

* Location refers to a position.  Although it MAY imply a sequence,
  the two concepts are not interchangeable, especially when the
  location is non-specific (e.g., specified one or more ambiguous endpoints).
  To represent a sequence derived from a Location, see
  :ref:`SequenceExpression`.


.. _Variation:

Variation
#########

In the genetics community, variation is often used to mean *sequence*
variation, describing the differences observed in DNA or AA bases among
individuals, and typically with respect to a common reference sequence.

In VRS, the Variation class is the conceptual root of all types of biomolecular
variation, and the *Variation* abstract class is the top-level object in
the :ref:`vr-schema-diagram`. Variation types are broadly categorized as
:ref:`MolecularVariation`, :ref:`SystemicVariation`, or a :ref:`utility
subclass <utilityvariation>`. Types of variation are widely varied, and
there are several :ref:`planned-variation` currently under consideration
to capture this diversity.

.. include:: defs/Variation.rst

.. _MolecularVariation:

Molecular Variation
$$$$$$$$$$$$$$$$$$$

.. include:: defs/MolecularVariation.rst

.. _SystemicVariation:

Systemic Variation
$$$$$$$$$$$$$$$$$$

.. include:: defs/SystemicVariation.rst


