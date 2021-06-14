#!/usr/bin/env python3

import os, sys, glob
import datetime, time
from subprocess import call
from wand.image import Image

ROOT = '/home/tom/tmy.se'
CONT = os.path.join(ROOT,'content')
PIC = os.path.join(CONT,'pic')
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
          ',':None,
          '!':None,
          '&':None,
        }
transl = {ord(k) : v for k,v in transl.items()}
slug = name.translate(transl).replace('--','-').lower()
title = name.title()

MDname = os.path.join(CONT,'%s.md'%slug)
PICname = os.path.join(PIC,'%s.%s'%(slug,typ))
suff = 0
while os.path.exists(MDname) or os.path.exists(PICname):
    suff+=1
    MDname = os.path.join(CONT,'%s%s.md'%(slug,suff))
    PICname = os.path.join(PIC,'%s%s.typ'%(slug,suff,typ))

if suff:
    slug += str(suff)

date=datetime.date.today()
t=time.localtime()
MD = f"""Title: {title}
Slug: {slug}
Date: {date} {t.tm_hour:02d}:{t.tm_min:02d}
Status: published
Tags: photo
image: {{photo}}{slug}.{typ}

[![{slug}]({{photo}}{slug}.{typ} "{slug}")]({{static}}/pic/{slug}.{typ})
"""

with open(MDname, 'w') as md:
    md.write(MD)


RESIZE = '1400x1260>'

with Image(filename=img_f) as img:
    img.transform(resize=RESIZE)
    img.save(filename=PICname)


call(['vim',MDname])
call(['git','add',MDname])
call(['git','add',PICname])
#call(['git','commit','-m "auto-add %s and pic"'%MDname, PICname,MDname])
