#!/usr/bin/env python3
"""convert yaml on stdin to json on stdout"""
import copy
import json
import yaml
import re
from collections import defaultdict

SCHEMA_DEF_KEYWORD_BY_VERSION = {
    "http://json-schema.org/draft-07/schema": "definitions",
    "http://json-schema.org/draft/2020-12/schema": "$defs"
}


ref_re = re.compile(r':ref:`(.*?)(<.*>)?`')
link_re = re.compile(r'`(.*)\<(.*)\>`_')


class YamlSchemaProcessor:

    def __init__(self, raw_schema):
        self.raw_schema = raw_schema
        self.processed_schema = copy.deepcopy(raw_schema)
        self.schema_def_keyword = SCHEMA_DEF_KEYWORD_BY_VERSION[self.raw_schema['$schema']]
        self.dependency_map = defaultdict(set)
        self.defs = self.processed_schema[self.schema_def_keyword]
        self.processed_classes = set()
        self.process_schema()
        self.for_js = copy.deepcopy(self.processed_schema)
        self.clean_for_js()

    def _get_refs(self, schema_class):
        return [item['$ref'].split('/')[-1] for item in self.defs[schema_class]['oneOf'] if '$ref' in item]

    def _map_dependencies(self, schema_class, refs):
        for ref in refs:
            self.dependency_map[ref].add(schema_class)
            if self.class_is_abstract(ref):
                child_refs = self._get_refs(ref)
                self._map_dependencies(ref, child_refs)

    def process_schema(self):
        for schema_class in self.defs:
            if 'heritable_properties' in self.defs[schema_class]:
                assert 'oneOf' in self.defs[schema_class]  # Expected schema pattern
                refs = self._get_refs(schema_class)
                self._map_dependencies(schema_class, refs)

        for schema_class in self.defs:
            self.process_schema_class(schema_class)

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

    def js_json_dump(self, stream):
        json.dump(self.for_js, stream, indent=3, sort_keys=False)

    def js_yaml_dump(self, stream):
        yaml.dump(self.for_js, stream, sort_keys=False)

    def resolve_curie(self, curie):
        namespace, identifier = curie.split(':')
        base_url = self.processed_schema['namespaces'][namespace]
        return base_url + identifier

    def process_property_tree(self, raw_node, processed_node):
        if isinstance(raw_node, dict):
            for k, v in raw_node.items():
                if k.endswith('_curie'):
                    new_k = k[:-6]
                    processed_node[new_k] = self.resolve_curie(v)
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

    @staticmethod
    def _scrub_rst_markup(string):
        string = ref_re.sub('\g<1>', string)
        string = link_re.sub('[\g<1>](\g<2>)', string)
        string = string.replace('\n', ' ')
        return string

    def clean_for_js(self):
        self.for_js.pop('namespaces', None)
        for schema_class, schema_definition in self.for_js[self.schema_def_keyword].items():
            if self.class_is_abstract(schema_class):
                schema_definition.pop('heritable_properties', None)
                schema_definition.pop('heritable_required', None)
                schema_definition.pop('header_level', None)
            if 'description' in schema_definition:
                schema_definition['description'] = self._scrub_rst_markup(schema_definition['description'])
