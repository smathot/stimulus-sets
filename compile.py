#!/usr/bin/env python
#-*- coding:utf-8 -*-

from academicmarkdown import build
build.HTML(u'stimulus-sets.md', u'stimulus-sets.html', standalone=False)
build.PDF(u'stimulus-sets.md', u'stimulus-sets.pdf')
