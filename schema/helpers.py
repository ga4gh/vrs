import logging

_logger = logging.getLogger(__name__)


def pjs_filter(yaml_dict):
    for message_name, message_definition in yaml_dict['definitions'].items():
        if 'anyOf' in message_definition:
            _logger.warning(f'Removing anyOf attribute from {message_name} to avoid pjs error.')
            del message_definition['anyOf']
    return yaml_dict
