# -*- coding: utf-8  -*-

import sys

import pywikibot
from pywikibot.specialbots import UploadRobot

def complete_desc_and_upload(filename, pagetitle, desc, date, categories):
    #complete this once if applies to all files

    description = u"""{{Information
|Description    = {{en|1=""" + desc + """}}
|Source         = <!-- if applicable: {{own}} --->
|Author         = <!-- your name:  --->
|Date           = """ + date + """
|Permission     = 
|other_versions = 
}}
=={{int:license-header}}==
<!-- your license --->

""" + categories + """
[[Category:Taken with camera 123]]
"""
    url = [ filename ]
    keepFilename = False        #set to True to skip double-checking/editing destination filename
    verifyDescription = True    #set to False to skip double-checking/editing description => change to bot-mode
    targetSite = pywikibot.getSite('commons', 'commons')
    
    bot = UploadRobot(url, description=description, useFilename=pagetitle, keepFilename=keepFilename, verifyDescription=verifyDescription, targetSite=targetSite)
    bot.run()

def main(args):
    #list each file here
    
    filename    = """testimage-1.jpg"""
    pagetitle   = """testimage-1-from asdfasdfa.jpg"""
    desc        = """Mount St Helens viewed from ... in the rain"""
    date        = "2010-04-07"
    categories  = """Category:Locality
Category:Theme
Category:View type
Category:Feature1
Category:Feature2"""
    complete_desc_and_upload(filename, pagetitle, desc, date, categories)


    #sample with:  - local file name identical to file name at Commons
    #              - date as previous file
    #              - less quotes (no CR or " in fields)
    filename   = "testimage-2.jpg"
    pagetitle  = filename
    desc       = "Mount St Helens as seen from ... at sunset"
    categories = "[[Category:Locality]] [[Category:Theme]] [[Category:View type]] [[Category:Feature1]] [[Category:Feature2]]"
    complete_desc_and_upload(filename, pagetitle, desc, date, categories)
   

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    finally:
        pywikibot.stopme()