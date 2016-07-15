import logging
import json
from json.decoder import JSONDecodeError

_ENCODING = 'utf-8'

logger = logging.getLogger(__name__)

def underscore_to_camelcase(value):
    first, *rest = value.split('_')
    return first + ''.join(word.capitalize() for word in rest)


def dic_to_json(dic):
#    if dic is None:
#        dic = {}
    return json.dumps(dic).encode(_ENCODING)


def response_to_dic(response):
    try:
        return json.loads(response.data.decode(_ENCODING))
    except JSONDecodeError as e:
        logger.error('There was an error decoding the response.', exc_info=True)
        return {'error': 'There was an error decoding the response.'}

