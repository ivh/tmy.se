#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Marquart'
SITENAME = u'tmy.se'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Stockholm'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_RSS = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

#STATIC PATHS
STATIC_PATHS = [
    'pic',
    'static',
    'robots.txt',
    'favicon.ico',
]

RELATIVE_URLS = True
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True

DEFAULT_METADATA = {
        'status': 'draft',
        'author': AUTHOR,
        'title': ' ',
}

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}'
CATEGORY_URL = 'ctg/{slug}'
CATEGORY_SAVE_AS = 'ctg/{slug}.html'
TAG_URL = 'ctg/{slug}'
TAG_SAVE_AS = 'ctg/{slug}.html'
AUTHOR_SAVE_AS = ''
PAGE_LANG_SAVE_AS = ''
DRAFT_LANG_SAVE_AS = ''
DRAFT_SAVE_AS = ''
ARTICLE_LANG_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAGS_SAVE_AS = ''

TYPOGRIFY = True
DEFAULT_PAGINATION = 10
USE_FOLDER_AS_CATEGORY = False
SUMMARY_MAX_LENGTH = None

THEME= 'theme/chunk'
SITESUBTITLE = None
FOOTER_TEXT = 'Built with <a href="http://getpelican.com">Pelican</a>, served by <a href="https://caddyserver.com/">Caddy</a>.'
DISPLAY_CATEGORIES_ON_MENU = False
LINKS = (('email: tom@tmy.se', 'mailto:tom@tmy.se'),)
SINGLE_AUTHOR = True
MINT = False
