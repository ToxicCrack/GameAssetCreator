#encoding: UTF-8

#The MIT License
#Copyright 2018 Daniel Lichtblau
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from parserBase import *
import pprint
import re

class parserUnity(parserBase):
    def parse(self, url, asset):
        tags = []
        description = ""
        name = ""
        #field-name-field-art-tags
        html = self.getHtml(url)
        matches = re.findall('<div class="Eh1GG _15pcy".*?>(.*?)</div>', html, flags=re.IGNORECASE)
        if(matches is not None):
            tags = matches

        matches = re.search('<meta name="twitter:description" content="(.*?)"', html, flags=re.I | re.DOTALL)
        if(matches is not None):
            description = matches.group(1).replace("</p>", "\n")
            description = description.replace("</li>", "\n")
            description = description.replace("<br>", "\n")
            description = description.replace("<br />", "\n")
            description = self.cleanhtml(description)
        
        matches = re.search('<meta name="twitter:title" content="(.*?)"', html, flags=re.IGNORECASE)
        if(matches is not None):
          name = matches.group(1).replace(" - Asset Store", "")
          
        matches = re.search('<meta name="twitter:image" content="(.*?)"', html, flags=re.IGNORECASE)
        if(matches is not None):
          preview = matches.group(1)
          self.saveURL(preview, asset['path'])
            
        return {"tags": tags, "description": description, "name": name}