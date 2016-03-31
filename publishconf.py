#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://p.tmy.se'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_RSS = 'feed'

DELETE_OUTPUT_DIRECTORY = True

