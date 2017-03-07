from datetime import datetime

from .enum_ import SeriesType
from ..core import Entity


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


class Serie(SmallSerie):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._season = kwargs.get('season')
        self._description = kwargs.get('description')
        self._favourite = kwargs.get('favourite')
        self._imageUrlBanner = kwargs.get('image_url_banner')
        self._scoreDistribution = kwargs.get('score_distribution')
        self._listStats = kwargs.get('list_stats')

    @property
    def season(self):
        return self._season

    @property
    def description(self):
        return self._description

    @property
    def favourite(self):
        return self._favourite

    @property
    def imageUrlBanner(self):
        return self._imageUrlBanner

    @property
    def scoreDistribution(self):
        return self._scoreDistribution

    @property
    def listStats(self):
        return self._listStats


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


class Anime(Serie, SmallAnime):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._duration = kwargs.get('duration')
        self._youtubeId = kwargs.get('youtube_id')
        self._hashtag = kwargs.get('hashtag')
        self._source = kwargs.get('source')
        self._airingStats = kwargs.get('airing_stats')

    @property
    def duration(self):
        return self._duration

    @property
    def youtubeId(self):
        return self._youtubeId

    @property
    def hashtag(self):
        return self._hashtag

    @property
    def source(self):
        return self._source

    @property
    def airingStats(self):
        return self._airingStats


class Manga(Serie, SmallManga):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._totalVolumes = kwargs.get('total_volumes')

    @property
    def totalVolumes(self):
        return self._totalVolumes
