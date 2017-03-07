from .core import Authentication
from .core import AuthenticationProvider
from .core import GrantType
from .ani.user import User
from .ani.enum_ import ListStatus
from .ani.enum_ import Smiley
from .ani.animeList import AnimeListResource

import logging
logging.basicConfig(
	format='%(levelname)s - %(name)s ln.%(lineno)d - %(message)s',
	level=logging.INFO)

logging.getLogger('anipy.ani.AnimeList').setLevel(logging.DEBUG)
logging.getLogger('anipy.core.Updatable').setLevel(logging.DEBUG)

logging.getLogger('requests').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
