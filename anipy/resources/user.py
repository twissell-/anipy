import requests

from anipy.core import Resource
from anipy.model.user import User
from anipy.exception import raise_from_respose


class UserResource(Resource):
    """docstring for UserResource"""


    def __init__(self):
        super(UserResource, self).__init__()
        self._url = self._baseUrl + 'user/'

    def __new__(type):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def principal(self):
        response = requests.get(self._url, headers=self._headers)
        raise_from_respose(response)

        return User.fromResponse(response)

    def byDisplayName(self, displayName):
        url = self._url + displayName

        response = requests.get(url, headers=self._headers)
        raise_from_respose(response)

        return User.fromResponse(response)

    def byId(self, id_):
        return self.byDisplayName(str(id_))
