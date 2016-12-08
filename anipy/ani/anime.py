import requests

from anipy.core import Entity
from anipy.utils import underscore_to_camelcase


class SmallAnime(Entity):
    """docstring for SmallAnime"""
    def __init__(self, dic=None, **kwargs):
        super().__init__()
        if not dic is None:
            kwargs = dic

        self._id = kwargs.get('id')
        self._titleRomaji = kwargs.get('titleRomaji')
        self._type = kwargs.get('type')
        self._imageUrlMed = kwargs.get('imageUrlMed')
        self._imageUrlSml = kwargs.get('imageUrlSml')
        self._adult = kwargs.get('adult')
        self._popularity = kwargs.get('popularity')
        self._titleJapanese = kwargs.get('titleJapanese')
        self._titleEnglish = kwargs.get('titleEnglish')
        self._synonyms = kwargs.get('synonyms')
        self._imageUrlLge = kwargs.get('imageUrlLge')
        self._airingStatus = kwargs.get('airingStatus')
        self._averageScore = kwargs.get('averageScore')
        self._totalEpisodes = kwargs.get('totalEpisodes')
        self._relationType = kwargs.get('relationType')
        self._role = kwargs.get('role')

    def __repr__(self):
        return '<%s %s \'%s\'>' % (
            self.__class__.__name__, 
            self.id,
            self.titleRomaji)


    @classmethod
    def fromResponse(cls, response):
        if isinstance(response, requests.Response):
            response = response.json()
        dic = {}

        for k in response:
            dic[underscore_to_camelcase(k)] = response.get(k)

        return cls(dic=dic)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def titleRomaji(self):
        return self._titleRomaji
    
    @titleRomaji.setter
    def titleRomaji(self, titleRomaji):
        self._titleRomaji = titleRomaji

    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        self._type = type

    @property
    def imageUrlMed(self):
        return self._imageUrlMed
    
    @imageUrlMed.setter
    def imageUrlMed(self, imageUrlMed):
        self._imageUrlMed = imageUrlMed

    @property
    def imageUrlSml(self):
        return self._imageUrlSml
    
    @imageUrlSml.setter
    def imageUrlSml(self, imageUrlSml):
        self._imageUrlSml = imageUrlSml

    @property
    def adult(self):
        return self._adult
    
    @adult.setter
    def adult(self, adult):
        self._adult = adult

    @property
    def popularity(self):
        return self._popularity
    
    @popularity.setter
    def popularity(self, popularity):
        self._popularity = popularity

    @property
    def titleJapanese(self):
        return self._titleJapanese
    
    @titleJapanese.setter
    def titleJapanese(self, titleJapanese):
        self._titleJapanese = titleJapanese

    @property
    def titleEnglish(self):
        return self._titleEnglish
    
    @titleEnglish.setter
    def titleEnglish(self, titleEnglish):
        self._titleEnglish = titleEnglish

    @property
    def synonyms(self):
        return self._synonyms
    
    @synonyms.setter
    def synonyms(self, synonyms):
        self._synonyms = synonyms

    @property
    def imageUrlLge(self):
        return self._imageUrlLge
    
    @imageUrlLge.setter
    def imageUrlLge(self, imageUrlLge):
        self._imageUrlLge = imageUrlLge

    @property
    def airingStatus(self):
        return self._airingStatus
    
    @airingStatus.setter
    def airingStatus(self, airingStatus):
        self._airingStatus = airingStatus

    @property
    def averageScore(self):
        return self._averageScore
    
    @averageScore.setter
    def averageScore(self, averageScore):
        self._averageScore = averageScore

    @property
    def totalEpisodes(self):
        return self._totalEpisodes
    
    @totalEpisodes.setter
    def totalEpisodes(self, totalEpisodes):
        self._totalEpisodes = totalEpisodes

    @property
    def relationType(self):
        return self._relationType
    
    @relationType.setter
    def relationType(self, relationType):
        self._relationType = relationType

    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, role):
        self._role = role
