import json
from requests import Response

class AniException(Exception):
    """There was an ambiguous exception that occurred.

    Also, works as a root exception that all Anipy exceptions must extends
    """

class InvalidGrantException(AniException):
    """Wraps Anilist 'invalid_grant' error."""

class InvalidRequestException(AniException):
    """Wraps Anilist 'invalid_grant' error."""

def raise_from_respose(response):
    """Raise an exception acording the json data of the response"""

    if isinstance(response, Response):
        response = response.json()
    elif isinstance(response, str):
        response = json.loads(response)
    elif isinstance(response, dict):
        pass
    else:
        raise ValueError('Response must be requests.Response, str or dict.')

    if response.get('error') == 'invalid_grant':
        raise InvalidGrantException(response.get('error_description'))
    elif response.get('error') == 'invalid_request':
        raise InvalidRequestException(response.get('error_description'))
    else:
        raise AniException('%s %s' % (response.get('error'), response.get('error_description')))