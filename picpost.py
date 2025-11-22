#!/usr/bin/env python3

import os, sys, glob
import datetime
from subprocess import call
from pathlib import Path
from wand.image import Image

ROOT = Path(__file__).parent.resolve()
CONT = ROOT / 'content'
PIC = CONT / 'pic'
os.chdir(ROOT)

nargs = len(sys.argv)
if nargs == 3:
    img_f, name = sys.argv[1:]
    name = name.lower()
elif nargs == 2:
    path = os.path.join(os.path.expanduser('~'),'Downloads','*')
    img_f = max(glob.iglob(path), key=os.path.getctime)
    name = sys.argv[1]
    name = name.lower()
else:
    print('dude!')
    exit()

if img_f.lower().endswith('png'):
    typ = 'png'
else:
    typ = 'jpg'

transl = {' ':'-',
          'ä':'a',
          'ö':'o',
          'å':'a',
          'ü':'u',
          'ß':'ss',
          '?':None,
          '.':None,
          '=':None,
          ',':None,
          "'":None,
          '!':None,
          '&':None,
        }
transl = {ord(k) : v for k,v in transl.items()}
slug = name.translate(transl).replace('--','-').lower()
title = name.title()

MDname = CONT / f'{slug}.md'
PICname = PIC / f'{slug}.{typ}'
suff = 0
while MDname.exists() or PICname.exists():
    suff+=1
    MDname = CONT / f'{slug}{suff}.md'
    PICname = PIC / f'{slug}{suff}.{typ}'

if suff:
    slug += str(suff)

date = datetime.date.today()
MD = f"""Title: {title}
Slug: {slug}
Date: {date}
Status: published
Tags: photo
image: {{photo}}{slug}.{typ}

[![{slug}]({{photo}}{slug}.{typ} "{slug}")]({{static}}/pic/{slug}.{typ})
"""

MDname.write_text(MD)

RESIZE = '1400x1260>'

with Image(filename=img_f) as img:
    img.transform(resize=RESIZE)
    img.save(filename=str(PICname))

editor = os.environ.get('EDITOR', 'vim')
call([editor, str(MDname)])
call(['git','add',str(MDname)])
call(['git','add',str(PICname)])
#call(['git','commit','-m "auto-add %s and pic"'%MDname, PICname,MDname])
