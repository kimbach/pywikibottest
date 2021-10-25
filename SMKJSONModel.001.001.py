# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = empty_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Type, Callable, cast
from enum import Enum
from datetime import datetime
import dateutil.parser
import json
import requests
import SMKJSONModel

def complete_artwork_desc_and_upload(filename, pagetitle, desc, date, categories):
    #complete this once if applies to all files

    description = u"""{{Artwork
|Description    = {{en|1=""" + desc + """}}
|Source         = [[Statens Museeum for Kunst]]
|Author         = 
|Date           = """ + date + """
|Permission     = 
|other_versions = 
}}
=={{int:license-header}}==
<!-- your license --->

""" + categories + """
"""
    url = [ filename ]
    #keepFilename = False        #set to True to skip double-checking/editing destination filename
    keepFilename = True        #set to True to skip double-checking/editing destination filename
    #verifyDescription = True    #set to False to skip double-checking/editing description => change to bot-mode
    verifyDescription = False    #set to False to skip double-checking/editing description => change to bot-mode
    #targetSite = pywikibot.Site('beta', 'commons')
    
    #bot = UploadRobot(url, description=description, useFilename=pagetitle, keepFilename=keepFilename, verifyDescription=verifyDescription, targetSite=targetSite)
    #bot.run()

json_string = json.loads(requests.get("https://api.smk.dk/api/v1/art/search/?keys=*&filters=%5Bpublic_domain%3Atrue%5D,%5Bhas_image%3Atrue%5D&offset=0&rows=10").text)
result = SMKJSONModel.empty_from_dict(json_string)
categories  = """[[Category:Wiki Labs Kultur]]
[[Category:Paintings in Statens Museum for Kunst]]"""

for item in result.items:
    if item.has_image: 
        filename = item.image_native
        pagetitle = 'SMK-' + item.id + '-' + item.object_number + ':' + item.titles[0].title
        desc = ''
        for line in item.content_description:
            desc = desc + line
        
        production_date = ''
        for date in item.production_date:
            production_date = production_date + date.start.strftime("%Y-%m-%d") + ' - ' + date.end.strftime("%Y-%m-%d") + '\n'  


        complete_artwork_desc_and_upload(filename, pagetitle, desc, production_date, categories)

        print ('id           =' + item.id)
        print ('object_number=' + item.object_number)
        print ('image_native =' + item.image_native)

