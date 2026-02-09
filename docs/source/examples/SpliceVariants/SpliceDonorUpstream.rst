Splice donor — upstream intronic variant
========================================

This example demonstrates how a splice-adjacent intronic HGVS variant is represented using ``RelativeAllele``. The variant occurs immediately upstream of a splice donor site and is expressed using HGVS c. notation.

HGVS expression
---------------

We will use the following HGVS expression from ClinVar: `NM_001034954.3(SORBS1):c.2865+1G>T <https://www.ncbi.nlm.nih.gov/clinvar/variation/4366340/>`_.

This expression specifies a single-nucleotide variant one base upstream of the coding exon boundary, placing the variant in the intron adjacent to a splice donor site.

Transcript context
------------------

`NCBI Reference Sequence: NM_001034954.3 <https://www.ncbi.nlm.nih.gov/nuccore/NM_001385641>`_

* Minus strand
* Splice donor (exon → intron boundary)
* Upstream intronic (exon side of the exon boundary)

Transcript features at the splice junction
------------------------------------------

The exon boundaries below provide the local transcript context used to interpret the splice-adjacent HGVS position and to identify the exon boundary referenced by the HGVS expression.

.. code-block::

  CDS            184..4062
  exon 29        2854..3048
                      /gene="SORBS1"
  exon 30        3049..3822
                      /gene="SORBS1"

NCBI graphical sequence view
----------------------------

The figure below shows the same region in the `NCBI Sequence Viewer <https://www.ncbi.nlm.nih.gov/nuccore/1915575689?report=graph&tracks=[key:sequence_track,name:Sequence,display_name:Sequence,id:STD649220238,annots:Sequence,ShowLabel:false,ColorGaps:false,shown:true,order:1][key:gene_model_track,name:Genes,display_name:Genes,id:STD3194982005,annots:Unnamed,Options:ShowAll,CDSProductFeats:true,NtRuler:true,AaRuler:true,HighlightMode:2,ShowLabel:true,shown:true,order:4][key:feature_track,name:Other features---misc_feature,display_name:misc_feature Features,id:STD3760889287,subkey:misc_feature,annots:Unnamed,shown:true,order:5][key:feature_track,name:Other features---polyA_site,display_name:polyA_site Features,id:STD3911386278,subkey:polyA_site,annots:Unnamed,shown:true,order:22][key:feature_track,name:Other features---regulatory,display_name:regulatory Features,id:STD2883984253,subkey:regulatory,annots:Unnamed,shown:true,order:23][key:SNP_track,name:T2973540,display_name:Cited Variations\, dbSNP b157 v2,id:T2973540,dbname:VDB,annots:NA000146873.21\232,Layout:Adaptive,shown:true,order:24]&mk=3048|3048|blue|9&v=3025:3070&c=800080&select=null&slim=0>`_, which displays transcript structure and exon boundaries aligned to the reference sequence.

.. figure:: ../../images/splice_variants/donor_upstream/ncbi_reference_sequence.png
  :alt:  NCBI Sequence Viewer showing the splice donor region in NM_001034954.3
  :align: center
  :target: https://www.ncbi.nlm.nih.gov/nuccore/1915575689?report=graph&tracks=[key:sequence_track,name:Sequence,display_name:Sequence,id:STD649220238,annots:Sequence,ShowLabel:false,ColorGaps:false,shown:true,order:1][key:gene_model_track,name:Genes,display_name:Genes,id:STD3194982005,annots:Unnamed,Options:ShowAll,CDSProductFeats:true,NtRuler:true,AaRuler:true,HighlightMode:2,ShowLabel:true,shown:true,order:4][key:feature_track,name:Other features---misc_feature,display_name:misc_feature Features,id:STD3760889287,subkey:misc_feature,annots:Unnamed,shown:true,order:5][key:feature_track,name:Other features---polyA_site,display_name:polyA_site Features,id:STD3911386278,subkey:polyA_site,annots:Unnamed,shown:true,order:22][key:feature_track,name:Other features---regulatory,display_name:regulatory Features,id:STD2883984253,subkey:regulatory,annots:Unnamed,shown:true,order:23][key:SNP_track,name:T2973540,display_name:Cited Variations\, dbSNP b157 v2,id:T2973540,dbname:VDB,annots:NA000146873.21\232,Layout:Adaptive,shown:true,order:24]&mk=3048|3048|blue|9&v=3025:3070&c=800080&select=null&slim=0

  NCBI Sequence Viewer showing the splice donor region in NM_001034954.3

Anchor selection
----------------

To represent this variant, an anchor is chosen at the inter-residue position corresponding to the exon boundary referenced by the HGVS expression. For splice-donor variants, this anchor is placed at the end of the exon preceding the intron.

Anchor selection is determined by splice context and does not depend on transcript orientation. In this example, the exon end occurs at inter-residue position **3048**, which is used as the anchor.

The diagram below illustrates the selected anchor position relative to the exon boundary.

.. image:: ../../images/splice_variants/donor_upstream/anchor.drawio.svg
  :alt: Calculating interbase coordinates for anchor
  :align: center

Mapping relative to the anchor
------------------------------

Offsets are applied relative to the anchor to identify the transcript-relative inter-residue interval corresponding to the HGVS position.

Because the anchor represents the point at which an alignment gap occurs (e.g. an exon junction mapped to two sides of an intronic sequence), ``anchorOrientation`` is used to select which side of the anchor is used as the reference point. For this splice-donor variant, the anchor is oriented to the **left**, selecting the side of the anchor immediately preceding the exon-intron boundary.

Offsets are expressed in inter-residue coordinates. In this example, ``offsetStart = 0`` and ``offsetEnd = 1`` select the single inter-residue interval immediately upstream of the exon boundary, corresponding to the nucleotide referenced by the HGVS expression.

Transcript orientation is then used to map this inter-residue interval to the genomic reference.

In this example, the variant is described relative to the transcript reference sequence (``NM_001034954.3``), where the reference base at the variant position is ``G``.

The variant state is therefore shown on the transcript as the **mapped state** (``G → T``), and on the corresponding genomic reference (``NC_000010.11``) as the **base state** (``A → T``). Because this transcript is on the minus strand, the mapped and base states differ.

The diagram below illustrates the application of offsets relative to the anchor, the resolved inter-residue interval, and the relationship between the mapped and base states.

.. image:: ../../images/splice_variants/donor_upstream/mapping.drawio.svg
  :alt: mapping
  :align: center

The corresponding exon boundaries on the genomic reference are shown below for visual confirmation.

.. figure:: ../../images/splice_variants/donor_upstream/ucsc-exon30.png
  :alt: UCSC Exon 30
  :target: https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr10%3A95337293%2D95337297&hgsid=3617902765_kvlU8kYxpPuUSmhZphrKM32aASQP

  Exon 30 boundary in the UCSC Genome Browser.

.. figure:: ../../images/splice_variants/donor_upstream/ucsc-exon29.png
  :alt: UCSC Exon 29
  :target: https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg38&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr10%3A95339131%2D95339135&hgsid=3617902765_kvlU8kYxpPuUSmhZphrKM32aASQP

  Exon 29 boundary in the UCSC Genome Browser.

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
            "id": "NC_000010.11",
            "refgetAccession": "SQ.ss8r_wB0-b9r44TQTMmVTI92884QvBiB"
          },
          "start": 95339131,
          "end": 95339132
        },
        "mappedSequenceLocation": {
          "sequenceReference": {
            "type": "SequenceReference",
            "id": "NM_001034954.3",
            "refgetAccession": "SQ.SDt4gIJa8ChOmuI3te-3gpbJExmt1dHX"
          },
          "anchor": 3048,
          "anchorOrientation": "left",
          "offsetStart": 0,
          "offsetEnd": 1
        }
      },
      "mappedState": {
        "type": "LiteralSequenceExpression",
        "sequence": "T"
      },
      "baseState": {
        "type": "LiteralSequenceExpression",
        "sequence": "A"
      }
    }
