import requests

from enum import Enum
from datetime import datetime

from anipy.exception import raise_from_respose
from anipy.exception import NotAuthenticatedException

_URL = 'https://anilist.co/api/auth/access_token'

class GrantType(Enum):
    """Enum for Authentication grant type."""
    authorizationCode = 'authorization_code'
    authorizationPin = 'authorization_pin'
    clientCredentials = 'client_credentials'
    refreshToken = 'refresh_token'


class AuthenticationProvider(object):
    """AuthenticationProvider(GrantType) -> Authentication.

    (Singleton) Builder for the Authentication class"""

    clientId = None
    clientSecret = None
    redirectUri = None

    def __new__(type, grantType):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def __init__(self, grantType):
        super(AuthenticationProvider, self).__init__()

        self._grantType = grantType
        self._currentAuth = None
        if grantType is GrantType.authorizationCode:
            self.authenticate = self._codeRequest
        elif grantType is GrantType.authorizationPin:
            self.authenticate = self._pinRequest
        elif grantType is GrantType.clientCredentials:
            self.authenticate = self._clientCredentialsRequest
        elif grantType is GrantType.refreshToken:
            self.authenticate = self._refreshRequest
        else:
            raise ValueError('Invalid grant type.')

    @classmethod
    def config(cls, clientId, clientSecret, redirectUri):
        cls.clientId = clientId
        cls.clientSecret = clientSecret
        cls.redirectUri = redirectUri

    @classmethod
    def currentAuth(cls):
        auth = cls._instance._currentAuth
        if  auth is None:
            raise NotAuthenticatedException('Current authentication is None.')

        return auth

    @classmethod
    def refresh(cls, refreshToken, clientId=None, clientSecret=None):
        return cls._instance._refreshRequest(refreshToken, clientId, clientSecret)

    def _refreshRequest(self, refreshToken, clientId=None, clientSecret=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret

        url = _URL
        data = {
            'grant_type': GrantType.refreshToken.value,
            'client_id': clientId,
            'client_secret': clientSecret,
            'refresh_token': refreshToken}

        response = requests.post(url, data=data)
        raise_from_respose(response)

        dicResponse = response.json()
        dicResponse['refresh_token'] = refreshToken

        auth = Authentication(dic=dicResponse)
        self._currentAuth = auth

        return auth

    def _codeRequest(self, code, clientId=None, clientSecret=None, redirectUri=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret
        redirectUri = self.redirectUri if redirectUri is None else redirectUri

        url = _URL
        data = {
            'grant_type': GrantType.authorizationCode.value,
            'client_id': clientId,
            'client_secret': clientSecret,
            'redirect_uri': redirectUri,
            'code': code}

        response = requests.post(url, data=data)
        raise_from_respose(response)

        auth = Authentication(response=response)
        self._currentAuth = auth

        return auth


    def _pinRequest(self, pin, clientId=None, clientSecret=None, redirectUri=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret
        redirectUri = self.redirectUri if redirectUri is None else redirectUri

        url = _URL
        data = {
            'grant_type': GrantType.authorizationPin.value,
            'client_id': clientId,
            'client_secret': clientSecret,
            'redirect_uri': redirectUri,
            'code': pin}

        response = requests.post(url, data=data)
        raise_from_respose(response)

        auth = Authentication(response=response)
        self._currentAuth = auth

        return auth

    def _clientCredentialsRequest(self, clientId=None, clientSecret=None):
        clientId = self.clientId if clientId is None else clientId
        clientSecret = self.clientSecret if clientSecret is None else clientSecret

        url = _URL
        data = {
            'grant_type': GrantType.clientCredentials.value,
            'client_id': clientId,
            'client_secret': clientSecret}

        response = requests.post(url, data=data)
        raise_from_respose(response)

        auth = Authentication(response=response)
        self._currentAuth = auth

        return auth


class Authentication(object):
    """Represents a Anilist authentication response """

    def __init__(self, response=None, dic=None, **kwargs):
        super(Authentication, self).__init__()

        if not response is None:
            kwargs = response.json()
        elif not dic is None:
            kwargs = dic

        self._accessToken = kwargs.get('access_token', None)
        self._tokenType = kwargs.get('token_type', None)
        self._expiresIn = kwargs.get('expires_in', None)
        self._refreshToken = kwargs.get('refresh_token', None)
        exp = kwargs.get('expires', None)
        self._expires = exp if exp is None else datetime.fromtimestamp(exp)

    @classmethod
    def fromCode(cls, code, clientId=None, clientSecret=None, redirectUri=None):
        return AuthenticationProvider(
            GrantType.authorizationCode).authenticate(code, clientId, clientSecret, redirectUri)

    @classmethod
    def fromPin(cls, pin, clientId=None, clientSecret=None, redirectUri=None):
        return AuthenticationProvider(
            GrantType.authorizationPin).authenticate(pin, clientId, clientSecret)

    @classmethod
    def fromCredentials(cls, clientId=None, clientSecret=None):
        return AuthenticationProvider(
            GrantType.clientCredentials).authenticate(clientId, clientSecret)

    @classmethod
    def fromRefreshToken(cls, refreshToken, clientId=None, clientSecret=None):
        return AuthenticationProvider(GrantType.refreshToken).authenticate(refreshToken)

    def refresh(self):
        newAuth = AuthenticationProvider.refresh(self.refreshToken)
        self._accessToken = newAuth.accessToken
        self._tokenType = newAuth.tokenType
        self._expiresIn = newAuth.expiresIn
        self._expires = newAuth.expires

    @property
    def isExpired(self):
        return self.expires < datetime.now()

    @property
    def accessToken(self):
        if self.isExpired:
            self.refresh()

        return self._accessToken

    @property
    def tokenType(self):
        return self._tokenType.capitalize()

    @property
    def expires(self):
        return self._expires

    @property
    def expiresIn(self):
        return self._expiresIn

    @property
    def refreshToken(self):
        return self._refreshToken
