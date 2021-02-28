.. _equivalence:

Equivalence Between Concepts
!!!!!!!!!!!!!!!!!!!!!!!!!!!!
VRS allows for the expressive representation of variation
concepts. Sometimes this allows for forms that can be reduced from one
to another, and sometimes bi-directionally. Examples of this include the
bi-directional translation of chromosomal bands to sequence coordinates
via a sequence-band mapping, the uni-directional translation of a gene
to one or more sequence location(s), and the use of different
:ref:`SequenceExpression` instances that would resolve to the same sequence.
Similarly, authority-based concepts such as :ref:`Gene` are entirely
dependent on the definition of the concept by that authority–we provide
no guidance on how to translate or relate such concepts to one another.

We provide no guidance or mechanism to enforce "equivalence" between
these concepts, because the semantics of one representation to another
are distinct, even when there exists functions that equate or translate
between two distinct concepts. Instead, we encourage communities to adopt
policies about *how* and *when* to use the various concepts provided by
VRS to represent different forms of variation. To assist in that effort,
the GA4GH Genomic Knowledge Standards Work Stream is developing a
specification for resource-defined Variation Concept Origination Policies
(VCOPs). You can learn more about VCOPs in the `VRSATILE`_ framework.
