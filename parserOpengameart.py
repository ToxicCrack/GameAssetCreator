#encoding: UTF-8

#The MIT License
#Copyright 2018 Daniel Lichtblau
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from parserBase import *
import pprint
import re

class parserOpengameart(parserBase):
    def parse(self, url):
        tags = []
        #field-name-field-art-tags
        html = self.getHtml(url)
        matches = re.findall('field_art_tags_tid=([a-zA-Z0-9\-\./_\)\(]*)"', html, flags=re.IGNORECASE)
        if(matches is not None):
            tags = matches

        matches = re.search('<div class=\'license\-name\'>([a-zA-Z0-9\-\./_\)\(]*)</div>', html, flags=re.IGNORECASE)
        if(matches is not None):
            tags.append(matches.group(1))
            
        return {"tags": tags}