import requests

from anipy.core import Resource
from anipy.model.list import ListEntry
from anipy.exception import raise_from_respose


class AnimeListResource(Resource):
    """docstring for AnimeListResource"""

    def __init__(self):
        super(AnimeListResource, self).__init__()
        self._url = self._baseUrl + 'user/%s/animelist/'

    def __new__(type):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def byUserDisplayName(self, displayName, raw=False):
        return self._byUserIdOrDisplayName(displayName, raw).json()

    def byUserId(self, id_, raw=False):
        return self._byUserIdOrDisplayName(id_, raw).json()

    def watchingByUserId(self, id_):
        return list(ListEntry.fromResponse(item) for item in self._byUserIdOrDisplayName(id_).json()['lists']['watching'])

    def _byUserIdOrDisplayName(self, displayName, raw=False):
        url = self._url % str(displayName)
        if raw:
            url += 'raw'

        response = requests.get(self._url % displayName, headers=self._headers)
        raise_from_respose(response)

        return response
