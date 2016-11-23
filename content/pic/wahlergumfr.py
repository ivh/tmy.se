#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pylab import *

a=26.2, 7.5, 7.9, 6.6, 35.0, 5.8, 5.2
b=22.2, 6.5, 6.4, 3.7, 45.2, 5.3, 5.9
c='#00a4df','#007bb8','#cacd00','#005797','#e1001a','#ae0917','#ffd300'
e=0,0,0,0,0.05,0,0
l=u'Moderaterna',u'Folkpartiet',u'Centern',u'Kristdemokraterna',\
	u'Socialdemokraterna',u'Vänstern',u'Miljöpartiet'

subplot(121)
pie(a,colors=c,labels=l,explode=e,autopct='%1.1f%%', shadow=True)
title('Wahlergebnis 2006')

subplot(122)
pie(b,colors=c,labels=l,explode=e,autopct='%1.1f%%', shadow=True)
title('Umfrage August/September 2008')

show()
