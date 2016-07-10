import requests

from anipy.exception import raise_from_respose


class User(object):
    """docstring for User"""
    def __init__(self, dic=None, **kwargs):
        if not dic is None:
            kwargs = dic

        super(User, self).__init__()
        self._id_ = kwargs.get('id', None)
        self._displayName = kwargs.get('displayName', None)
        self._animeTime = kwargs.get('animeTime', None)
        self._mangaChap = kwargs.get('mangaChap', None)
        self._about = kwargs.get('about', None)
        self._listOrder = kwargs.get('listOrder', None)
        self._adultContent = kwargs.get('adultContent', None)
        self._following = kwargs.get('following', None)
        self._imageUrlLg = kwargs.get('imageUrlLg', None)
        self._imageUrlMd = kwargs.get('imageUrlMd', None)
        self._imageUrlBanner = kwargs.get('imageUrlBanner', None)
        self._titleLanguage = kwargs.get('titleLanguage', None)
        self._scoreType = kwargs.get('scoreType', None)
        self._customListAnime = kwargs.get('customListAnime', None)
        self._customListManga = kwargs.get('customListManga', None)
        self._advancedRating = kwargs.get('advancedRating', None)
        self._advancedRatingNames = kwargs.get('advancedRatingNames', None)
        self._notifications = kwargs.get('notifications', None)

    @classmethod
    def fromResponse(cls, response):
        if isinstance(response, requests.Response):
            response = response.json()
        userDic = {}

        userDic['id'] = response.get('id', None)
        userDic['displayName'] = response.get('display_name', None)
        userDic['animeTime'] = response.get('anime_time', None)
        userDic['mangaChap'] = response.get('manga_chap', None)
        userDic['about'] = response.get('about', None)
        userDic['listOrder'] = response.get('list_order', None)
        userDic['adultContent'] = response.get('adult_content', None)
        userDic['following'] = response.get('following', None)
        userDic['imageUrlLg'] = response.get('image_url_lge', None)
        userDic['imageUrlMd'] = response.get('image_url_med', None)
        userDic['imageUrlBanner'] = response.get('image_url_banner', None)
        userDic['titleLanguage'] = response.get('title_language', None)
        userDic['scoreType'] = response.get('score_type', None)
        userDic['customListAnime'] = response.get('custom_list_anime', None)
        userDic['customListManga'] = response.get('custom_list_manga', None)
        userDic['advancedRating'] = response.get('advanced_rating', None)
        userDic['advancedRatingNames'] = response.get('advanced_rating_names', None)
        userDic['notifications'] = response.get('notifications', None)

        return cls(dic=userDic)

    @classmethod
    def resource(cls, authentication=None):
        return UserResource(authentication)

    @property
    def id(self):
        return self._id_

    @id.setter
    def id(self, id):
        self._id_ = id

    @property
    def displayName(self):
        return self._displayName

    @displayName.setter
    def displayName(self, displayName):
        self._displayName = displayName

    @property
    def animeTime(self):
        return self._animeTime

    @animeTime.setter
    def animeTime(self, animeTime):
        self._animeTime = animeTime

    @property
    def mangaChap(self):
        return self._mangaChap

    @mangaChap.setter
    def mangaChap(self, mangaChap):
        self._mangaChap = mangaChap

    @property
    def about(self):
        return self._about

    @about.setter
    def about(self, about):
        self._about = about

    @property
    def listOrder(self):
        return self._listOrder

    @listOrder.setter
    def listOrder(self, listOrder):
        self._listOrder = listOrder

    @property
    def adultContent(self):
        return self._adultContent

    @adultContent.setter
    def adultContent(self, adultContent):
        self._adultContent = adultContent

    @property
    def following(self):
        return self._following

    @following.setter
    def following(self, following):
        self._following = following

    @property
    def imageUrlLg(self):
        return self._imageUrlLg

    @imageUrlLg.setter
    def imageUrlLg(self, imageUrlLg):
        self._imageUrlLg = imageUrlLg

    @property
    def imageUrlMd(self):
        return self._imageUrlMd

    @imageUrlMd.setter
    def imageUrlMd(self, imageUrlMd):
        self._imageUrlMd = imageUrlMd

    @property
    def imageUrlBanner(self):
        return self._imageUrlBanner

    @imageUrlBanner.setter
    def imageUrlBanner(self, imageUrlBanner):
        self._imageUrlBanner = imageUrlBanner

    @property
    def titleLanguage(self):
        return self._titleLanguage

    @titleLanguage.setter
    def titleLanguage(self, titleLanguage):
        self._titleLanguage = titleLanguage

    @property
    def scoreType(self):
        return self._scoreType

    @scoreType.setter
    def scoreType(self, scoreType):
        self._scoreType = scoreType

    @property
    def customListAnime(self):
        return self._customListAnime

    @customListAnime.setter
    def customListAnime(self, customListAnime):
        self._customListAnime = customListAnime

    @property
    def customListManga(self):
        return self._customListManga

    @customListManga.setter
    def customListManga(self, customListManga):
        self._customListManga = customListManga

    @property
    def advancedRating(self):
        return self._advancedRating

    @advancedRating.setter
    def advancedRating(self, advancedRating):
        self._advancedRating = advancedRating

    @property
    def advancedRatingNames(self):
        return self._advancedRatingNames

    @advancedRatingNames.setter
    def advancedRating_names(self, advancedRatingNames):
        self._advancedRatingNames = advancedRatingNames

    @property
    def notifications(self):
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        self._notifications = notifications


class UserResource(object):
    """docstring for UserResource"""

    _URL = 'https://anilist.co/api/user'
    _auth = None

    def __init__(self, auth=None):
        super(UserResource, self).__init__()
        if  auth is None and self._auth is None:
            raise ValueError('Invalid authentication: can not be None')

        self._auth = auth

    def __new__(type, auth):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def principal(self):
        response = requests.get(self._URL, headers=self._auth.headers)
        raise_from_respose(response)

        return User.fromResponse(response)

    def byDisplayName(self, displayName):
        url = '%s/%s' % (self._URL, displayName)

        response = requests.get(url, headers=self._auth.headers)
        raise_from_respose(response)

        return User.fromResponse(response)

    def byId(self, id_):
        return self.byDisplayName(str(id_))
