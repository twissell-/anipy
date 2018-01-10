from anipy import User


class TestAnimeList(object):

    def testGetLists(self):
        user = User.principal()
        assert user


