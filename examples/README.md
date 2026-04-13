# Examples - Variant Representation Specification

This README is automatically generated from the [Makefile](./Makefile) and [an accompanying Python script](./generate_readme.py). Please edit examples in YAML. When ready to compile, run the Makefile to generate both the JSON versions and this README. From this directory:

```bash
make all
```

## Examples by Class

VRS is a collection of data models or concepts that are used together to represent molecular and systemic variation.

| Class | Representative examples |
| --- | --- |
| Adjacency | [Adjacency](json/ambiguous_linker.json), [Adjacency](json/invalid_adjacency.json), [Adjacency](json/precise_linker.json), [Adjacency](json/revcomp_breakpoint.json), [Adjacency](json/sequence_homology.json), [Adjacency](json/simple_breakpoint.json) |
| Allele | [Allele](json/SPDI_contraction.json), [Allele](json/SPDI_expansion.json) |
| CisPhasedBlock | [CisPhasedBlock](json/simple_haplotype.json) |
| DerivativeMolecule | [DerivativeMolecule](json/sv_derivative_molecule.json) |
| Terminus | [Terminus](json/terminal_breakend.json) |
