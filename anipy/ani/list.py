from enum import Enum

from anipy import ListStatus
from anipy.core import Entity
from anipy.core import Updatable


class ListEntry(Entity):
    """docstring for ListEntry"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        listStatus = kwargs.get('listStatus')
        if listStatus not in list(ListStatus) and listStatus is not None:
            listStatus = ListStatus(listStatus)

        self._recordId = kwargs.get('recordId')
        self._listStatus = listStatus
        self._scoreRaw = kwargs.get('scoreRaw', 0)
        self._score = kwargs.get('score', 0)
        self._notes = kwargs.get('notes')
        self._updatedTime = kwargs.get('updatedTime')
        self._addedTime = kwargs.get('addedTime')
        self._advancedRatingScores = kwargs.get('advancedRatingScores', [0, 0, 0, 0, 0])
        self._customLists = kwargs.get('customLists', [0, 0, 0, 0, 0])


    @property
    def recordId(self):
        return self._recordId

    @recordId.setter
    def recordId(self, recordId):
        self._recordId = recordId

    @property
    def listStatus(self):
        return self._listStatus

    @listStatus.setter
    @Updatable
    def listStatus(self, listStatus):
        self._listStatus = listStatus

    @property
    def score(self):
        return self._score

    @score.setter
    @Updatable
    def score(self, score):
        if isinstance(score, Enum):
            self._score = score.value
        else:
            self._score = score

    @property
    def notes(self):
        return self._notes

    @notes.setter
    @Updatable
    def notes(self, notes):
        self._notes = notes

    @property
    def updatedTime(self):
        return self._updatedTime

    @updatedTime.setter
    def updatedTime(self, updatedTime):
        self._updatedTime = updatedTime

    @property
    def addedTime(self):
        return self._addedTime

    @addedTime.setter
    def addedTime(self, addedTime):
        self._addedTime = addedTime

    @property
    def scoreRaw(self):
        return self._scoreRaw

    @scoreRaw.setter
    def scoreRaw(self, scoreRaw):
        self._scoreRaw = scoreRaw

    @property
    def advancedRatingScores(self):
        return self._advancedRatingScores

    @advancedRatingScores.setter
    def advancedRatingScores(self, advancedRatingScores):
        self._advancedRatingScores = advancedRatingScores

    @property
    def customLists(self):
        return self._customLists

    @customLists.setter
    def customLists(self, customLists):
        self._customLists = customLists


class MangaListEntry(ListEntry):
    """docstring for MangaListEntry"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._manga = kwargs.get('manga')
        self._chaptersRead = kwargs.get('chaptersRead')
        self._volumesRead = kwargs.get('volumesRead')
        self._reread = kwargs.get('reread')


