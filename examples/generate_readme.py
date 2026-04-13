"""
Auto-generate examples/README.md from compiled JSON examples.
Run via the Makefile; do not invoke directly.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path


def main():
    json_dir = Path("json")
    output_file = Path("README.md")

    if not json_dir.is_dir():
        print(f"Error: '{json_dir}' directory not found.", file=sys.stderr)
        sys.exit(1)

    # Map each classes to a sorted list of (type, filename) tuples
    class_to_examples = defaultdict(list)

    for json_file in sorted(json_dir.glob("*.json")):
        with json_file.open() as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Warning: could not parse {json_file}: {e}", file=sys.stderr)
                continue

        class_type = data.get("type")
        if not class_type:
            print(f"Warning: no 'type' field in {json_file}, skipping.", file=sys.stderr)
            continue
        
        class_to_examples[class_type].append((class_type, json_file.name))

    # Sort examples within each data_type alphabetically by name
    for class_type in class_to_examples:
        class_to_examples[class_type].sort(key=lambda x: x[0])

    # Build Markdown
    lines = [
        "# Examples - Variant Representation Specification",
        "",
        (
            "This README is automatically generated from the [Makefile](./Makefile) and [an accompanying Python script](./generate_readme.py). "
            "Please edit examples in YAML. "
            "When ready to compile, run the Makefile to generate both the JSON versions and this README. "
            "From this directory:\n"
            "\n"
            "```bash\n"
            ""
            "make all\n"
            "```"
            ""
        ),
        "",
        "## Examples by Class",
        "",
        "VRS is a collection of data models or concepts that are used together to represent molecular and systemic variation.",
        "",
        "| Class | Representative examples |",
        "| --- | --- |",
    ]

    for class_type in sorted(class_to_examples):
        examples = class_to_examples[class_type]
        links = ", ".join(
            f"[{name}](json/{filename})" for name, filename in examples
        )
        lines.append(f"| {class_type} | {links} |")

    lines.append("")  # trailing newline

    output_file.write_text("\n".join(lines))
    print(f"Generated {output_file}")


if __name__ == "__main__":
    main()
