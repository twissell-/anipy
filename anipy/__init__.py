from anipy.core import Authentication
from anipy.core import AuthenticationProvider
from anipy.core import GrantType
from anipy.ani.user import User
from anipy.ani.list import ListStatus
from anipy.ani.animeList import AnimeListResource

import logging
logging.basicConfig(
	format='%(levelname)s - %(name)s - %(message)s',
	level=logging.WARNING)

logging.getLogger('anipy.ani.animeList').setLevel(logging.DEBUG)

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
