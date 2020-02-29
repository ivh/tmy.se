#!/usr/bin/env python3

import os, sys, glob
import datetime, time
from subprocess import call
from wand.image import Image

ROOT = '/home/tom/tmy.se'
CONT = os.path.join(ROOT,'content')
os.chdir(ROOT)

nargs = len(sys.argv)
if nargs >= 2:
    name = ' '.join(sys.argv[1:])
else:
    print('dude!')
    exit()

slug = name.replace(' ','-').replace('ä','a').replace('ö','o').replace('å','a').replace('ü','u').replace('ß','ss').lower()
title = name.title()

MDname = os.path.join(CONT,'%s.md'%slug)
suff = 0
while os.path.exists(MDname):
    suff+=1
    MDname = os.path.join(CONT,'%s%s.md'%(slug,suff))

if suff:
    slug += str(suff)

MD = """Title: {title}
Slug: {slug}
Date: {date} {t.tm_hour}:{t.tm_min}
Status: draft
Tags:

""".format(title=title,slug=slug,date=datetime.date.today(), t=time.localtime())

with open(MDname, 'w') as md:
    md.write(MD)

call(['vim',MDname])
call(['git','add',MDname])
call(['git','commit','-m "add %s"'%MDname,MDname])
