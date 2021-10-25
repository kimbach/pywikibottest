# -*- coding: utf-8  -*-

import requests
import json

def recursive_iter_1(obj):
    if isinstance(obj, dict):
        for item in obj.values():
            yield from recursive_iter(item)
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for item in obj:
            yield from recursive_iter(item)
    else:
        yield obj

def recursive_iter(obj, keys=()):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from recursive_iter(v, keys + (k,))
    elif any(isinstance(obj, t) for t in (list, tuple)):
        for idx, item in enumerate(obj):
            yield from recursive_iter(item, keys + (idx,))
    else:
        yield keys, obj

data = json.loads(requests.get("https://api.smk.dk/api/v1/art/search/?keys=*&filters=%5Bpublic_domain%3Atrue%5D,%5Bhas_image%3Atrue%5D&offset=0&rows=10").text)
#items=data['items'].get()
#print(items[0].image_native)
for keys, item in recursive_iter(data['items']):
    print(keys[0])

    #if 'true' == keys[0]['has_image']:
    #    if 'image_native' == keys[0]: 
    #        print(item)
    #print(keys)

#    item[0].get()
#    print(item['image_native'])
#response = json.loads(requests.get("https://api.smk.dk/api/v1/art/search/?keys=*&filters=%5Bpublic_domain%3Atrue%5D,%5Bhas_image%3Atrue%5D&offset=0&rows=10").text)
#print(response)

#for item in recursive_iter(response):
#    print(item)
