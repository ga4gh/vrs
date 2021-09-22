#!/usr/bin/env python3
"""convert yaml on stdin to json on stdout"""
import copy
import json
import sys
import yaml
from collections import defaultdict

SCHEMA_DEF_KEYWORD_BY_VERSION = {
    "http://json-schema.org/draft-07/schema": "definitions",
    "http://json-schema.org/draft/2020-12/schema": "$defs"
}


def resolve_curie(curie):
    namespace, identifier = curie.split(':')
    base_url = raw_schema['namespaces'][namespace]
    return base_url + identifier


class YamlSchemaProcessor:

    def __init__(self, raw_schema):
        self.raw_schema = raw_schema
        self.processed_schema = copy.deepcopy(raw_schema)
        self.schema_def_keyword = SCHEMA_DEF_KEYWORD_BY_VERSION[self.raw_schema['$schema']]
        self.dependency_map = defaultdict(set)
        self.defs = self.processed_schema[self.schema_def_keyword]
        self.processed_classes = set()
        self.process_schema()

    def process_schema(self):
        self.processed_schema.pop('namespaces', None)
        for schema_class in self.defs:
            if 'heritable_properties' in self.defs[schema_class]:
                assert 'oneOf' in self.defs[schema_class]  # Expected schema pattern
                refs = [item['$ref'].split('/')[-1] for item in self.defs[schema_class]['oneOf'] if '$ref' in item]
                for ref in refs:
                    self.dependency_map[ref].add(schema_class)

        for schema_class in self.defs:
            self.process_schema_class(schema_class)
        for schema_class in self.defs:
            if self.class_is_abstract(schema_class):
                self.defs[schema_class].pop('heritable_properties', None)
                self.defs[schema_class].pop('heritable_required', None)
                self.defs[schema_class].pop('header_level', None)

    def class_is_abstract(self, schema_class):
        one_of_items = self.raw_schema[self.schema_def_keyword][schema_class].get('oneOf', [])
        if len(one_of_items) > 0 and '$ref' in one_of_items[0]:
            return True
        return False

    def class_is_primitive(self, schema_class):
        schema_class_type = self.raw_schema[self.schema_def_keyword][schema_class].get('type', 'abstract')
        if schema_class_type not in ['abstract', 'object']:
            return True
        return False

    def json_dump(self, stream):
        json.dump(self.processed_schema, stream, indent=3, sort_keys=False)

    def process_property_tree(self, raw_node, processed_node):
        if isinstance(raw_node, dict):
            for k, v in raw_node.items():
                if k.endswith('_curie'):
                    new_k = k[:-6]
                    processed_node[new_k] = resolve_curie(v)
                    del (processed_node[k])
                else:
                    self.process_property_tree(raw_node[k], processed_node[k])
        elif isinstance(raw_node, list):
            for raw_item, processed_item in zip(raw_node, processed_node):
                self.process_property_tree(raw_item, processed_item)
        return

    def process_schema_class(self, schema_class):
        raw_class_def = self.raw_schema[self.schema_def_keyword][schema_class]
        if schema_class in self.processed_classes:
            return
        if self.class_is_primitive(schema_class):
            self.processed_classes.add(schema_class)
            return
        processed_class_def = self.processed_schema[self.schema_def_keyword][schema_class]
        inherited_properties = dict()
        inherited_required = set()
        # The below assertion is in place to limit support to single inheritance.
        # This can be changed to multiple inheritance very readily if we add a
        # mechanism for indicating preference for overlapping attributes.
        # That functionality is not needed at this time.
        assert len(self.dependency_map[schema_class]) <= 1
        for dependency in self.dependency_map[schema_class]:
            self.process_schema_class(dependency)
            processed_dependency = self.processed_schema[self.schema_def_keyword][dependency]
            inherited_properties |= processed_dependency['heritable_properties']
            inherited_required |= set(processed_dependency['heritable_required'])
        if self.class_is_abstract(schema_class):
            prop_k = 'heritable_properties'
            req_k = 'heritable_required'
        else:
            prop_k = 'properties'
            req_k = 'required'
        raw_class_properties = raw_class_def.get(prop_k, dict())  # Nested inheritance!
        processed_class_properties = processed_class_def.get(prop_k, dict())
        processed_class_required = set(processed_class_def.get(req_k, []))
        self.process_property_tree(raw_class_properties, processed_class_properties)
        # Mix in inherited properties
        processed_class_def[prop_k] = inherited_properties | processed_class_properties
        processed_class_def[req_k] = sorted(list(inherited_required | processed_class_required))
        self.processed_classes.add(schema_class)


if __name__ == '__main__':
    raw_schema = yaml.load(sys.stdin, Loader=yaml.SafeLoader)
    p = YamlSchemaProcessor(raw_schema)
    p.json_dump(sys.stdout)