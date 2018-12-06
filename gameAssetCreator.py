# -*- coding: utf-8 -*-

#The MIT License
#Copyright 2018 Daniel Lichtblau
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from threading import *
import wx
import mainDialog
import pprint
from config import Config
import os
import re
import shutil
import json
#from wx.lib.pubsub import setupkwargs
from wx.lib.pubsub import pub
import wx.stc
from parserOpengameart import *
from parserGamedevmarket import *
from parserTokegameart import *

# Define notification event for thread completion
EVT_RESULT_ID = wx.Window.NewControlId()

def EVT_RESULT(win, func):
    """Define Result Event."""
    win.Connect(-1, -1, EVT_RESULT_ID, func)
    
class ResultEvent(wx.PyEvent):
    """Simple event to carry arbitrary result data."""
    def __init__(self, data):
        """Init Result Event."""
        wx.PyEvent.__init__(self)
        self.SetEventType(EVT_RESULT_ID)
        self.data = data

class gacDialog(mainDialog.mainDialog):
  config = Config()
  worker = None
  errorStr = ""
  
  def __init__(self,parent):
    #initialize parent class
    mainDialog.mainDialog.__init__(self,parent)
    self.Bind(wx.EVT_CLOSE, self.closeWindow)
    
    self.m_rootDirPicker.SetPath(self.config.getValue("rootDir"))
    self.m_outputDirPicker.SetPath(self.config.getValue("outputDir"))
    
    # Set up event handler for any worker thread results
    EVT_RESULT(self,self.onWorkerResult)
    pub.subscribe(self.onStatusUpdate, 'update')
    pub.subscribe(self.onProgressUpdate, 'progress')
    self.m_btnCancel.Enable(False)
    
    #Tags Page
    #sizer = self.TagsTab.GetSizer()
    #self.m_tagsInput = wx.stc.StyledTextCtrl( parent=self.TagsTab, style=wx.stc.STC_STYLE_LINENUMBER )
    tagsText = json.dumps(self.config.getValue("possibleTags", []), indent=4)
    #self.m_tagsInput.SetLexer(wx.stc.STC_LEX_LUA)
    self.m_tagsInput.write(tagsText)
    #self.m_tagsInput.SetMarginType(0, wx.stc.STC_MARGIN_NUMBER)
    #sizer.Add( self.m_tagsInput, 1, wx.EXPAND |wx.ALL, 5 )
    
    #Types Page
    #sizer = self.TypeTab.GetSizer()
    #self.m_typeInput = wx.stc.StyledTextCtrl( parent=self.TypeTab, style=wx.stc.STC_STYLE_LINENUMBER )
    typeText = json.dumps(self.config.getValue("typeGuess", []), indent=4)
    #self.m_typeInput.SetLexer(wx.stc.STC_LEX_LUA)
    self.m_typeInput.write(typeText)
    #self.m_typeInput.SetMarginType(0, wx.stc.STC_MARGIN_NUMBER)
    #sizer.Add( self.m_typeInput, 1, wx.EXPAND |wx.ALL, 5 )
    
  def closeWindow(self, event):
    self.Destroy()
    
  def btnSaveTagsClicked( self, event ):
    text = self.m_tagsInput.GetValue()
    obj = None
    try:
        obj = json.loads(text)
    except Exception as e:
      pprint.pprint(str(e))
      msg = wx.MessageDialog(self, "JSON Error! Please correct the code:\n"+str(e), caption="Error", style=wx.OK|wx.CENTRE)
      msg.ShowModal()
      
    if(obj is not None):
        self.config.setValue("possibleTags", obj)
    
  def btnSaveTypesClicked( self, event ):
    text = self.m_typeInput.GetValue()
    obj = None
    try:
        obj = json.loads(text)
    except Exception as e:
      pprint.pprint(str(e))
      msg = wx.MessageDialog(self, "JSON Error! Please correct the code:\n"+str(e), caption="Error", style=wx.OK|wx.CENTRE)
      msg.ShowModal()
      
    if(obj is not None):
        self.config.setValue("typeGuess", obj)
    
  def createZipsClicked( self, event ):
    self.errorStr = ""
    self.config.setValue("rootDir", self.m_rootDirPicker.GetPath())
    self.config.setValue("outputDir", self.m_outputDirPicker.GetPath())
    
    if(not os.path.isdir(self.m_rootDirPicker.GetPath())):
        self.errorStr += "- Root directory is invalid\n"
    if(not os.path.isdir(self.m_outputDirPicker.GetPath())):
        self.errorStr += "- Output directory is invalid\n"
        
    if(self.errorStr != ""):
        msg = wx.MessageDialog(self, self.errorStr, caption="Error", style=wx.OK|wx.CENTRE)
        msg.ShowModal()
    
    if not self.worker and self.errorStr == "":
        self.m_btnCreateZIPs.Enable(False)
        self.m_btnCancel.Enable(True)
        self.worker = gacWorker(self)
        
  def cancelClicked( self, event ):
      if self.worker:
          self.worker.abort()
    
  def onStatusUpdate(self, msg):
      self.m_statusLabel.SetLabel("%s" % msg)
      
  def onProgressUpdate(self, progress):
      self.m_progressBar.SetValue(progress)
      
  def onWorkerResult(self, event):
    if event.data is False:
        self.m_statusLabel.SetLabel("Cancelled")
    else:
        self.m_statusLabel.SetLabel("Done")

    self.m_btnCreateZIPs.Enable(True)
    self.m_btnCancel.Enable(False)
    pprint.pprint("DONE")
    self.worker = None
    
    
class gacWorker(Thread):
    _want_abort = 0
    _notify_window = None
    config = None
    lock = Lock()
    assets = []
    parsers = {
        "opengameart.org": parserOpengameart(),
        "gamedevmarket.net": parserGamedevmarket(),
        "tokegameart.net": parserTokegameart()
    }
    previewSoundRegex = r'(preview|sample)\.(mp3)'
    previewImageRegex = r'(preview|sample)\.(png|jpg|jpeg|gif)'
    textFileRegex = r'(info|credits|readme|liesmich|license)\.(txt|md)'
    urlFileRegex = r'\.(url)'
    
    overwriteMetaJson = True
    guessTagsFromDescription = False
    descriptionFromTextfile = True
    #at which depth should the directories treated as an asset
    assetDirDepth = 1
    parseAssetUrls = True
    randomPreviewFallback = True
    createSpriteSheetPreview = True

    def __init__(self, notify_window):
        """Init Worker Thread Class."""
        Thread.__init__(self)
        self.setDaemon(True)
        self._notify_window = notify_window
        self.config = self._notify_window.config
        self._want_abort = 0
        
        self.overwriteMetaJson = notify_window.m_overwriteMetaJson.IsChecked()
        self.guessTagsFromDescription = notify_window.m_guessTagsFromDescription.IsChecked()
        #self.descriptionFromTextfile = notify_window.m_descriptionFromTextfile.IsChecked()
        self.parseAssetUrls = notify_window.m_parseWebsites.IsChecked()
        self.assetDirDepth = notify_window.m_assetsStartAtDepth.GetValue()
        self.randomPreviewFallback = notify_window.m_randomPreviewFallback.IsChecked()
        
        self.start()
        
    def run(self):
        #pprint.pprint("Scanning..")
        wx.CallAfter(pub.sendMessage, "update", msg = "Scanning...")
        self._notify_window.m_progressBar.SetValue(0)
        self.assets = []
        self.scanDirs(self._notify_window.m_rootDirPicker.GetPath())
        numAsset = 0
        #pprint.pprint(self.assets)
        for asset in self.assets:
            if(self._want_abort == 0):
                #overriden type?
                if(self._notify_window.m_typeOverride.GetStringSelection() != "Autodetect"):
                  asset["type"] = self._notify_window.m_typeOverride.GetStringSelection()
              
                #Parse Websites
                if(self.parseAssetUrls and asset["url"] is not None):
                    wx.CallAfter(pub.sendMessage, "update", msg = "Parse URL for %s..." % asset["name"])
                    self.parseUrl(asset)
                    
                #Create Spritesheets
                #if(self.createSpriteSheetPreview and asset["preview"] is None):
                #  wx.CallAfter(pub.sendMessage, "update", msg = "Create Spritesheet for %s..." % asset["name"])
                #  self.createSpriteSheet(asset)
                  
                #Random image as preview
                if(self.randomPreviewFallback and asset["preview"] is None):
                  self.createRandomPreview(asset)

                wx.CallAfter(pub.sendMessage, "update", msg = "Create meta.json for %s..." % asset["name"])
                self.createMeta(asset)
                wx.CallAfter(pub.sendMessage, "update", msg = "Zipping %s..." % asset["name"])
                self.createZip(asset, self._notify_window.m_outputDirPicker.GetPath())
            
            numAsset +=1
            wx.CallAfter(pub.sendMessage, "progress", progress = 50 + (float(numAsset) / float(len(self.assets)) * 50))
            
        if(self._want_abort == 0):
            wx.PostEvent(self._notify_window, ResultEvent(True))
        else:
            wx.PostEvent(self._notify_window, ResultEvent(False))
        
    def abort(self):
        # Method for use by main thread to signal an abort
        self._want_abort = 1

    def scanDirs(self, rootPath, subPath="", depth=0, asset={}):
        numRootFolder = 0
        currentPath = os.path.join(rootPath, subPath)
        for (dirpath, dirnames, filenames) in os.walk(currentPath):
          if(self._want_abort == 0):
            for dirname in dirnames:
              if(self._want_abort == 0):
                if(depth == self.assetDirDepth):
                  asset = {}
                  asset["tags"] = {}
                  asset["type"] = None
                  asset["preview"] = None
                  asset["description"] = None
                  asset["url"] = None
                  asset["name"] = dirname.replace("_", " ")
                  asset["zipfilename"] = dirname
                  asset["path"] = os.path.join(currentPath, dirname)
                  type = self.guessType(dirname)
                  asset["type"] = type

                  numRootFolder +=1
                  wx.CallAfter(pub.sendMessage, "progress", progress = float(numRootFolder) / float(len(dirnames)) * 50)
                  wx.CallAfter(pub.sendMessage, "update", msg = "Scanning %s..." % dirname)

                if(depth >= self.assetDirDepth):
                    asset["tags"] = self.guessTags(dirname, asset["tags"])
                    
                self.scanDirs(currentPath, dirname, (depth+1), asset)
                
                if(depth == self.assetDirDepth):
                  if asset["type"] == None:
                    asset["type"] = "2D"
                  self.assets.append(asset)

            for filename in filenames:
              """if("files" not in asset):
                asset["files"] = []
              asset["files"].append(os.path.join(currentPath, filename))"""

              #Tags
              if(depth >= self.assetDirDepth):
                asset["tags"] = self.guessTags(filename, asset["tags"])

              #Type
              if depth >= self.assetDirDepth and asset["type"] == None:
                asset["type"] = self.guessType(filename)

              # Previews
              if depth >= self.assetDirDepth and asset["preview"] == None:
                if(depth == self.assetDirDepth):
                  #Look for preview file in root
                  if(asset["type"] == "Audio"):
                    output = re.search(self.previewSoundRegex, filename, flags=re.IGNORECASE)
                    if output is not None:
                      asset["preview"] = filename
                  else:
                    output = re.search(self.previewImageRegex, filename, flags=re.IGNORECASE)
                    if output is not None:
                      asset["preview"] = filename

                else:
                  # look in subdirs for a reasonable file
                  relPath = dirpath.replace(asset["path"], "")
                  if(asset["type"] == "Audio"):
                    output = re.search(self.previewSoundRegex, filename, flags=re.IGNORECASE)
                    if output is not None:
                      asset["preview"] = os.path.join(relPath, filename)
                  else:
                    output = re.search(self.previewImageRegex, filename, flags=re.IGNORECASE)
                    if output is not None:
                      asset["preview"] = os.path.join(relPath, filename)

              #Description
              if depth >= self.assetDirDepth and asset["description"] == None:
                if(self.descriptionFromTextfile):
                  output = re.search(self.textFileRegex, filename, flags=re.IGNORECASE)
                  if output is not None:
                    with open(os.path.join(dirpath, filename), mode="r", encoding='utf-8', errors='ignore') as read_file:
                      asset["description"] = read_file.read()
                      if(self.guessTagsFromDescription):
                        asset["tags"] = self.guessTags(asset["description"], asset["tags"])

              #URL
              if(depth >= self.assetDirDepth):
                output = re.search(self.textFileRegex, filename, flags=re.IGNORECASE)
                if output is not None:
                  with open(os.path.join(dirpath, filename), mode="r", errors='ignore') as read_file:
                    asset["url"] = self.guessUrl(read_file.read(), asset["url"])
                else:
                  output = re.search(self.urlFileRegex, filename, flags=re.IGNORECASE)
                  if output is not None:
                    with open(os.path.join(dirpath, filename), mode="r", errors='ignore') as read_file:
                      asset["url"] = self.guessUrl(read_file.read(), asset["url"])
            break

  
    def guessType(self, text):
        guesses = self.config.getValue("typeGuess", {"2D":[],"3D":[],"Audio":[],"gui":[]})
        for type in guesses:
          for value in guesses[type]:
            regex = '[^a-zA-Z]'+value+'[^a-zA-Z]'
            text = ' '+text+' '
            output = re.search(regex, text, flags=re.IGNORECASE)
            if output is not None:
              return type
        return None
  
    def guessTags(self, text, tags={}):
        posTags = self.config.getValue("possibleTags", [])
        for posTag in posTags:
          if isinstance(posTag, dict):
            # Multiple searchwords for one tag
            key = next(iter(posTag))
            searchWords = posTag[key]
            posTag = key
            for searchWord in searchWords:
              regex = searchWord
              output = re.search(regex, text, flags=re.IGNORECASE)
              if output is not None:
                tags[posTag] = posTag
          else:
            regex = ''+posTag+''
            #text = ' '+text+' '
            output = re.search(regex, text, flags=re.IGNORECASE)
            if output is not None:
              tags[posTag] = posTag
              
        # add overriden tags
        addTags = self._notify_window.m_addTags.GetValue().split(";")
        for addTag in addTags:
          addTag = addTag.strip()
          if(addTag != ""):
            tags[addTag] = addTag
              
        return tags
  
    def guessUrl(self, text, currentURL):
        url = None
        # first, priorize some known urls
        domains = self.config.getValue("knownAssetDomains", [])
        domainsStr = '|'.join(domains)
        regex = r'http[s]?://(www\.)?('+domainsStr+')([-a-zA-Z0-9@:%_\\+.~#?&//=]*)?'

        # does the asset already have one of the known domains?
        if(currentURL is not None):
          hasKnownDomain = re.search(regex, currentURL, flags=re.IGNORECASE)
          if(hasKnownDomain is not None):
            return currentURL

        # currentURL has none of the known domains. Search text for it
        matches = re.search(regex, text, flags=re.IGNORECASE)
        if(matches is not None):
          url = matches.group(0)
        # No preferred URL found. Take the first one we find
        if(url is None):
          matches = re.search(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)?', text, flags=re.IGNORECASE)
          if(matches is not None):
            url = matches.group(0)

        return url
    
    def parseUrl(self, asset):
        if(asset["url"] is None):
            return None
        #check if the url is one of our parsers
        for parserDomain in self.parsers:
            regex = r'http[s]?:\/\/(www\.)?('+parserDomain+')([-a-zA-Z0-9@:%_\\+.~#?&//=]*)?'
            matches = re.search(regex, asset["url"], flags=re.IGNORECASE)
            if(matches is not None):
                parser = self.parsers[parserDomain]
                parserData = parser.parse(asset["url"], asset)
                if("tags" in parserData and len(parserData["tags"]) > 0):
                    for tag in parserData["tags"]:
                        asset["tags"][tag] = tag
                if("description" in parserData and parserData["description"] != ""):
                    asset["description"] = parserData["description"]
                if("name" in parserData and parserData["name"] != ""):
                    asset["name"] = parserData["name"]
                        
    def createSpriteSheet(self, asset):
      pass
    
    def createRandomPreview(self, asset):
      for (dirpath, dirnames, filenames) in os.walk(asset["path"]):
        for filename in filenames:
          matches = re.search('\.(png|gif|jpg|jpeg)', filename)
          if(matches is not None):
            asset["preview"] = os.path.join(dirpath.replace(asset["path"], ""), filename)
            #pprint.pprint(asset["preview"])
            break
        if(asset["preview"] is not None):
          break
  
    def createMeta(self, asset):
        meta = {
          "name": asset["name"],
          "type": asset["type"]
        }
        if(len(asset["tags"]) > 0):
          meta["tags"] = []
          for tag in asset["tags"]:
            meta["tags"].append(tag)
        if(asset["preview"] is not None):
          meta["preview"] = asset["preview"].replace('\\', '/')
        if(asset["description"] is not None):
          meta["description"] = asset["description"]
        if(asset["url"] is not None):
          meta["url"] = asset["url"]

        if(self.overwriteMetaJson):
          with open(os.path.join(asset["path"], "meta.json"), "w") as write_file:
            json.dump(meta, write_file)
        else:
          with open(os.path.join(asset["path"], "meta.json"), "r") as read_file:
            data = json.load(read_file)
            meta = merge_two_dicts(data, meta)

          with open(os.path.join(asset["path"], "meta.json"), "w") as write_file:
            json.dump(meta, write_file)
  
    def createZip(self, asset, outputDir):
        output_filename = os.path.join(outputDir, asset["zipfilename"])
        shutil.make_archive(output_filename, 'zip', asset["path"])
  
  
def merge_two_dicts(x, y):
  z = x.copy()
  z.update(y)
  return z

app = wx.App(False)
#create an object of CalcFrame
frame = gacDialog(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
