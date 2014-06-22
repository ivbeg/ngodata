#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Persimmon schemes 'NED'
http://persimmon-project.org

Persimmon schemes. Basic 'news' schemes

"""
from __future__ import generators

__author__ = "Ivan Begtin (ibegtin@gmail.com)"
__version__ = "3.0.4"
__copyright__ = "Copyright (c) 2008 Ivan Begtin"
__license__ = "BSD"
from persimmon.web.base import *

GRANTS_SCHEME = SourceScheme(attrs={
    'is_paged' : False,
    'has_unique_url' : True,
    'root_url' : u'http://www.ned.org',
    'url' : u'http://www.ned.org/where-we-work/eurasia/russia',
    'encoding' : u'utf8'
    }, 
    pagination=None,
    lister = {
    'data_area_path' : ElementPath(u"//div[@class='content']/h1/..", setKey='data_area'),
    'scheme' : MapperScheme(schemeMap={
            0 :  MapperField('text', 'text', FIELD_TYPE_STRING, unique=False, path=ElementPath('strong/..')),
            1 :  MapperField('title', 'title', FIELD_TYPE_STRING, unique=False, path=ElementPath('strong')),
            2 :  MapperField('amount', 'amount', FIELD_TYPE_STRING, unique=False, path=ElementPath('em')),
        },
        schemeType=SCHEME_LIST_OBJECTS,
        
	schemePath=ElementPath(u"p", startKey='data_area'),
        )
    },    
)    

def export_source(source_type, limit=500):
	s = source_type
	items = s.getitems(limit=limit)
#	print len(items)
	keys = ['title', 'amount', 'text']#'url', 'amount', 'status', 'activedate', 'location', 'text']
	print '\t'.join(keys)
	for item in items:	
	    values = []
	    for key in keys:
#		if key != "__raw":
#		    value = value.replace('\t', ' ').strip()
#		    if key == 'reg': value = value.replace('-', '').strip()
		    values.append(item[key].replace('\n', ' ').strip())
	    print ('\t'.join(values)).encode('utf8')
#		if key != '__raw':
#		    try:
#			print key, '-', value.encode('utf8', 'ignore')
#		    except:
#			print key, '-', value

if __name__ == '__main__':
    export_source(GRANTS_SCHEME)
