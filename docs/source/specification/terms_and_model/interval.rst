.. _interval:

Interval
!!!!!!!!

.. todo::

   Update to include simple interval and nested interval

**Biological definition:** None.

**Computational definition:** Two integers that define the start and
 end positions of a range of residues, possibly with length zero, and
 specified using interbase coordinates.

**Information model**

.. csv-table::
   :header: Field, Type, Label, Description
   :align: left

   start, uint64, required, start position
   end, uint64, required, end position

**Implementation guidance**

* Implementations MUST require that 0 ≤ start ≤ end. In the case of
  double-stranded DNA, this constraint holds even when a feature is on
  the complementary strand.

**Notes**

* VR uses Interbase coordinates because they provide conceptual
  consistency that is not possible with residue-based systems (see
  :ref:`rationale <interbase-coordinates-design>`). Implementations
  `will need to convert`_ between interbase and 1-based inclusive
  residue coordinates familiar to most human users.
* Interbase coordinates start at 0 (zero).
* The length of an interval is *end - start*.
* An interval in which start == end is a zero width point between two residues.
* An interval of length == 1 may be colloquially referred to as a position.
* Two intervals are *equal* if the their start and end coordinates are equal.
* Two intervals *intersect* if the start or end coordinate of one is
  strictly between the start and end coordinates of the other. That
  is, if:

   * b.start < a.start < b.end OR
   * b.start < a.end < b.end OR
   * a.start < b.start < a.end OR
   * a.start < b.end < a.end
* Two intervals a and b *coincide* if they intersect or if they are
  equal (the equality condition is required to handle the case of two
  identical zero-width Intervals).

**Examples**

* <start, end>=<*0,0*> refers to the point with width zero before the first residue.
* <start, end>=<*i,i+1*> refers to the *i+1th* (1-based) residue.
* <start, end>=<*N,N*> refers to the position after the last residue for Sequence of length *N*.
* See `Interbase Interval tests`_ in the VR-python repo for a diagram and examples.

.. _will need to convert: https://www.biostars.org/p/84686/
.. _Interbase Interval tests: https://github.com/ga4gh/vr-python/blob/master/notebooks/archive/Interbase%20Interval%20tests.ipynb
