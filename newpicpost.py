#!/usr/bin/env python3

import os, sys, glob
import datetime, time
from subprocess import call
from wand.image import Image

nargs = len(sys.argv)
if nargs == 3:
    img_f, name = sys.argv[1:]
elif nargs == 2:
    path = os.path.join(os.path.expanduser('~'),'Downloads','*')
    img_f = max(glob.iglob(path), key=os.path.getctime)
    name = sys.argv[1]
else:
    print('dude!')
    exit()


ROOT = '/home/tom/tmy.se'
CONT = os.path.join(ROOT,'content')
PIC = os.path.join(CONT,'pic')
os.chdir(ROOT)

MDname = os.path.join(CONT,'%s.md'%name)
if os.path.exists(MDname):
    YN = input('delete existing file %s? [y/N]'%MDname)
    if YN.upper() != 'Y':
        exit()


MD = """Title: {name}
Slug: {name}
Date: {date} {t.tm_hour}:{t.tm_min}
Status: published
Tags: foto
image: {{photo}}{name}.jpg

![{name}]({{photo}}{name}.jpg "{name}")
""".format(name=name,date=datetime.date.today(), t=time.localtime())

with open(MDname, 'w') as md:
    md.write(MD)


RESIZE = '1024x896>'
QUAL = 82

with Image(filename=img_f) as img:
    img.transform(resize=RESIZE)
    img.format = 'jpeg'
    img.compression_quality = QUAL
    img.save(filename=os.path.join(PIC,'%s.jpg'%name))
    

call(['vim',MDname])
