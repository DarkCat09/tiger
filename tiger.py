# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class frameMain
###########################################################################

class frameMain ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tiger (ReTag3) by DarkCat09", pos = wx.DefaultPosition, size = wx.Size( 770,465 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.menuBar1 = wx.MenuBar( 0 )
		self.fileMenu = wx.Menu()
		self.filePlayItem = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"Play", wx.EmptyString, wx.ITEM_NORMAL )
		self.fileMenu.Append( self.filePlayItem )

		self.fileMenu.AppendSeparator()

		self.fileRenameItem = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"Rename", wx.EmptyString, wx.ITEM_NORMAL )
		self.fileMenu.Append( self.fileRenameItem )

		self.fileRetagItem = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"ReTag", wx.EmptyString, wx.ITEM_NORMAL )
		self.fileMenu.Append( self.fileRetagItem )

		self.fileDeleteItem = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.fileMenu.Append( self.fileDeleteItem )

		self.fileMenu.AppendSeparator()

		self.fileExitItem = wx.MenuItem( self.fileMenu, wx.ID_ANY, u"Exit"+ u"\t" + u"CTRL+Q", wx.EmptyString, wx.ITEM_NORMAL )
		self.fileMenu.Append( self.fileExitItem )

		self.menuBar1.Append( self.fileMenu, u"File" )

		self.editMenu = wx.Menu()
		self.editCopyItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Copy tags", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editCopyItem )

		self.editPasteItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Paste tags", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editPasteItem )

		self.editPasteAllItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Paste tags to selected file(s)", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editPasteAllItem )

		self.editMenu.AppendSeparator()

		self.editRetagItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"ReTag file(s)", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editRetagItem )

		self.editRenameItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Rename file(s)", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editRenameItem )

		self.editTagByNameItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"ReTag by filename", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editTagByNameItem )

		self.editNameByTagItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Rename by tag", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editNameByTagItem )

		self.editMenu.AppendSeparator()

		self.editAddCoverItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Add cover for file(s)", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editAddCoverItem )

		self.editRemoveCoverItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Remove cover from file(s)", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editRemoveCoverItem )

		self.editExtractCoverItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Extract cover from file", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editExtractCoverItem )

		self.editMenu.AppendSeparator()

		self.editSwapTagsItem = wx.Menu()
		self.swapTitleArtistItem = wx.MenuItem( self.editSwapTagsItem, wx.ID_ANY, u"Title and Author", wx.EmptyString, wx.ITEM_NORMAL )
		self.editSwapTagsItem.Append( self.swapTitleArtistItem )

		self.swapAlbumTitleItem = wx.MenuItem( self.editSwapTagsItem, wx.ID_ANY, u"Album and Title", wx.EmptyString, wx.ITEM_NORMAL )
		self.editSwapTagsItem.Append( self.swapAlbumTitleItem )

		self.swapAlbumArtistItem = wx.MenuItem( self.editSwapTagsItem, wx.ID_ANY, u"Album and Author", wx.EmptyString, wx.ITEM_NORMAL )
		self.editSwapTagsItem.Append( self.swapAlbumArtistItem )

		self.editMenu.AppendSubMenu( self.editSwapTagsItem, u"Swap tags" )

		self.editMenu.AppendSeparator()

		self.editFormatTrimItem = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Trim tags (remove spaces)", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editFormatTrimItem )

		self.editFormatTrack = wx.Menu()
		self.formatTrackNumItem = wx.MenuItem( self.editFormatTrack, wx.ID_ANY, u"To x", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatTrack.Append( self.formatTrackNumItem )

		self.formatTrackZeroNumItem = wx.MenuItem( self.editFormatTrack, wx.ID_ANY, u"To 0x", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatTrack.Append( self.formatTrackZeroNumItem )

		self.formatTrackZeroesNumItem = wx.MenuItem( self.editFormatTrack, wx.ID_ANY, u"To 00x", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatTrack.Append( self.formatTrackZeroesNumItem )

		self.formatTrackZeroesAutoItem = wx.MenuItem( self.editFormatTrack, wx.ID_ANY, u"Automatically count zeroes (to 0...x)", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatTrack.Append( self.formatTrackZeroesAutoItem )

		self.formatTrackSlashItem = wx.MenuItem( self.editFormatTrack, wx.ID_ANY, u"To xx/xx", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatTrack.Append( self.formatTrackSlashItem )

		self.formatTrackNumsItem = wx.MenuItem( self.editFormatTrack, wx.ID_ANY, u"To xx", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatTrack.Append( self.formatTrackNumsItem )

		self.editMenu.AppendSubMenu( self.editFormatTrack, u"Format track tag" )

		self.editFormatArtist = wx.Menu()
		self.formatArtistRemoveTheItem = wx.MenuItem( self.editFormatArtist, wx.ID_ANY, u"Remove \"The\"", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatArtist.Append( self.formatArtistRemoveTheItem )

		self.formatArtistEndTheItem = wx.MenuItem( self.editFormatArtist, wx.ID_ANY, u"To Artist, the", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatArtist.Append( self.formatArtistEndTheItem )

		self.formatArtistBeginTheItem = wx.MenuItem( self.editFormatArtist, wx.ID_ANY, u"To The Artist", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatArtist.Append( self.formatArtistBeginTheItem )

		self.formatArtistNsItem = wx.MenuItem( self.editFormatArtist, wx.ID_ANY, u"To Name Surname", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatArtist.Append( self.formatArtistNsItem )

		self.formatArtistSnCommaItem = wx.MenuItem( self.editFormatArtist, wx.ID_ANY, u"To Surname, Name", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatArtist.Append( self.formatArtistSnCommaItem )

		self.formatArtistSnItem = wx.MenuItem( self.editFormatArtist, wx.ID_ANY, u"To Surname Name", wx.EmptyString, wx.ITEM_NORMAL )
		self.editFormatArtist.Append( self.formatArtistSnItem )

		self.editMenu.AppendSubMenu( self.editFormatArtist, u"Format author tag" )

		self.editMenu.AppendSeparator()

		self.editEncoding = wx.MenuItem( self.editMenu, wx.ID_ANY, u"Fix encoding", wx.EmptyString, wx.ITEM_NORMAL )
		self.editMenu.Append( self.editEncoding )

		self.menuBar1.Append( self.editMenu, u"Edit" )

		self.optionsMenu = wx.Menu()
		self.menuBar1.Append( self.optionsMenu, u"Options" )

		self.helpMenu = wx.Menu()
		self.helpDocsItem = wx.MenuItem( self.helpMenu, wx.ID_ANY, u"Documentation", wx.EmptyString, wx.ITEM_NORMAL )
		self.helpMenu.Append( self.helpDocsItem )

		self.helpWebSiteItem = wx.MenuItem( self.helpMenu, wx.ID_ANY, u"Web Site", wx.EmptyString, wx.ITEM_NORMAL )
		self.helpMenu.Append( self.helpWebSiteItem )

		self.helpAboutProg = wx.MenuItem( self.helpMenu, wx.ID_ANY, u"About Tiger", wx.EmptyString, wx.ITEM_NORMAL )
		self.helpMenu.Append( self.helpAboutProg )

		self.helpAboutDeveloper = wx.MenuItem( self.helpMenu, wx.ID_ANY, u"About Developer (DarkCat09)", wx.EmptyString, wx.ITEM_NORMAL )
		self.helpMenu.Append( self.helpAboutDeveloper )

		self.helpWxInfoItem = wx.MenuItem( self.helpMenu, wx.ID_ANY, u"About wxWidgets", wx.EmptyString, wx.ITEM_NORMAL )
		self.helpMenu.Append( self.helpWxInfoItem )

		self.menuBar1.Append( self.helpMenu, u"Help" )

		self.SetMenuBar( self.menuBar1 )

		mainSizer = wx.BoxSizer( wx.VERTICAL )

		topSizer = wx.GridSizer( 0, 2, 0, 0 )

		self.renameTabs = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.multiRenamePanel = wx.Panel( self.renameTabs, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.renameTabs.AddPage( self.multiRenamePanel, u"Rename files", False )
		self.multiRetagPanel = wx.Panel( self.renameTabs, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.renameTabs.AddPage( self.multiRetagPanel, u"ReTag files", False )
		self.getTagsPanel = wx.Panel( self.renameTabs, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.renameTabs.AddPage( self.getTagsPanel, u"Get Tags from Name", False )

		topSizer.Add( self.renameTabs, 1, wx.EXPAND, 5 )

		self.coverBook = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.coverPanel = wx.Panel( self.coverBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		coverBoxLayout = wx.BoxSizer( wx.VERTICAL )

		coverToolsWrapLayout = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		coverSourceChoiceChoices = [ u"Directory cover", u"File cover" ]
		self.coverSourceChoice = wx.Choice( self.coverPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, coverSourceChoiceChoices, 0 )
		self.coverSourceChoice.SetSelection( 0 )
		coverToolsWrapLayout.Add( self.coverSourceChoice, 0, wx.ALL, 5 )

		self.removeCoverButton = wx.Button( self.coverPanel, wx.ID_ANY, u"Remove cover", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.removeCoverButton.SetBitmap( wx.Bitmap( u"icons/rm_cover.png", wx.BITMAP_TYPE_ANY ) )
		coverToolsWrapLayout.Add( self.removeCoverButton, 0, wx.ALL, 5 )

		self.applyCoverButton = wx.Button( self.coverPanel, wx.ID_ANY, u"Apply to all", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.applyCoverButton.SetBitmap( wx.Bitmap( u"icons/dl_cover_all.png", wx.BITMAP_TYPE_ANY ) )
		coverToolsWrapLayout.Add( self.applyCoverButton, 0, wx.ALL, 5 )


		coverBoxLayout.Add( coverToolsWrapLayout, 1, wx.EXPAND, 5 )

		self.coverBitmap = wx.StaticBitmap( self.coverPanel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		coverBoxLayout.Add( self.coverBitmap, 0, wx.ALL, 5 )


		self.coverPanel.SetSizer( coverBoxLayout )
		self.coverPanel.Layout()
		coverBoxLayout.Fit( self.coverPanel )
		self.coverBook.AddPage( self.coverPanel, u"a page", False )

		topSizer.Add( self.coverBook, 1, wx.EXPAND, 5 )


		mainSizer.Add( topSizer, 1, wx.EXPAND, 5 )

		self.retagToolBar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL )
		self.refreshTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Refresh", wx.Bitmap( u"icons/swap_arrow.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Refresh", wx.EmptyString, None )

		self.searchTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Search", wx.Bitmap( u"icons/search.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Search file(s)", wx.EmptyString, None )

		self.retagToolBar.AddSeparator()

		self.retagTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"ReTag file", wx.Bitmap( u"icons/pencil.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"ReTag", wx.EmptyString, None )

		self.retagAllTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"ReTag files", wx.Bitmap( u"icons/retag_all.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"ReTag All", wx.EmptyString, None )

		self.renameTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Rename file", wx.Bitmap( u"icons/rename_field.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Rename", wx.EmptyString, None )

		self.renameDirTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Rename directory", wx.Bitmap( u"icons/rename_dir.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Rename Directory", wx.EmptyString, None )

		self.retagToolBar.AddSeparator()

		self.copyTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Copy tags", wx.Bitmap( u"icons/copy.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Copy Tags", wx.EmptyString, None )

		self.pasteTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Paste tags", wx.Bitmap( u"icons/paste.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Paste Tags", wx.EmptyString, None )

		self.pasteAllTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Paste tags to files", wx.Bitmap( u"icons/paste_all.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Paste Tags to All", wx.EmptyString, None )

		self.retagToolBar.AddSeparator()

		self.playTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Play file", wx.Bitmap( u"icons/play.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Play File", wx.EmptyString, None )

		self.playAllTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Play all files", wx.Bitmap( u"icons/play.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Play All", wx.EmptyString, None )

		self.retagToolBar.AddSeparator()

		self.downloadTagsTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Download tags", wx.Bitmap( u"icons/dl_tags.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Download Tags", wx.EmptyString, None )

		self.downloadAllTags = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Download tags for all", wx.Bitmap( u"icons/dl_tags_all.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Download Tags for All", wx.EmptyString, None )

		self.downloadCover = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"Download file cover", wx.Bitmap( u"icons/dl_cover.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Download Cover", wx.EmptyString, None )

		self.downloadDirCoverTool = self.retagToolBar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/dl_cover_all.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Download Cover for Album", wx.EmptyString, None )

		self.retagToolBar.Realize()

		mainSizer.Add( self.retagToolBar, 0, wx.EXPAND, 5 )

		bottomSizer = wx.BoxSizer( wx.VERTICAL )

		self.addressBook = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addressBook.SetMaxSize( wx.Size( -1,35 ) )

		self.addressPanel = wx.Panel( self.addressBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		addressSizer = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.addressLabel = wx.StaticText( self.addressPanel, wx.ID_ANY, u"Address:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addressLabel.Wrap( -1 )

		addressSizer.Add( self.addressLabel, 0, wx.ALL, 5 )

		self.addressDirPicker = wx.DirPickerCtrl( self.addressPanel, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		addressSizer.Add( self.addressDirPicker, 0, wx.ALL, 3 )


		self.addressPanel.SetSizer( addressSizer )
		self.addressPanel.Layout()
		addressSizer.Fit( self.addressPanel )
		self.addressBook.AddPage( self.addressPanel, u"a page", False )

		bottomSizer.Add( self.addressBook, 0, wx.EXPAND, 5 )

		self.filterBook = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.filterBook.SetMaxSize( wx.Size( -1,35 ) )

		self.filterPanel = wx.Panel( self.filterBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		filterSizer = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.filterLabel = wx.StaticText( self.filterPanel, wx.ID_ANY, u"Filter by", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.filterLabel.Wrap( -1 )

		filterSizer.Add( self.filterLabel, 0, wx.ALL, 5 )

		filterTypeChoiceChoices = [ u"File Name", u"Title", u"Artist", u"Album", u"Genre", u"Track #" ]
		self.filterTypeChoice = wx.Choice( self.filterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, filterTypeChoiceChoices, 0 )
		self.filterTypeChoice.SetSelection( 0 )
		filterSizer.Add( self.filterTypeChoice, 0, wx.ALL, 4 )

		self.filterTextCtrl = wx.TextCtrl( self.filterPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		filterSizer.Add( self.filterTextCtrl, 0, wx.ALL, 4 )

		self.filterButton = wx.Button( self.filterPanel, wx.ID_ANY, u"Filter!", wx.DefaultPosition, wx.DefaultSize, 0 )
		filterSizer.Add( self.filterButton, 0, wx.ALL, 3 )

		self.filterSeparator = wx.StaticLine( self.filterPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		filterSizer.Add( self.filterSeparator, 0, wx.EXPAND |wx.ALL, 3 )

		self.filterHideFiles = wx.Button( self.filterPanel, wx.ID_ANY, u"Hide Selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		filterSizer.Add( self.filterHideFiles, 0, wx.ALL, 3 )

		self.filterShowFiles = wx.Button( self.filterPanel, wx.ID_ANY, u"Show All", wx.DefaultPosition, wx.DefaultSize, 0 )
		filterSizer.Add( self.filterShowFiles, 0, wx.ALL, 3 )


		self.filterPanel.SetSizer( filterSizer )
		self.filterPanel.Layout()
		filterSizer.Fit( self.filterPanel )
		self.filterBook.AddPage( self.filterPanel, u"a page", False )

		bottomSizer.Add( self.filterBook, 0, wx.EXPAND, 5 )

		self.dirsBook = wx.Simplebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dirsPanel = wx.Panel( self.dirsBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		dirsSizer = wx.GridSizer( 0, 2, 0, 0 )

		self.dirsGenericList1 = wx.GenericDirCtrl( self.dirsPanel, wx.ID_ANY, u"/", wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.DIRCTRL_DIR_ONLY|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.dirsGenericList1.ShowHidden( False )
		dirsSizer.Add( self.dirsGenericList1, 1, wx.EXPAND |wx.ALL, 5 )

		self.dirsMusicList = wx.dataview.TreeListCtrl( self.dirsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_CHECKBOX|wx.dataview.TL_MULTIPLE )

		dirsSizer.Add( self.dirsMusicList, 1, wx.EXPAND |wx.ALL, 5 )


		self.dirsPanel.SetSizer( dirsSizer )
		self.dirsPanel.Layout()
		dirsSizer.Fit( self.dirsPanel )
		self.dirsBook.AddPage( self.dirsPanel, u"a page", False )

		bottomSizer.Add( self.dirsBook, 2, wx.EXPAND, 5 )


		mainSizer.Add( bottomSizer, 2, wx.EXPAND, 5 )


		self.SetSizer( mainSizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.OnExit, id = self.fileExitItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnWebsiteClick, id = self.helpWebSiteItem.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAboutClick, id = self.helpAboutProg.GetId() )
		self.Bind( wx.EVT_MENU, self.OnAboutDevClick, id = self.helpAboutDeveloper.GetId() )
		self.Bind( wx.EVT_MENU, self.OnWxInfoClick, id = self.helpWxInfoItem.GetId() )
		self.addressDirPicker.Bind( wx.EVT_DIRPICKER_CHANGED, self.OnDirectorySelected )
		self.dirsGenericList1.Bind( wx.EVT_DIRCTRL_SELECTIONCHANGED, self.OnDirectorySelected )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnExit( self, event ):
		event.Skip()

	def OnWebsiteClick( self, event ):
		event.Skip()

	def OnAboutClick( self, event ):
		event.Skip()

	def OnAboutDevClick( self, event ):
		event.Skip()

	def OnWxInfoClick( self, event ):
		event.Skip()

	def OnDirectorySelected( self, event ):
		event.Skip()



