# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with XBMC; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# *  Created by `Black

import sys
import xbmc
import xbmcgui
try:
    from sqlite3 import dbapi2 as sqlite
except:
    from pysqlite2 import dbapi2 as sqlite

class Main:
	# grab the home window
	WINDOW = xbmcgui.Window(10000)
	PLAYERCONTROLS = xbmcgui.Window(10114)
	
	def __init__(self):
		init = int(sys.argv[1])
		if (init == 0):
			self.initProperties()
		elif (init == 1):
			self.updateViewModes()
		else:
			self.WINDOW.setProperty('NextStage','2')
			self.PLAYERCONTROLS.setProperty('NextStage','2')
	
	def updateViewModes(self):
		currentWindowId = int(xbmcgui.getCurrentWindowId())
		currentWindow = xbmcgui.Window(currentWindowId)
		currentFocusId = int(currentWindow.getFocusId())
		if (currentFocusId == 50 or currentFocusId == 55 or currentFocusId == 56 or currentFocusId == 60):
			folderPath = xbmc.getInfoLabel('Container.FolderPath')
			id = '%d-%s' % (currentWindowId, folderPath)
			# Connect to database
			database = sqlite.connect('%s/viewmodes.db' % sys.path[0])
			cursor = database.cursor()
			try:
				cursor.execute('insert into view (id,window,path,visibility) values (?, ?, ?, ?)', (id, currentWindowId, folderPath, 0))
			except sqlite.IntegrityError, m:
				cursor.execute('''update view SET visibility = 0 where id = "PreviousStage"''')
				cursor.execute('update view SET visibility = 0 where id = ?', (id,))
			database.commit()
			cursor.close()
			self.WINDOW.setProperty(id,'0')
			self.WINDOW.setProperty('PreviousStage','0')
			self.WINDOW.setProperty('NextStage','2')
			self.PLAYERCONTROLS.setProperty('NextStage','2')
		elif (currentFocusId == 52 or currentFocusId == 54):
			folderPath = xbmc.getInfoLabel('Container.FolderPath')
			id = '%d-%s' % (currentWindowId, folderPath)
			# Connect to database
			database = sqlite.connect('%s/viewmodes.db' % sys.path[0])
			cursor = database.cursor()
			try:
				cursor.execute('insert into view (id,window,path,visibility) values (?, ?, ?, ?)', (id, currentWindowId, folderPath, 1))
			except sqlite.IntegrityError, m:
				cursor.execute('''update view SET visibility = 1 where id = "PreviousStage"''')
				cursor.execute('update view SET visibility = 1 where id = ?', (id,))
			database.commit()
			cursor.close()
			self.WINDOW.setProperty(id,'1')
			self.WINDOW.setProperty('PreviousStage','1')
			self.WINDOW.setProperty('NextStage','2')
			self.PLAYERCONTROLS.setProperty('NextStage','2')
	
	def initProperties(self):
		# Connect to database
		database = sqlite.connect('%s/viewmodes.db' % sys.path[0])
		cursor = database.cursor()
		cursor.execute('select * from view')
		for row in cursor:  
			self.WINDOW.setProperty("%s" % row[0], '%d' % row[3])	
		cursor.close()
		self.WINDOW.setProperty('NextStage','2')
		self.PLAYERCONTROLS.setProperty('NextStage','2')
	
if ( __name__ == "__main__" ):
    Main()

