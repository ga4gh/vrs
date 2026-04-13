# Examples - Variant Representation Specification

This README is automatically generated from the [Makefile](./Makefile) and [an accompanying Python script](./generate_readme.py). Please edit examples in YAML. When ready to compile, run the Makefile to generate both the JSON versions and this README. From this directory:

```bash
make all
```

## Examples by Class

VRS is a collection of data models or concepts that are used together to represent molecular and systemic variation.

| Class | Representative examples |
| --- | --- |
| Adjacency | [ambiguous_linker](json/ambiguous_linker.json), [invalid_adjacency](json/invalid_adjacency.json), [precise_linker](json/precise_linker.json), [revcomp_breakpoint](json/revcomp_breakpoint.json), [sequence_homology](json/sequence_homology.json), [simple_breakpoint](json/simple_breakpoint.json) |
| Allele | [SPDI_contraction](json/SPDI_contraction.json), [SPDI_expansion](json/SPDI_expansion.json) |
| CisPhasedBlock | [simple_haplotype](json/simple_haplotype.json) |
| DerivativeMolecule | [sv_derivative_molecule](json/sv_derivative_molecule.json) |
| Terminus | [terminal_breakend](json/terminal_breakend.json) |
