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

.. _using-sequence-expressions:

Using Sequence Expressions
@@@@@@@@@@@@@@@@@@@@@@@@@@
When using Sequence Expressions, our general recommendation is to use
:ref:`LiteralSequenceExpression` for when the precise sequence state is of
importance to the Variation concept; this is the most common use case.
When the precise state is not important but instead it is desired to refer
to the general sequence derived from a location on a reference sequence, we
recommend using a :ref:`DerivedSequenceExpression`; this is typically used
when describing large sequences that are approximately reference for use in
some large-scale :ref:`MolecularVariation` or :ref:`SystemicVariation` concepts.
:ref:`RepeatedSequenceExpression` is typically used for the semantic importance
of describing a specific, repeated subsequence *by count*, such as description
of CAG repeats in the *ATXN7* gene, where the repeat count is a diagnostic
biomarker for severe neurodegenerative disorder spinocerebellar ataxia type 7 [1]_.

.. [1] Bettencourt C, Hensman-Moss D, Flower M, et al. DNA repair pathways underlie
       a common genetic mechanism modulating onset in polyglutamine diseases. *Ann
       Neurol*. 2016;79(6):983-990. `doi:10.1002/ana.24656`_

.. _`doi:10.1002/ana.24656`: https://doi.org/10.1002/ana.24656