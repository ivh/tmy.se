#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.tmy.se'
RELATIVE_URLS = False
#LOAD_CONTENT_CACHE = False

FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom'
FEED_RSS = 'feed'
FEED_MAX_ITEMS = 100
