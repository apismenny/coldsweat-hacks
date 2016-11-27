# -*- coding: utf-8 -*-

import urllib2
import re
from coldsweat import *
from coldsweat.plugins import *


@event('entry_parsed')
def entry_parsed(entry, parsed_entry):
    if entry.feed.title == 'Cyanide & Happiness':
        request = urllib2.Request(entry.link)
        page = urllib2.urlopen(request).read()

        m = re.search(r'<img id="main-comic" src="//(.+)\?', page)

        if m is not None:
            entry.content = '<img src="' + m.group(1) + '">'
