"""Subclass of frameMain, which is generated by wxFormBuilder."""

import wx
import wx.adv
import tiger

import os
import re
import threading
import webbrowser

# Implementing frameMain
class TigerframeMain(tiger.frameMain):
	def __init__(self, parent):
		tiger.frameMain.__init__(self, parent)
		self.dirsGenericList1.SetDefaultFolder(os.path.expanduser('~'))
		self.dirsMusicList.AppendColumn('Filename')
		self.dirsMusicList.AppendColumn('Title')
		self.dirsMusicList.AppendColumn('Album')
		self.dirsMusicList.AppendColumn('Artist')
		self.dirsMusicList.AppendColumn('Year')
		self.dirsMusicList.AppendColumn('Genre')
		self.dirsMusicList.AppendColumn('Track')

	# Handlers for frameMain events
	def OnExit(self, event):
		self.Close()

	def OnWebsiteClick(self, event):
		webbrowser.open('http://darkcat09.github.io/tiger')

	def OnAboutClick(self, event):
		aboutText = '''
		Tiger (formerly ReTag3) is an open-source replacement for Tag&Rename.
		It can edit ID3-tags (ReTag), download cover and lyrics,
		import/export tags, rename files by mask, and much more...
		Developed by DarkCat09. Hello from Russia! :)'''
		#wx.MessageDialog(self, aboutText, 'About Tiger (ReTag3)', wx.OK).ShowModal()
		about = wx.adv.AboutDialogInfo()
		about.Name = 'Tiger/ReTag3'
		about.Version = '0.2 beta'
		about.Copyright = '(C) 2021 Чечкенёв Андрей'
		about.Description = aboutText
		about.WebSite = ('http://darkcat09.github.io/tiger', 'Official web-site and documentation')
		about.Developers = ['Chechkenev Andrey (@DarkCat09)']
		wx.adv.AboutBox(about)

	def OnAboutDevClick(self, event):
		# TODO
		pass

	def OnWxInfoClick(self, event):
		wx.InfoMessageBox(self)

	def OnDirectorySelected(self, event):
		if (isinstance(event, wx.TreeEvent)):
			directory = self.dirsGenericList1.GetPath()
		else:
			directory = event.GetPath()
		#wx.MessageDialog(self, 'Path:' + directory, 'Tiger - Debug', wx.OK).ShowModal()
		updateThread = threading.Thread(target=self.UpdateMusicList, args=(directory,), daemon=True)
		updateThread.start()
		print('started!')

	def UpdateMusicList(self, directory):
		addedDirs = {}
		splitPath = re.compile(r'/\\')
		self.dirsMusicList.DeleteAllItems()
		for root, dirs, files in os.walk(directory):
			for file in files:
				if (file[file.rfind('.'):] == '.mp3'):
					filedirs = splitPath.split(root) + [file]
					print(root)
					print(file)
					for item in range(len(filedirs) - 1):
						for dirname in addedDirs:
							if (filedirs[item] == dirname):
								break
						else:
							rootdir = self.dirsMusicList.GetRootItem()
							if (item > 0):
								rootdir = addedDirs[filedirs[item - 1]]
							addedDirs[filedirs[item]] = self.dirsMusicList.AppendItem(rootdir, filedirs[item])
							self.dirsMusicList.SetItemText(addedDirs[filedirs[item]], 1, 'Title')
							self.dirsMusicList.SetItemText(addedDirs[filedirs[item]], 2, 'Album')
							self.dirsMusicList.SetItemText(addedDirs[filedirs[item]], 3, 'Artist')
							self.dirsMusicList.SetItemText(addedDirs[filedirs[item]], 4, 'Year')
							self.dirsMusicList.SetItemText(addedDirs[filedirs[item]], 5, 'Genre')
							self.dirsMusicList.SetItemText(addedDirs[filedirs[item]], 6, 'Track')
		print('done!')


class MainApp(wx.App):
	def OnInit(self):
		mainFrame = TigerframeMain(None)
		mainFrame.Show(True)
		return True


if __name__ == '__main__':
	app = MainApp()
	app.MainLoop()
