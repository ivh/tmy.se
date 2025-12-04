#!/usr/bin/env -S uv run

import os, sys, glob
import datetime
from subprocess import call
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
CONT = ROOT / 'content'
os.chdir(ROOT)

nargs = len(sys.argv)
if nargs >= 2:
    name = ' '.join(sys.argv[1:])
else:
    print('dude!')
    exit()

transl = {' ':'-',
          'ä':'a',
          'ö':'o',
          'å':'a',
          'ü':'u',
          'ß':'ss',
          '?':None,
          '.':None,
          ',':None,
          "'":None,
          '=':None,
          '!':None,
          '&':None,
        }
transl = {ord(k) : v for k,v in transl.items()}
slug = name.translate(transl).replace('--','-').lower()
title = name.title()

MDname = CONT / f'{slug}.md'
suff = 0
while MDname.exists():
    suff+=1
    MDname = CONT / f'{slug}{suff}.md'

if suff:
    slug += str(suff)

MD = """Title: {title}
Slug: {slug}
Date: {date}
Status: draft
Tags:

""".format(title=title, slug=slug, date=datetime.date.today())

MDname.write_text(MD)

editor = os.environ.get('EDITOR', 'vim')
call([editor, str(MDname)])
call(['git','add',str(MDname)])
#call(['git','commit','-m "add %s"'%MDname,MDname])
