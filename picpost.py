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

slug = name.replace(' ','-').replace('ä','a').replace('ö','o').replace('å','a').replace('ü','u').replace('ß','ss').lower()
title = name.title()

MDname = os.path.join(CONT,'%s.md'%slug)
PICname = os.path.join(PIC,'%s.jpg'%slug)
suff = 0
while os.path.exists(MDname) or os.path.exists(PICname):
    suff+=1
    MDname = os.path.join(CONT,'%s%s.md'%(slug,suff))
    PICname = os.path.join(PIC,'%s%s.jpg'%(slug,suff))

if suff:
    slug += str(suff)

MD = """Title: {title}
Slug: {slug}
Date: {date} {t.tm_hour}:{t.tm_min}
Status: published
Tags: photo
image: {{photo}}{slug}.jpg

[![{slug}]({{photo}}{slug}.jpg "{slug}")]({{static}}/pic/{slug}.jpg)
""".format(title=title,slug=slug,date=datetime.date.today(), t=time.localtime())

with open(MDname, 'w') as md:
    md.write(MD)


RESIZE = '1400x1260>'
QUAL = 86

with Image(filename=img_f) as img:
    img.transform(resize=RESIZE)
    img.format = 'jpeg'
    img.compression_quality = QUAL
    img.save(filename=PICname)


call(['vim',MDname])
call(['git','add',MDname])
call(['git','add',PICname])
call(['git','commit','-m "auto-add %s and pic"'%MDname, PICname,MDname])
