# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://tmy.se'
RELATIVE_URLS = False

# Feed settings
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom'
FEED_RSS = 'feed'
FEED_MAX_ITEMS = 10

DELETE_OUTPUT_DIRECTORY = True
