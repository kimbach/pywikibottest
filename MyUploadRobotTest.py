# -*- coding: utf-8  -*-

import sys

import pywikibot
from pywikibot.specialbots import UploadRobot

def complete_desc_and_upload(filename, pagetitle, desc, date, categories):
    #complete this once if applies to all files

    description = u"""{{Information
|Description    = {{en|1=""" + desc + """}}
|Source         = <!-- if applicable: {{own}} --->
|Author         = Kim Bach
|Date           = """ + date + """
|Permission     = 
|other_versions = 
}}
=={{int:license-header}}==
{{self|cc-by-sa-4.0}}

""" + categories + """
"""
    url = [ filename ]
    #keepFilename = False        #set to True to skip double-checking/editing destination filename
    keepFilename = True        #set to True to skip double-checking/editing destination filename
    #verifyDescription = True    #set to False to skip double-checking/editing description => change to bot-mode
    verifyDescription = False    #set to False to skip double-checking/editing description => change to bot-mode
    targetSite = pywikibot.Site('beta', 'commons')
    
    bot = UploadRobot(url, description=description, useFilename=pagetitle, keepFilename=keepFilename, verifyDescription=verifyDescription, targetSite=targetSite)
    bot.run()

#    page = pywikibot.Page(targetSite, 'File:' + filename)
#    page = pywikibot.Page(targetSite, 'File:' + filename)
#    print(page.text)
#    page.text = description
#    page.save('Replacing description')  # Saves the page

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
{{PD-old-70}}

""" + categories + """
"""
    url = [ filename ]
    #keepFilename = False        #set to True to skip double-checking/editing destination filename
    keepFilename = True        #set to True to skip double-checking/editing destination filename
    #verifyDescription = True    #set to False to skip double-checking/editing description => change to bot-mode
    verifyDescription = False    #set to False to skip double-checking/editing description => change to bot-mode
    targetSite = pywikibot.Site('beta', 'commons')
    
    bot = UploadRobot(url, description=description, useFilename=pagetitle, keepFilename=keepFilename, verifyDescription=verifyDescription, targetSite=targetSite)
    bot.run()

#    page = pywikibot.Page(targetSite, 'File:' + filename)
    page = pywikibot.Page(targetSite, 'File:' + filename)
#    print(page.text)
    page.text = description
    page.save('Replacing description')  # Saves the page

def main(args):
    #list each file here
    
    filename    = """https://iip.smk.dk/iiif/jp2/KMS1.tif.reconstructed.tif.jp2/full/full/0/native.jpg"""
    filename    = """KMS1.tif.reconstructed.tif.jpg"""
    pagetitle   = """WikiLabsKultur_001_TheHeartOfWikiLabsKultur.jpg"""
    desc        = """The Heart Of Wiki Labs Kultur - Updated Image"""
    date        = "2016-10-14 22:06"
    date        = "2019-09-10 19:00"
    categories  = """[[Category:Wiki Labs Test]]"""
    complete_artwork_desc_and_upload(filename, pagetitle, desc, date, categories)


    #sample with:  - local file name identical to file name at Commons
    #              - date as previous file
    #              - less quotes (no CR or " in fields)
    #filename   = "testimage-2.jpg"
    #pagetitle  = filename
    #desc       = "Mount St Helens as seen from ... at sunset"
    #categories = "[[Category:Locality]] [[Category:Theme]] [[Category:View type]] [[Category:Feature1]] [[Category:Feature2]]"
    #complete_desc_and_upload(filename, pagetitle, desc, date, categories)
   

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    finally:
        pywikibot.stopme()