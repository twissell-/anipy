import requests

from anipy.core import Resource
from anipy.ani.list import AnimeListResource
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


class User(object):
    """docstring for User"""

    _animeListResource = AnimeListResource()

    def __init__(self, dic=None, **kwargs):
        if not dic is None:
            kwargs = dic

        super(User, self).__init__()
        self._id = kwargs.get('id', None)
        self._displayName = kwargs.get('displayName', None)
        self._animeTime = kwargs.get('animeTime', None)
        self._mangaChap = kwargs.get('mangaChap', None)
        self._about = kwargs.get('about', None)
        self._listOrder = kwargs.get('listOrder', None)
        self._adultContent = kwargs.get('adultContent', None)
        self._following = kwargs.get('following', None)
        self._imageUrlLge = kwargs.get('imageUrlLge', None)
        self._imageUrlMed = kwargs.get('imageUrlMed', None)
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
        userDic['imageUrlLge'] = response.get('image_url_lge', None)
        userDic['imageUrlMed'] = response.get('image_url_med', None)
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
    def resource(cls):
        return UserResource()

    @property
    def lists(self):
        return self._animeListResource.allByUserId(self.id)

    @property
    def watching(self):
        return self._animeListResource.watchingByUserId(self.id)

    @property
    def completed(self):
        return self._animeListResource.completedByUserId(self.id)

    @property
    def noHold(self):
        return self._animeListResource.onHoldByUserId(self.id)

    @property
    def dropped(self):
        return self._animeListResource.droppedgByUserId(self.id)

    @property
    def planToWatch(self):
        return self._animeListResource.planToWatchByUserId(self.id)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

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
    def imageUrlLge(self):
        return self._imageUrlLge

    @imageUrlLge.setter
    def imageUrlLge(self, imageUrlLge):
        self._imageUrlLge = imageUrlLge

    @property
    def imageUrlMed(self):
        return self._imageUrlMed

    @imageUrlMed.setter
    def imageUrlMed(self, imageUrlMed):
        self._imageUrlMed = imageUrlMed

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
