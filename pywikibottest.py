import pywikibot
import locale

#locale.setlocale(locale.LC_ALL, '')
#site = pywikibot.Site('test', 'wikipedia')
site = pywikibot.Site('beta', 'commons')
page = site.get_parsed_page('Main_Page')
print(page)
