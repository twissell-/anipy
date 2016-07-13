from anipy.core import Authentication
from anipy.core import AuthenticationProvider
from anipy.ani.user import User
from anipy.ani.list import ListStatus

import logging
logging.basicConfig(
	format='%(levelname)s - %(name)s - %(message)s',
	level=logging.DEBUG)

logging.getLogger('requests').setLevel(logging.WARNING)
