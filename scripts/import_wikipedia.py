#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Script para importar o JSON das siglas da Wikipedia para a Siglapédia
Copyright 2013 Ricardo Lafuente <r@sollec.org>

Licenciado segundo a GPL v3
http://www.gnu.org/licenses/gpl.html

Conteúdo das siglas recolhido pelo Pedro Rodrigues <medecau@gmail.com>
'''


### Set up Django path
import sys, os
projectpath = os.path.abspath('../../')
if projectpath not in sys.path:
    sys.path.append(projectpath)
    sys.path.append(os.path.join(projectpath, 'siglapedia/'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'siglapedia.settings'

import json
from siglapedia import settings
from acronyms.models import Acronym

data = open('siglas-wikipedia.json', 'r').read()
acros = json.loads(data)

print settings.DATABASES

for a in acros:
    print a
    link = a['url']
    name = a['sigla']
    definition = a['significado']
    if not Acronym.objects.filter(name=name, definition=definition, link=link):
        a = Acronym.objects.create(name=name, definition=definition, link=link)
