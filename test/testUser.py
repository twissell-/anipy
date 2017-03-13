from anipy import User
from test import assertDataType


# TODO: Imporve this tests
class TestUser(object):
    
    def testGetPrincipal(self):

        user = User.principal()

        assert user
        assert user.displayName == 'aCertainSomeone'
        assert user.id == 82369

    def testGetUserById(self):

        user = User.byId(82369)
        assert user
        assert user.id == 82369

    def testGetUserByDisplayName(self):

        user = User.byDisplayName('aCertainSomeone')
        assert user
        assert user.displayName == 'aCertainSomeone'

    def testUserProperties(self):
        user = User.principal()

        assertDataType('user.animeTime', user.animeTime, int)
        assertDataType('user.mangaChap', user.mangaChap, int)
        assertDataType('user.about', user.about, str)
        assertDataType('user.listOrder', user.listOrder, int)
        assertDataType('user.adultContent', user.adultContent, bool)
        assertDataType('user.following', user.following, bool)
        assertDataType('user.imageUrlLge', user.imageUrlLge, str)
        assertDataType('user.imageUrlMed', user.imageUrlMed, str)
        assertDataType('user.imageUrlBanner', user.imageUrlBanner, str)
        assertDataType('user.titleLanguage', user.titleLanguage, str)
        assertDataType('user.scoreType', user.scoreType, int)
        assertDataType('user.customListAnime', user.customListAnime, list)
        assertDataType('user.customListManga', user.customListManga, list)
        assertDataType('user.advancedRating', user.advancedRating, bool)
        assertDataType('user.advancedRatingNames', user.advancedRatingNames, list)
        assertDataType('user.notifications', user.notifications, int)
        assertDataType('user.airingNotifications', user.airingNotifications, int)
        assertDataType('user.stats', user.stats, dict)
