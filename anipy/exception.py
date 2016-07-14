import logging

from urllib3.response import HTTPResponse
from json.decoder import JSONDecodeError

logger = logging.getLogger(__name__)

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

class InternalServerError(AniException):
    """Anilist.co return a 500 Response and a html. No extra information was given."""

def raise_from_respose(response):
    """Raise an exception acording the json data of the response"""

    if not isinstance(response, HTTPResponse):
        raise ValueError('Response must be instance of HTTPResponse intead of %s' % type(response))

    if 400 > response.status or response.status >= 600:
        return

    print(response.data)
    if response.status == 500 and 'text/html' in response.headers['content-type']:
        raise InternalServerError('Anilist.co return a 500 Response and a html. No extra information was given.')

    try:
        response = response.json()
    except JSONDecodeError as e:
        logger.error('There was an error decoding the response', exc_info=True)
        return

    if response.get('error') == 'invalid_grant':
        raise InvalidGrantException(response.get('error_description'))
    elif response.get('error') == 'invalid_request':
        raise InvalidRequestException(response.get('error_description'))
    elif response.get('error') == 'unauthorized':
        if response.get('error_description') is None:
            raise UnauthorizedException()
        raise UnauthorizedException(response.get('error_description'))
    else:
        logger.warning('Unhandled error: ' + str(response))
        raise AniException()