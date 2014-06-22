#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Persimmon schemes 'USRF'
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
    'root_url' : u'http://www.usrf.ru',
    'url' : u'http://www.usrf.ru/grants/under100k/supported_projects.html',
    'encoding' : u'utf8'
    }, 
    pagination=None,
    lister = {
    'data_area_path' : ElementPath(u"//div[@id='right_column_content']", setKey='data_area'),
    'scheme' : MapperScheme(schemeMap={
            0 :  MapperField('title', 'title', FIELD_TYPE_STRING, unique=False, path=ElementPath('following-sibling::p[1]/preceding-sibling::h3')),
            1 :  MapperField('grantee', 'grantee', FIELD_TYPE_STRING, unique=False, path=ElementPath('following-sibling::p[1]')),
            2 :  MapperField('stratarea', 'stratarea', FIELD_TYPE_STRING, unique=False, path=ElementPath('following-sibling::p[2]')),
            3 :  MapperField('grant', 'grant', FIELD_TYPE_STRING, unique=False, path=ElementPath('following-sibling::p[3]')),
            4 :  MapperField('cofunding', 'cofunding', FIELD_TYPE_STRING, unique=False, path=ElementPath('following-sibling::p[4]')),
            5 :  MapperField('duration', 'duration', FIELD_TYPE_STRING, unique=False, path=ElementPath('following-sibling::p[5]')),
            6 :  MapperField('text', 'text', FIELD_TYPE_STRING, unique=False, path=ElementPath('following-sibling::p[6]')),
        },
        schemeType=SCHEME_LIST_OBJECTS,
        
	schemePath=ElementPath(u"h3", startKey='data_area'),
        )
    },    
)    

def export_source(source_type, limit=500):
	s = source_type
	items = s.getitems(limit=limit)
#	print len(items)
	keys = ['title', 'grantee', 'stratarea', 'grant', 'cofunding', 'duration', 'text']#'url', 'amount', 'status', 'activedate', 'location', 'text']
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
