.. _location:

Location
!!!!!!!!

**Biological definition**

As used by biologists, the precision of “location” (or “locus”) varies
widely, ranging from precise start and end numerical coordinates
defining a Location, to bounded regions of a sequence, to conceptual
references to named genomic features (e.g., chromosomal bands, genes,
exons) as proxies for the Locations on an implied reference sequence.

**Computational definition**

The `Location` abstract class refers to position of a contiguous
segment of a biological sequence.  The most common and concrete
Location is a :ref:`sequence-location`, i.e., a Location based on a
named sequence and an Interval on that sequence. Additional
:ref:`planned-locations` may also be conceptual or symbolic locations,
such as a cytoband region or a gene. Any of these may be used as the
Location for Variation.

**Implementation Guidance**

* Location refers to a position.  Although it may imply a sequence,
  the two concepts are not interchangable, especially when the
  location is non-specific (e.g., a range) or symbolic (a gene).


.. _sequence-location:

SequenceLocation
@@@@@@@@@@@@@@@@

**Biological definition**

None

**Computational definition**

A Location subclass for describing a defined :ref:`Interval` over a
named :ref:`Sequence`.

**Information model**

.. csv-table::
   :header: Field, Type, Label, Description
   :align: left
   :widths: 12, 9, 10, 30

   id, :ref:`Id`, optional, Location Id; must be unique within document
   type, string, required, Location type; must be set to 'SequenceLocation'
   sequence_id, :ref:`Id`, required, An id mapping to the Identifier of the external database Sequence
   interval, :ref:`Interval`, required, Position of feature on reference sequence specified by sequence_id.

**Implementation guidance**

* For a :ref:`Sequence` of length *n*:
   * 0 ≤ *interval.start* ≤ *interval.end* ≤ *n*
   * interbase coordinate 0 refers to the point before the start of the Sequence
   * interbase coordinate n refers to the point after the end of the Sequence.
* Coordinates MUST refer to a valid Sequence. VR does not support
  referring to intronic positions within a transcript sequence,
  extrapolations beyond the ends of sequences, or other implied
  sequence.

.. important:: HGVS permits variants that refer to non-existent
               sequence. Examples include coordinates extrapolated
               beyond the bounds of a transcript and intronic
               sequence. Such variants are not representable using VR
               and must be projected to a genomic reference in order
               to be represented.
