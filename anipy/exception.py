import logging
from urllib3.response import HTTPResponse

from anipy.utils import response_to_dic

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

    logger.debug('Response status: ' + str(response.status))
    logger.debug('Response content-type: ' + response.headers['content-type'])

    if response.status == 405:
        logger.error('HTTP 405 Method not allowed.')
        raise AniException('HTTP 405 Method not allowed.')
    if response.status == 500 and 'text/html' in response.headers['content-type']:
        raise InternalServerError('Anilist.co return a 500 Response and a html. No extra information was given.')

    response = response_to_dic(response)

    if response.get('error') == 'invalid_grant':
        raise InvalidGrantException(response.get('error_description'))
    elif response.get('error') == 'invalid_request':
        raise InvalidRequestException(response.get('error_description'))
    elif response.get('error') == 'unauthorized':
        if response.get('error_description') is None:
            raise UnauthorizedException()
        raise UnauthorizedException(response.get('error_description'))
    else:
        logger.error('Unhandled error: ' + str(response))
