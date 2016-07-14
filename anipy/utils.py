import json

_ENCODING = 'utf-8'

def underscore_to_camelcase(value):
    first, *rest = value.split('_')
    return first + ''.join(word.capitalize() for word in rest)


def dic_to_json(dic):
    return json.dumps(dic).encode(_ENCODING)


def response_to_dic(response):
    return json.loads(response.data.decode(_ENCODING))
