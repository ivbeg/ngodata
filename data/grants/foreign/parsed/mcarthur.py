#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Persimmon schemes 'McArthur'
http://persimmon-project.org

Persimmon schemes. Basic 'news' schemes

"""
from __future__ import generators

__author__ = "Ivan Begtin (ibegtin@gmail.com)"
__version__ = "3.0.4"
__copyright__ = "Copyright (c) 2008 Ivan Begtin"
__license__ = "BSD"
from persimmon.web.base import *
from persimmon.web.mapper import *

GRANTS_SCHEME = SourceScheme(attrs={
    'is_paged' : False,
    'has_unique_url' : True,
    'root_url' : u'http://www.macfound.org',
    'url' : u'http://www.macfound.org/grants/?location=Russia&page={{page}}',
    'encoding' : u'utf8'
    }, 
    pagination=Pagination(page_type=PAGE_TYPE_PAGED, is_counted=True, page_len=8, num_shift=1),
    lister = {
    'data_area_path' : ElementPath(u"//ul[@class='grant-list']", setKey='data_area'),
    'scheme' : MapperScheme(schemeMap={
            0 :  MapperField('url', ['title', 'url'], FIELD_TYPE_URL, unique=True, path=ElementPath('h2/a')),
            1 :  MapperField('amount', 'amount', FIELD_TYPE_STRING, path=ElementPath("div[@class='details']/div[@class='amount']")),
            2 :  MapperField('status', 'status', FIELD_TYPE_STRING, path=ElementPath("div[@class='details']/div[@class='strategy-status']")),
            3 :  MapperField('activedate', 'activedate', FIELD_TYPE_STRING, path=ElementPath("p[@class='activedate']/strong")),
            4 :  MapperField('location', 'location', FIELD_TYPE_STRING, path=ElementPath("p/span")),
            5 :  MapperField('text', 'text', FIELD_TYPE_STRING, path=ElementPath("p/span/..")),
        },
        schemeType=SCHEME_LIST_OBJECTS,
        
	schemePath=ElementPath(u"li", startKey='data_area'),
        )
    },    
)    

def export_source(source_type, limit=500):
	s = source_type
	items = s.getitems(limit=limit)
#	print len(items)
	keys = ['title','url', 'amount', 'status', 'activedate', 'location', 'text']
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
