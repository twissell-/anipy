import requests

from enum import Enum

from anipy.core import Entity
from anipy.core import Updatable


class ListStatus(Enum):
    """Enumeration for entry's list status."""
    watching = 'watching'
    reading = 'watching'
    completed = 'completed'
    onHold = 'on-hold'
    dropped = 'dropped'
    planToWatch = 'plan to watch'
    planToRead = 'plan to watch'
    # none = None # uncomments if errors

    def __str__(self):
        return self.value


class ListEntry(Entity):
    """docstring for ListEntry"""
    def __init__(self, dic=None, **kwargs):
        super(ListEntry, self).__init__()
        if not dic is None:
            kwargs = dic

        listStatus = kwargs.get('listStatus', None)
        if listStatus not in list(ListStatus) and listStatus is not None:
            listStatus = ListStatus(listStatus)

        self._recordId = kwargs.get('recordId', None)
        self._listStatus = listStatus
        self._score = kwargs.get('score', 0)
        self._priorty = kwargs.get('priorty', None)
        self._notes = kwargs.get('notes', None)
        self._private = kwargs.get('private', None)
        self._updatedTime = kwargs.get('updatedTime', None)
        self._addedTime = kwargs.get('addedTime', None)
        self._scoreRaw = kwargs.get('scoreRaw', 0)
        self._advancedRatingScores = kwargs.get('advancedRatingScores', [0, 0, 0, 0, 0])
        self._hiddenDefault = kwargs.get('hiddenDefault', False)
        self._customLists = kwargs.get('customLists', [0, 0, 0, 0, 0])

    @property
    def save(self):
        self._animeListResource(self)

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
    def score(self, score):
        self._score = score

    @property
    def priorty(self):
        return self._priorty
    
    @priorty.setter
    def priorty(self, priorty):
        self._priorty = priorty

    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    @Updatable
    def notes(self, notes):
        self._notes = notes

    @property
    def private(self):
        return self._private
    
    @private.setter
    def private(self, private):
        self._private = private

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
    def hiddenDefault(self):
        return self._hiddenDefault
    
    @hiddenDefault.setter
    def hiddenDefault(self, hiddenDefault):
        self._hiddenDefault = hiddenDefault

    @property
    def customLists(self):
        return self._customLists
    
    @customLists.setter
    def customLists(self, customLists):
        self._customLists = customLists


class MangaListEntry(ListEntry):
    """docstring for MangaListEntry"""
    def __init__(self, **kwargs):
        super(MangaListEntry, self).__init__(**kwargs)
        self._manga = kwargs.get('manga', None)
        self._chaptersRead = kwargs.get('chaptersRead', None)
        self._volumesRead = kwargs.get('volumesRead', None)
        self._reread = kwargs.get('reread', None)


