Design Decisions
################

VR contributors confronted numerous trade-offs in developing this specification. As these trade-offs may not be apparent to outside readers, this section highlights the most significant ones and the rationale for our design decisions, including:

* Use “Allele” rather than “Variant”
* Alleles must be right normalized
* Sequence ranges use an interbase coordinate system
* Modeling Language
* Serialization Options

.. _use-allele:

Allele Rather than Variant
**************************
The most primitive sequence assertion in VR is the :ref:`Allele` entity. Colloquially, the words "allele" and "variant" have similar meanings and they are often used interchangeably. However, the VR contributors believe that it is essential to distinguish the state of the sequence from the change between states of a sequence. It is imperative that precise terms are used when modeling data. Therefore, within VR, Allele refers to a state and "variant" refers to the change from one Allele to another.

The word "variant", which implies change, makes it awkward to refer to the (unchanged) reference allele. Some systems will use an HGVS-like syntax (e.g., NC_000019.10:g.44906586G>G or NC_000019.10:g.44906586=) when referring to an unchanged residue. In some cases, such "variants" are even associated with allele frequencies. Similarly, a predicted consequence is better associated with an allele than with a variant.

.. _right-normalize:

****************************
Alleles are Right Normalized
****************************

**TODO: update to discuss our WIP of SPDI algorithm (BOCA)**

In order to standardize the presentation of sequence variation, the VR specification requires that Alleles be right normalized (aka shifted or shuffled) using the `vt algorithm`_. Furthermore, normalization rules should be identical for all sequence types; although this need not be a strict requirement, there is no reason to normalize in different directions based on sequence type.

The choice of algorithm was relatively straightforward: vt is well-documented, published, easily understood, easily implemented, and covers a wide-range of cases.

The choice to right normalize is more contentious. The HGVS nomenclature recommendations, originally published in 1998, require that alleles be right normalized `(3' rule)`_ on all sequence types. The Variant Call Format (VCF), released as a PDF specification in 2009, made the conflicting choice to write variants `left (5') normalized`_ and anchored with the previous nucleotide.

Several factors contributed to requiring right alignment in VR:
* Right-normalized alleles on transcript and protein sequences are likely closer to their biological consequences than their left-normalized counterparts. By convention, sequences are written in the order of biological processing: 5'-to-3' for genomic sequences and for transcript sequences (regardless of strand), and N-to-C for protein sequences. Broadly speaking and with exceptions, the consequences of variation occur on the downstream end of processing. For example, a right-shifted insertion allele that induces a downstream stop codon is always closer to the consequence (termination of transcription) than its left-shifted counterpart.
* Related to, but distinct from, the above factor is that it is often easier for humans to understand certain sequence changes at their downstream locations. For example, most biologists likely imagine a trinucleotide repeat as extending from the downstream end rather than being inserted upstream. While the information content is clearly the same regardless of the mechanism or representation, there is nonetheless a strong bias toward envisioning variation on the rightmost position.
While consistency with Alleles written according HGVS recommendations was not a factor, it is an advantage of this design choice.


.. _interbase-coordinates-design:

Interbase Coordinates
*********************

Sequence ranges use an interbase coordinate system. Interbase coordinate conventions are used in this terminology because they provide conceptual consistency that is not possible with residue-based systems.

.. important:: The choice of what to count–residues versus inter-residue positions–has significant semantic implications for coordinates. Because interbase coordinates and the corresponding 0-based residue-counted coordinates are numerically identical in some circumstances, uninitiated readers often conflate the choice of numerical base with the choice of residue or inter-residue counting. Whereas the choice of numerical base is inconsequential, the semantic advantages of interbase are significant.

When humans refer to a range of residues within a sequence, the most common convention is to use an interval of ordinal residue positions in the sequence. While natural for humans, this convention has several shortcomings when dealing with sequence variation.

For example, interval coordinates are interpreted as exclusive coordinates for insertions, but as inclusive coordinates for substitutions and deletions; in effect, the interpretation of coordinates depends on the variant type, which is an unfortunate coupling of distinct concepts.

.. _modeling-language:

*****************
Modeling Language
*****************

The VR collaborators investigated numerous options for modeling data, generating code, and writing the wire protocol. Required and desired selection criteria included:

* language-neutral -- or at least C/C++, java, python
* high-quality tooling/libraries
* high-quality code generation
* documentation generation
* supported constructs and data types
   * typedefs/aliases
   * enums
   * lists, maps, and maps of lists/maps
   * nested objects
* protocol versioning (but not necessarily automatic adaptation)

Initial versions of the VR logical model were implemented in UML, protobuf, and swagger/OpenAPI, and JSON Schema. We have implemented our schema in JSON Schema. Nonetheless, it is anticipated that some adopters of the VR logical model may implement the specification in other protocols.

.. _custom-serialization:

**********************
Serialization Strategy
**********************

There are many packages and proposals that aspire to a canonical form for json in many languages. Despite this, there are no ratified or *de facto* winners. Many packages have similar names, which makes it difficult to discern whether they are related or not (often not). Although some packages look like good single-language candidates, none are ready for multi-language use. Many seem abandoned. The need for a canonical json form is evident, and there was at least one proposal for an ECMA standard.

Therefore, we implemented our own :ref:`serialization format <serialization>`, which is very similar to `Gibson Canonical JSON`_ (not to be confused with `OLPC Canonical JSON`_).

.. _vt algorithm: https://genome.sph.umich.edu/wiki/Variant_Normalization#Algorithm_for_Normalization
.. _(3' rule): https://varnomen.hgvs.org/recommendations/general/
.. _left (5') normalized: https://genome.sph.umich.edu/wiki/Variant_Normalization#Definition
.. _Gibson Canonical JSON: http://gibson042.github.io/canonicaljson-spec/
.. _OLPC Canonical JSON: http://wiki.laptop.org/go/Canonical_JSON