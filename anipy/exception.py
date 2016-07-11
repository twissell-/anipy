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

class UnauthorizedException(AniException):
    """Wraps Anilist 'unauthorized' error."""

class NotAuthenticatedException(AniException):
    """Some operation that needs authentication was executed without it."""

def raise_from_respose(response):
    """Raise an exception acording the json data of the response"""

    if not isinstance(response, Response):
        raise ValueError('Response must be instance of requests.Response')

    if 400 > response.status_code or response.status_code >= 600:
        return

    print(response.status_code)
    response = response.json()

    if response.get('error') == 'invalid_grant':
        raise InvalidGrantException(response.get('error_description'))
    elif response.get('error') == 'invalid_request':
        raise InvalidRequestException(response.get('error_description'))
    elif response.get('error') == 'unauthorized':
        if response.get('error_description') is None:
            raise UnauthorizedException()
        raise UnauthorizedException(response.get('error_description'))
    else:
        print(response)
        raise AniException('%s %s' % (response.get('error'), response.get('error_description')))