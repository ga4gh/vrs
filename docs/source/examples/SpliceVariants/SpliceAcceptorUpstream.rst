Splice acceptor — upstream intronic variant
===========================================

This example demonstrates how a splice-adjacent intronic HGVS variant is represented using ``RelativeAllele``. The variant occurs immediately upstream of a splice acceptor site and is expressed using HGVS c. notation.

HGVS expression
---------------

We will use the following HGVS expression from ClinVar: `NM_005188.4(CBL):c.1096-1G>C <https://www.ncbi.nlm.nih.gov/clinvar/variation/45196/>`_.

This expression specifies a single-nucleotide variant one base upstream of the coding exon boundary, placing the variant in the intron adjacent to a splice acceptor site.

Transcript context
------------------

`NCBI Reference Sequence: NM_005188.4 <https://www.ncbi.nlm.nih.gov/nuccore/NM_005188>`_

* Positive strand
* Splice acceptor (intron → exon boundary)
* Upstream intronic (intron side of the exon boundary)

Transcript features at the splice junction
------------------------------------------

The exon boundaries below provide the local transcript context used to interpret the splice-adjacent HGVS position in this example.

.. code-block::

  CDS            80..2800
  exon 7         1087..1174
                      /gene="CBL"
  exon 8        1175..1306
                      /gene="CBL"

NCBI graphical sequence view
----------------------------

The figure below shows the same region in the `NCBI Sequence Viewer <https://www.ncbi.nlm.nih.gov/nuccore/1732746290?report=graph&tracks=[key:sequence_track,name:Sequence,display_name:Sequence,id:STD649220238,annots:Sequence,ShowLabel:false,ColorGaps:false,shown:true,order:1][key:gene_model_track,name:Genes,display_name:Genes,id:STD3194982005,annots:Unnamed,Options:ShowAll,CDSProductFeats:true,NtRuler:true,AaRuler:true,HighlightMode:2,ShowLabel:true,shown:true,order:4][key:feature_track,name:Other features---polyA_site,display_name:polyA_site Features,id:STD3911386278,subkey:polyA_site,annots:Unnamed,shown:true,order:5][key:feature_track,name:Other features---regulatory,display_name:regulatory Features,id:STD2883984253,subkey:regulatory,annots:Unnamed,shown:true,order:22][key:SNP_track,name:T2973540,display_name:Cited Variations\, dbSNP b157 v2,id:T2973540,dbname:VDB,annots:NA000146873.21\232,Layout:Adaptive,shown:true,order:23]&mk=1175|1175|blue|9&v=1150:1199&c=FF6600&select=null&slim=0>`_, which displays transcript structure and exon boundaries aligned to the reference sequence.

.. figure:: ../../images/splice_variants/acceptor_upstream/ncbi_reference_sequence.png
  :alt:  NCBI Sequence Viewer showing the splice acceptor region in NM_005188.4
  :align: center
  :target: https://www.ncbi.nlm.nih.gov/nuccore/1732746290?report=graph&tracks=[key:sequence_track,name:Sequence,display_name:Sequence,id:STD649220238,annots:Sequence,ShowLabel:false,ColorGaps:false,shown:true,order:1][key:gene_model_track,name:Genes,display_name:Genes,id:STD3194982005,annots:Unnamed,Options:ShowAll,CDSProductFeats:true,NtRuler:true,AaRuler:true,HighlightMode:2,ShowLabel:true,shown:true,order:4][key:feature_track,name:Other features---polyA_site,display_name:polyA_site Features,id:STD3911386278,subkey:polyA_site,annots:Unnamed,shown:true,order:5][key:feature_track,name:Other features---regulatory,display_name:regulatory Features,id:STD2883984253,subkey:regulatory,annots:Unnamed,shown:true,order:22][key:SNP_track,name:T2973540,display_name:Cited Variations\, dbSNP b157 v2,id:T2973540,dbname:VDB,annots:NA000146873.21\232,Layout:Adaptive,shown:true,order:23]&mk=1175|1175|blue|9&v=1150:1199&c=FF6600&select=null&slim=0

  NCBI Sequence Viewer showing the splice acceptor region in NM_005188.4.

Anchor selection
----------------

To represent this variant, an anchor is chosen at the inter-residue position corresponding to the exon boundary referenced by the HGVS expression. For splice-acceptor variants, this anchor is placed at the start of the exon following the intron.

Anchor selection is determined by splice context and does not depend on transcript orientation. In this example, the exon start occurs at inter-residue position **1174**, which is used as the anchor.

The diagram below illustrates the selected anchor position relative to the exon boundary.

.. image:: ../../images/splice_variants/acceptor_upstream/anchor.drawio.svg
  :alt: Calculating interbase coordinates for anchor
  :align: center

Mapping relative to the anchor
------------------------------

Offsets are applied relative to the anchor to identify the transcript-relative inter-residue interval corresponding to the HGVS position.

Because the anchor represents the point at which an alignment gap occurs (e.g. an exon junction mapped to two sides of an intronic sequence), ``anchorOrientation`` is used to select which side of the anchor is used as the reference point. For this splice-acceptor variant, the anchor is oriented to the **right**, selecting the side of the anchor immediately following the intron-exon boundary.

Offsets are expressed in inter-residue coordinates. In this example, ``offsetStart = -1`` and ``offsetEnd = 0`` select the single inter-residue interval immediately upstream of the anchor, corresponding to the nucleotide referenced by the HGVS expression.

Transcript orientation is then used to map this inter-residue interval to the genomic reference.

In this example, the variant is described relative to the transcript reference sequence (``NM_005188.4``), where the reference base at the variant position is ``G``.

The variant state is therefore shown on the transcript as the **mapped state** (``G → C``), and on the corresponding genomic reference (``NC_000011.10``) as the **base state** (``G → C``). Because this transcript is on the positive strand, the two states are identical.

The diagram below illustrates the application of offsets relative to the anchor, the resolved inter-residue interval, and the relationship between the mapped and base states.

.. image:: ../../images/splice_variants/acceptor_upstream/mapping.drawio.svg
  :alt: mapping
  :align: center

The corresponding exon boundaries on the genomic reference are shown below for visual confirmation.

.. figure:: ../../images/splice_variants/acceptor_upstream/ucsc-exon7.png
  :alt: UCSC Exon 7
  :target: https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr11%3A119277843%2D119277845&hgsid=3614864995_0UVsBWmZuB39ETn9UTymrTkWBAiD

  `Exon 7 boundary in the UCSC Genome Browser <https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr11%3A119277843%2D119277845&hgsid=3614864995_0UVsBWmZuB39ETn9UTymrTkWBAiD>`_

.. figure:: ../../images/splice_variants/acceptor_upstream/ucsc-exon8.png
  :alt: UCSC Exon 8
  :target: https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr11%3A119278165%2D119278169&hgsid=3614864995_0UVsBWmZuB39ETn9UTymrTkWBAiD

  `Exon 8 boundary in the UCSC Genome Browser <https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr11%3A119278165%2D119278169&hgsid=3614864995_0UVsBWmZuB39ETn9UTymrTkWBAiD>`_

Relative Allele representation
------------------------------

Together, the anchor position and offsets resolve the location of the variant, which can then be represented as a VRS ``RelativeAllele``. The resulting object captures the transcript-relative mapping, the resolved genomic location, and the allele state expressed on both sequences.

.. code-block:: json

    {
      "type": "RelativeAllele",
      "relativeLocation": {
        "baseSequenceLocation": {
          "type": "SequenceLocation",
          "sequenceReference": {
            "type": "SequenceReference",
            "id": "NC_000011.10",
            "refgetAccession": "SQ.2NkFm8HK88MqeNkCgj78KidCAXgnsfV1"
          },
          "start": 119278164,
          "end": 119278165
        },
        "mappedSequenceLocation": {
          "sequenceReference": {
            "type": "SequenceReference",
            "id": "NM_005188.4",
            "refgetAccession": "SQ.sGOtbqhneKsAZHmQ47sgcLmcYPcVTRbd"
          },
          "anchor": 1174,
          "anchorOrientation": "right",
          "offsetStart": -1,
          "offsetEnd": 0
        }
      },
      "mappedState": {
        "type": "LiteralSequenceExpression",
        "sequence": "C"
      },
      "baseState": {
        "type": "LiteralSequenceExpression",
        "sequence": "C"
      }
    }
