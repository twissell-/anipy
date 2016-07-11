from requests import Response

from anipy.auth import AuthenticationProvider


class Resource(object):
    """Abstract resource class. 

    Works as a base class for all other resources, keeping the generic and re-usable functionality"""
    def __init__(self):
        super(Resource, self).__init__()
        self._baseUrl = 'https://anilist.co/api/'

    @property
    def _headers(self):
        auth = AuthenticationProvider.currentAuth()

        return {'Authorization': '%s %s' % (auth.tokenType, auth.accessToken)}


def underscore_to_camelcase(value):
    first, *rest = value.split('_')
    return first + ''.join(word.capitalize() for word in rest)