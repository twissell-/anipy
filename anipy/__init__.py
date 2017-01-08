from anipy.core import Authentication
from anipy.core import AuthenticationProvider
from anipy.core import GrantType
from anipy.ani.user import User
from anipy.ani.list import ListStatus
from anipy.ani.list import Smiley
from anipy.ani.animeList import AnimeListResource

import logging
logging.basicConfig(
	format='%(levelname)s - %(name)s ln.%(lineno)d - %(message)s',
	level=logging.INFO)

logging.getLogger('anipy.ani.AnimeList').setLevel(logging.DEBUG)
logging.getLogger('anipy.core.Updatable').setLevel(logging.DEBUG)

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
