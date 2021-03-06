from ..core import (
    Resource,
    Entity
)
from .animeList import AnimeListResource


class UserResource(Resource):
    """docstring for UserResource"""

    _ENDPOINT = '/api/user/'

    def __init__(self):
        super().__init__()

    def __new__(type):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def principal(self):
        return User.fromResponse(self.get())

    def byDisplayName(self, displayName):
        return User.fromResponse(self.get(endpoint=self._ENDPOINT + displayName))

    def byId(self, id_):
        return self.byDisplayName(str(id_))


class User(Entity):
    """
    Object representation of an Anilist User response.
    """

    # TODO: remove unnecessary setters

    _userResource = UserResource()
    _animeListResource = AnimeListResource()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._id = kwargs.get('id')
        self._displayName = kwargs.get('displayName')
        self._animeTime = kwargs.get('animeTime')
        self._mangaChap = kwargs.get('mangaChap')
        self._about = kwargs.get('about')
        self._listOrder = kwargs.get('listOrder')
        self._adultContent = kwargs.get('adultContent')
        self._following = kwargs.get('following')
        self._imageUrlLge = kwargs.get('imageUrlLge')
        self._imageUrlMed = kwargs.get('imageUrlMed')
        self._imageUrlBanner = kwargs.get('imageUrlBanner')
        self._titleLanguage = kwargs.get('titleLanguage')
        self._scoreType = kwargs.get('scoreType')
        self._customListAnime = kwargs.get('customListAnime')
        self._customListManga = kwargs.get('customListManga')
        self._advancedRating = kwargs.get('advancedRating')
        self._advancedRatingNames = kwargs.get('advancedRatingNames')
        self._notifications = kwargs.get('notifications')
        self._airingNotifications = kwargs.get('airingNotifications')
        # TODO: make this an object
        self._stats = kwargs.get('stats')

    @classmethod
    def resource(cls):
        return cls._userResource

    @classmethod
    def principal(cls):
        """
        Shrotcut to UserResource's principal method.
        """
        return cls._userResource.principal()

    @classmethod
    def byDisplayName(cls, displayName):
        """
        Shrotcut to UserResource's byDisplayName method.
        """
        return cls._userResource.byDisplayName(displayName)

    @classmethod
    def byId(cls, id_):
        """
        Shrotcut to UserResource's byId method.
        """
        return cls._userResource.byId(id_)


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
    def advancedRatingNames(self, advancedRatingNames):
        self._advancedRatingNames = advancedRatingNames

    @property
    def notifications(self):
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        self._notifications = notifications

    @property
    def airingNotifications(self):
        return self._airingNotifications

    @airingNotifications.setter
    def airingNotifications(self, airingNotifications):
        self._airingNotifications = airingNotifications

    @property
    def stats(self):
        return self._stats
