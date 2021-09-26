.. _relationships:

Relationship of VRS to existing standards
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Because a primary objective of the GA4GH Variation Representation
Specification (VRS) effort is to unify disparate efforts to represent
biological sequence variation, it is important to describe how this
document relates to previous work in order to avoid “reinventing the
wheel”.

The Variant Call Format (VCF) is the de facto standard for
representing alleles, particularly for use during primary analysis in
high-throughput sequencing pipelines. VCF permits a wide range of
annotations on alleles, such as quality and likelihood scores. VCF is
a file-based format and is exclusively for genomic alleles. In
contrast, the VRS data model abstractly represents Alleles,
Haplotypes, and Genotypes on all sequence types, is independent of
medium, and is well-suited to secondary analyses, allele
interpretation, aggregation, and system-level interoperability.

The HGVS nomenclature recommendations describe how sequence variation
should be presented to human beings. In addition to representing a
wide variety of sequence changes from single residue variation through
large cytogenetic events, HGVS attempts to also encode in strings
notions of biological mechanism (e.g., inversion as a kind of
deletion-insertion event), predicted events (e.g., parentheses for
computing protein sequence), and complex states (e.g., mosaicism). In
practice, HGVS recommendations are difficult to implement fully and
consistently, leading to ambiguity in presentation. In contrast, the
VRS is a formal specification that improves consistency of
representation among computer systems. VRS is currently less
expressive than HGVS for rarer cases of variation, such as cytogenetic
variation or context-based allele representations (e.g., insT written
as dupT when the insertion follows a T). Future versions of the
specification will seek to address limitations while preserving
principles of conceptual clarity and precision.

The Sequence Ontology (SO) is a set of terms and relationships used to
describe the features and attributes of biological sequence. The focus
of the SO has been the annotation of, or placement of ‘meaning’, onto
genomic sequence regions. The VRS effort seeks to use the same
descriptive definitions where possible, and to inform the refinement
of SO.

The Genotype Ontology (GENO) builds on the SO to include richer
modeling of genetic variation at different levels of granularity that
are captured in genotype representations. Unlike the SO which is used
primarily for annotation of genomic features, GENO was developed by
the Monarch Initiative to support semantic data models for integrated
representation of genotypes and genetic variants described in human
and model organism databases. The core of the GENO model decomposes a
genotype specifying sequence variation across an entire genome into
smaller components of variation (e.g. allelic composition at a
particular locus, haplotypes, gene alleles, and specific sequence
alterations). GENO also enables description of biological attributes
of these genetic entities (e.g. zygosity, phase, copy number, parental
origin, genomic position), and their causal relationships with
phenotypes and diseases.

ClinVar is an archive of clinically reported relationships between
variation and phenotypes along with interpretations and supporting
evidence. Data in ClinVar are submitted primarily by diagnostic
labs. ClinVar includes expert reviews and data links to other
clinically-relevant resources at NCBI. VRS is expected to facilitate
data submissions by providing unified guidelines for data structure
and allele normalization.

ClinGen provides a centralized database of genomic and phenotypic data
provided by clinicians, researchers, and patients. It standardizes
clinical annotation and interpretation of genomic variants and
provides evidence-based expert consensus for curated genes and
variants. ClinGen has informed the VRS effort and is committed to
harmonizing and collaborating on the evolution of the VRS
specification to achieve improved data sharing.

HL7 FHIR Genomics, Version 2 Clinical Genomics Implementation Guide,
CDA Genetic Test Report: There are several standards developed under
the HL7 umbrella that include a genomics component. The FHIR Genomics
component was released as part of the overall FHIR specification
(latest is Release 3) based on standardized use cases.  The HL7
Clinical Genomics (CG) Work Group focuses on developing standards for
clinical genomic data and related relevant information within
EHRs. The specifications developed by the CG work group primarily
utilize the HL7 v2 messaging standard and the newer HL7 FHIR (Fast
Healthcare Interoperability Resources) framework.

The SPDI format created to represent alleles in NCBI’s Variation
Services has four components: the sequence identifier, which is
specified with a sequence accession and version; the 0-based
inter-residue coordinate where the deletion starts; the deleted
sequence (or its length) and the inserted sequence. The Variation
Services return the minimum deleted sequence required to avoid over
precision. For example, a deletion of one G in a run of 4 is specified
with deleted and inserted sequences of GGGG and GGG respectively,
avoiding the need to left or right shift the minimal
representation. This reduces ambiguity, but can lead to long allele
descriptions.


From https://github.com/ga4gh/vrs/issues/305:

VRS is being designed as an informational model that is designed as atomic building blocks that can be composed into higher order variant representations. It is designed for the primary function of precise computational data exchange.

VRS is also extensible. It is not limited to simple SNVs, DelIns and any subset of variation and such can be used as a standard that will grow with the types of variation that are often limited by other methods, nomenclatures and authorizing registries (SPDI, VCF and HGVS)

VRS is not limited to genomic sequence, but any type of sequence (genomic, transcript, protein).

VRS is not limited to sequence based variation (cytobands, systemic expression, genetic features)

SPDI is only about alleles and precise genomic variation, SPDI's nomenclature is built on VOCA (variant overprecision correction algorithm) as specified by NCBI. VRS is built on VOCA as well for the types of variation that fall within its domain.

VCF is genomic only. VCF is a file format. VCF is primarily designed for high-volume, compact variant calls. VCF is not designed to be extensible in the same way as VRS to support much broader representations of variation independent of samples or cohorts. VCF does not normalize the small precise SNVs and DelInss using the same VOCA based normalization.

HGVS is a nomenclature. HGVS is designed primarily for human-readability not computational identification. HGVS is not applied consistently in reporting, literature, and databases even though there has been great strides to provide tooling to validate HGVS syntax. HGVS does not normalize variation using VOCA. Several HGVS expressions can represent the same variant. VRS is not designed to be human-readable (we have started designing implementation guidance for wrapping VRS representations in Value Object Descriptors to allow exchange systems to add human-readable and useful attributes that improve the productivity of data exchange contracts involving variation - see VRSATILE).
