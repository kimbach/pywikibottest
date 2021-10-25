# -*- coding: utf-8  -*-

import pywikibot
from pywikibot import pagegenerators as pg

def recursive_iter(obj, keys=()):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from recursive_iter(v, keys + (k,))
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for idx, item in enumerate(obj):
            yield from recursive_iter(item, keys + (idx,))
    else:
        yield keys, obj


#with open('my_query.rq', 'r') as query_file:
query = u"""SELECT ?item ?itemLabel ?skaberLabel ?inventarnummer ?billeder ?commonscat WHERE {
?item wdt:P195 wd:Q671384 .
OPTIONAL { ?item wdt:P217 ?inventarnummer }
OPTIONAL { ?item wdt:P170 ?skaber }
OPTIONAL { ?item wdt:P18 ?billeder }
OPTIONAL { ?item wdt:P373 ?billeder }
SERVICE wikibase:label { bd:serviceParam wikibase:language "da,en" } .}"""

#query_file.read()

wikidata_site = pywikibot.Site("wikidata", "wikidata")

#repo = wikidata_site.data_repository()

#wdquery = pywikibot.WikidataQuery wikidataquery()
#wd_queryset = wdquery.QuerySet(query)

#wd_query = wdquery.WikidataQuery(cacheMaxAge=0)
#data = wd_query.query(wd_queryset)

#for keys, item in recursive_iter(data['claims']):
#    print(keys, item)
#    print(item)

generator = pg.WikidataSPARQLPageGenerator(query, site=wikidata_site)
#pywikibot.output(u'retrieved %d items' % generator. [u'status'][u'items'])
for item in generator:
    data = item.get()
    claims = data.get('claims')
    print(claims.get(u'P217')[0].target)
    #for keys, claim in recursive_iter(claims.get(u'P217')[0]):
    #    print(keys, claim)
        #print(clai)

    #print(claims.get(u'P217')[0].mainsnak)
    #smkid = claims.get(u'P217')[0]['mainsnak']
    #print(smkid[''])