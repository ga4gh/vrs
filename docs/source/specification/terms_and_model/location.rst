.. _location:

Location
!!!!!!!!
Biological definition
---------------------
As used by biologists, the precision of
“location” (or “locus”) varies widely; examples include chromosomal
bands, named genomic features (e.g., genes, exons, or markers), or
specific positions on a reference sequence.

Computational definition
------------------------
A Location is an abstract class that
refer to contiguous regions of biological sequences. Universally, a
Location is an identifiable position or region on a :ref:`Sequence`,
defined by a Sequence :ref:`Id` and related information, which varies
by Location subclass. Concrete types of Locations are described
below. The most common Location is a :ref:`SequenceLocation
<sequence-location>`, i.e., a Location based on a named sequence and
an Interval on that sequence. Additional planned location classes (see
:ref:`planned-locations`) may also be conceptual or symbolic
locations, such as a cytoband region or a gene. Any of these may be
used as the Location for Variation.

.. _sequence-location:

SequenceLocation
@@@@@@@@@@@@@@@@

Computational definition
------------------------
A Location subclass for describing a defined Interval over a named sequence.

Information model
-----------------

.. csv-table::
   :header: Field, Type, Label, Description
   :align: left
   :widths: 12, 9, 10, 30

   id, :ref:`Id`, optional, Location Id; must be unique within document
   sequence_id, :ref:`Id`, required, An id mapping to the Identifier of the external database Sequence
   interval, :ref:`Interval`, required, Position of feature on reference sequence specified by sequence_id.

Implementation guidance
-----------------------

* For a :ref:`Sequence` of length *n*:
   * 0 ≤ *interval.start* ≤ *interval.end* ≤ *n*
   * interbase coordinate 0 refers to the point before the start of the Sequence
   * interbase coordinate n refers to the point after the end of the Sequence.
* VR requires that coordinates refer to valid Sequence. VR does not
  support referring to intronic positions within a transcript
  sequence, extrapolations beyond the ends of sequences, or other
  implied sequence.

.. important:: HGVS permits variants that refer to non-existent
               sequence. Examples include coordinates extrapolated
               beyond the bounds of a transcript and intronic
               sequence. Such variants are not representable using VR
               and must be projected to a genomic reference in order
               to be represented.
