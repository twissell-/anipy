from datetime import datetime
from enum import Enum

import requests

from anipy.core import Entity
from anipy.utils import underscore_to_camelcase


class SeriesType(Enum):
    """Enumeration for entry's list status."""
    manga = 'manga'
    anime = 'anime'


class SmallSerie(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._id = kwargs.get('id')
        self._seriesType = SeriesType(kwargs.get('seriesType'))
        self._titleRomaji = kwargs.get('titleRomaji')
        self._titleEnglish = kwargs.get('titleEnglish')
        self._titleJapanese = kwargs.get('titleJapanese')
        # TODO: map type to a MediaType(Enum)
        self._type = kwargs.get('type')
        self._startDateFuzzy = datetime.strptime(str(kwargs.get('startDateFuzzy')), '%Y%m%d')
        self._endDateFuzzy = datetime.strptime(str(kwargs.get('endDateFuzzy')), '%Y%m%d')
        self._synonyms = kwargs.get('synonyms', [])
        self._genres = kwargs.get('genres', [])
        self._adult = kwargs.get('adult')
        self._averageScore = kwargs.get('averageScore')
        self._popularity = kwargs.get('popularity')
        self._imageUrlSml = kwargs.get('imageUrlSml')
        self._imageUrlLge = kwargs.get('imageUrlLge')
        self._updateAt = datetime.fromtimestamp(kwargs.get('updatedAt'))

    @property
    def id(self):
        return self._id

    @property
    def seriesType(self):
        return self._seriesType

    @property
    def titleRomaji(self):
        return self._titleRomaji

    @property
    def titleEnglish(self):
        return self._titleEnglish

    @property
    def titleJapanese(self):
        return self._titleJapanese

    @property
    def type(self):
        return self._type

    @property
    def startDateFuzzy(self):
        return self._startDateFuzzy

    @property
    def endDateFuzzy(self):
        return self._endDateFuzzy

    @property
    def synonyms(self):
        return self._synonyms

    @property
    def genres(self):
        return self._genres

    @property
    def adult(self):
        return self._adult

    @property
    def averageScore(self):
        return self._averageScore

    @property
    def popularity(self):
        return self._popularity

    @property
    def imageUrlSml(self):
        return self._imageUrlSml

    @property
    def imageUrlLge(self):
        return self._imageUrlLge

    @property
    def updateAt(self):
        return self._updateAt


# TODO: add here Serie(SmallSerie), Anime(Serie, SmallAnime) and Manga(Serie, SmallManga)

class SmallAnime(SmallSerie):
    """docstring for SmallAnime"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._totalEpisodes = kwargs.get('totalEpisodes')
        self._airingStatus = kwargs.get('airingStatus')

    def __repr__(self):
        return '<%s %s \'%s\'>' % (
            self.__class__.__name__,
            self.id,
            self.titleRomaji)

    @property
    def totalEpisodes(self):
        return self._totalEpisodes

    @property
    def airingStatus(self):
        return self._airingStatus


class SmallManga(SmallSerie):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._totalChapters = kwargs.get('totalChapters')
        self._publishingStatus = kwargs.get('publishingStatus')

    @property
    def totalChapters(self):
        return self._totalChapters

    @property
    def publishingStatus(self):
        return self._publishingStatus
