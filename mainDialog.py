# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class mainDialog
###########################################################################

class mainDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"GameAssetCreator", pos = wx.DefaultPosition, size = wx.Size( 500,580 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.Size( 500,580 ), wx.Size( 500,580 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.GeneralTab = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 0, 2, 10, 10 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText1 = wx.StaticText( self.GeneralTab, wx.ID_ANY, u"Asset Root Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1, 1, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

		self.m_rootDirPicker = wx.DirPickerCtrl( self.GeneralTab, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer1.Add( self.m_rootDirPicker, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( self.GeneralTab, wx.ID_ANY, u"Assets start at depth", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer1.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_assetsStartAtDepth = wx.SpinCtrl( self.GeneralTab, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 2, 0 )
		fgSizer1.Add( self.m_assetsStartAtDepth, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( self.GeneralTab, wx.ID_ANY, u"ZIP Output Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer1.Add( self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

		self.m_outputDirPicker = wx.DirPickerCtrl( self.GeneralTab, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		fgSizer1.Add( self.m_outputDirPicker, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText111 = wx.StaticText( self.GeneralTab, wx.ID_ANY, u"Overwrite meta.json", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111.Wrap( -1 )

		fgSizer1.Add( self.m_staticText111, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

		self.m_overwriteMetaJson = wx.CheckBox( self.GeneralTab, wx.ID_ANY, u"Overwrite or append", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_overwriteMetaJson.SetValue(True)
		fgSizer1.Add( self.m_overwriteMetaJson, 0, wx.ALL, 5 )

		self.m_staticText1111 = wx.StaticText( self.GeneralTab, wx.ID_ANY, u"Parse websites (may be slow)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1111.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1111, 0, wx.ALL, 5 )

		self.m_parseWebsites = wx.CheckBox( self.GeneralTab, wx.ID_ANY, u"Parse URLs to get extra data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_parseWebsites.SetValue(True)
		fgSizer1.Add( self.m_parseWebsites, 0, wx.ALL, 5 )

		self.m_staticText11111 = wx.StaticText( self.GeneralTab, wx.ID_ANY, u"Guess tags from description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11111.Wrap( -1 )

		fgSizer1.Add( self.m_staticText11111, 0, wx.ALL, 5 )

		self.m_guessTagsFromDescription = wx.CheckBox( self.GeneralTab, wx.ID_ANY, u"Search description for possible tags", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_guessTagsFromDescription, 0, wx.ALL, 5 )

		self.m_staticText111111 = wx.StaticText( self.GeneralTab, wx.ID_ANY, u"Pick random preview", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText111111.Wrap( -1 )

		fgSizer1.Add( self.m_staticText111111, 0, wx.ALL, 5 )

		self.m_randomPreviewFallback = wx.CheckBox( self.GeneralTab, wx.ID_ANY, u"if otherwise none is found", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_randomPreviewFallback.SetValue(True)
		fgSizer1.Add( self.m_randomPreviewFallback, 0, wx.ALL, 5 )

		self.m_staticText121 = wx.StaticText( self.GeneralTab, wx.ID_ANY, u"Add Tags to all ( ; separated)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText121.Wrap( -1 )

		fgSizer1.Add( self.m_staticText121, 0, wx.ALL, 5 )

		self.m_addTags = wx.TextCtrl( self.GeneralTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_addTags, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )

		self.m_staticText1211 = wx.StaticText( self.GeneralTab, wx.ID_ANY, u"Override Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1211.Wrap( -1 )

		fgSizer1.Add( self.m_staticText1211, 0, wx.ALL, 5 )

		m_typeOverrideChoices = [ u"Autodetect", u"2D", u"3D", u"Audio", u"GUI" ]
		self.m_typeOverride = wx.ComboBox( self.GeneralTab, wx.ID_ANY, u"- Select a type -", wx.DefaultPosition, wx.DefaultSize, m_typeOverrideChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.m_typeOverride.SetSelection( 0 )
		fgSizer1.Add( self.m_typeOverride, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )


		self.GeneralTab.SetSizer( fgSizer1 )
		self.GeneralTab.Layout()
		fgSizer1.Fit( self.GeneralTab )
		self.m_notebook1.AddPage( self.GeneralTab, u"General", False )
		self.TagsTab = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText23 = wx.StaticText( self.TagsTab, wx.ID_ANY, u"Specify the tags you want to use.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.SetLabelMarkup( u"Specify the tags you want to use." )
		self.m_staticText23.Wrap( -1 )

		bSizer9.Add( self.m_staticText23, 2, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self.TagsTab, wx.ID_ANY, u"Documentation", u"https://www.gameassetmanager.com/documentation/gameassetcreator/", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		bSizer9.Add( self.m_hyperlink1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_btnSaveTags = wx.Button( self.TagsTab, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_btnSaveTags.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		bSizer9.Add( self.m_btnSaveTags, 1, wx.ALIGN_CENTER|wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer8.Add( bSizer9, 0, wx.EXPAND, 5 )

		self.m_tagsInput = wx.TextCtrl( self.TagsTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB )
		bSizer8.Add( self.m_tagsInput, 1, wx.ALL|wx.EXPAND, 5 )


		self.TagsTab.SetSizer( bSizer8 )
		self.TagsTab.Layout()
		bSizer8.Fit( self.TagsTab )
		self.m_notebook1.AddPage( self.TagsTab, u"Tags", False )
		self.TypeTab = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer81 = wx.BoxSizer( wx.VERTICAL )

		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText231 = wx.StaticText( self.TypeTab, wx.ID_ANY, u"Mapping between type <-> searchword", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText231.Wrap( -1 )

		bSizer91.Add( self.m_staticText231, 2, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_hyperlink11 = wx.adv.HyperlinkCtrl( self.TypeTab, wx.ID_ANY, u"Documentation", u"https://www.gameassetmanager.com/documentation/gameassetcreator/", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		bSizer91.Add( self.m_hyperlink11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_btnSaveTags1 = wx.Button( self.TypeTab, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_btnSaveTags1.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE, wx.ART_BUTTON ) )
		bSizer91.Add( self.m_btnSaveTags1, 1, wx.ALIGN_CENTER|wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer81.Add( bSizer91, 0, wx.EXPAND, 5 )

		self.m_typeInput = wx.TextCtrl( self.TypeTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB )
		bSizer81.Add( self.m_typeInput, 1, wx.ALL|wx.EXPAND, 5 )


		self.TypeTab.SetSizer( bSizer81 )
		self.TypeTab.Layout()
		bSizer81.Fit( self.TypeTab )
		self.m_notebook1.AddPage( self.TypeTab, u"Types", False )
		self.AboutTab = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )


		bSizer14.Add( ( 10, 10), 0, wx.EXPAND, 5 )

		self.m_bitmap2 = wx.StaticBitmap( self.AboutTab, wx.ID_ANY, wx.Bitmap( u"logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_bitmap2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self.AboutTab, wx.ID_ANY, u"<big>GameAssetCreator V0.9</big>\nA tool to create asset zip files for the GameAssetManager", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText29.SetLabelMarkup( u"<big>GameAssetCreator V0.9</big>\nA tool to create asset zip files for the GameAssetManager" )
		self.m_staticText29.Wrap( -1 )

		bSizer14.Add( self.m_staticText29, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( ( 10, 10), 0, wx.EXPAND, 5 )

		self.m_staticText291 = wx.StaticText( self.AboutTab, wx.ID_ANY, u"Developed by:\nDaniel Lichtblau", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText291.SetLabelMarkup( u"Developed by:\nDaniel Lichtblau" )
		self.m_staticText291.Wrap( -1 )

		bSizer14.Add( self.m_staticText291, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( ( 500, 30), 0, wx.EXPAND, 5 )

		self.m_staticText2911 = wx.StaticText( self.AboutTab, wx.ID_ANY, u"Homepage:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText2911.SetLabelMarkup( u"Homepage:" )
		self.m_staticText2911.Wrap( -1 )

		bSizer14.Add( self.m_staticText2911, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )

		self.m_hyperlink5 = wx.adv.HyperlinkCtrl( self.AboutTab, wx.ID_ANY, u"www.gameassetmanager.com", u"https://www.gameassetmanager.com", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_ALIGN_CENTRE|wx.adv.HL_DEFAULT_STYLE )
		bSizer14.Add( self.m_hyperlink5, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )

		self.m_hyperlink4 = wx.adv.HyperlinkCtrl( self.AboutTab, wx.ID_ANY, u"Documentation", u"https://www.gameassetmanager.com/documentation/gameassetcreator/", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_ALIGN_CENTRE|wx.adv.HL_DEFAULT_STYLE )
		bSizer14.Add( self.m_hyperlink4, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )


		self.AboutTab.SetSizer( bSizer14 )
		self.AboutTab.Layout()
		bSizer14.Fit( self.AboutTab )
		self.m_notebook1.AddPage( self.AboutTab, u"About", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_progressBar = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL|wx.GA_SMOOTH )
		self.m_progressBar.SetValue( 0 )
		bSizer3.Add( self.m_progressBar, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_statusLabel = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_statusLabel.Wrap( -1 )

		bSizer3.Add( self.m_statusLabel, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_btnCreateZIPs = wx.Button( self, wx.ID_ANY, u"Create ZIPs", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_btnCreateZIPs.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_EXECUTABLE_FILE, wx.ART_BUTTON ) )
		bSizer4.Add( self.m_btnCreateZIPs, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		self.m_btnCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_btnCancel.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_CROSS_MARK, wx.ART_BUTTON ) )
		bSizer4.Add( self.m_btnCancel, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer4, 0, wx.ALIGN_CENTER, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_btnSaveTags.Bind( wx.EVT_BUTTON, self.btnSaveTagsClicked )
		self.m_btnSaveTags1.Bind( wx.EVT_BUTTON, self.btnSaveTypesClicked )
		self.m_btnCreateZIPs.Bind( wx.EVT_BUTTON, self.createZipsClicked )
		self.m_btnCancel.Bind( wx.EVT_BUTTON, self.cancelClicked )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnSaveTagsClicked( self, event ):
		event.Skip()

	def btnSaveTypesClicked( self, event ):
		event.Skip()

	def createZipsClicked( self, event ):
		event.Skip()

	def cancelClicked( self, event ):
		event.Skip()


