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
import SMKItem
import Artwork

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


        #complete_artwork_desc_and_upload(filename, pagetitle, desc, production_date, categories)

        artwork = Artwork(filename, 
            pagetitle, 
            artist,
            author,
            title,
            desc,
            depicted_people,
            production_date,
            medium,
            dimensions,
            institution,
            department,
            place_of_discovery,
            object_history, 
            exhibition_history,
            credit_line,
            inscriptions,
            notes,
            accession_number,
            place_of_creation,
            source,
            permission,
            other_versions,
            references,
            depicted_place,
            wikidata,
            categories)


        print ('id           =' + item.id)
        print ('object_number=' + item.object_number)
        print ('image_native =' + item.image_native)


