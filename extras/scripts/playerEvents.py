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

import xbmc,xbmcgui
import subprocess,os

audio = playing = lastpos = curpos = length = lastlenght = 0

# grab the home window
HOME = xbmcgui.Window(10000)

class MusicPlayer(xbmc.Player):
	
	def __init__ (self):
		xbmc.Player.__init__(self)
		
	def onPlayBackStarted(self):
		global audio, playing, lastpos, curpos, length
		if (self.isPlayingAudio()):
			audio = 1
			HOME.clearProperty('info')
			if (playing == 0):
				xbmc.executebuiltin('Notification(play,play,4000)')
				playing = 1
			elif (playing == 1):
				curpos = int(xbmc.PlayList(0).getposition())
				length = int(xbmc.PlayList(0).size())				
				if (lastpos == 0 and curpos == length - 1):
					xbmc.executebuiltin('Notification(prev,prev,4000)')
				elif (lastpos == length - 1 and curpos == 0):
					xbmc.executebuiltin('Notification(next,next,4000)')
				elif (curpos < lastpos):
					xbmc.executebuiltin('Notification(prev,prev,4000)')
				elif (lastpos < curpos or lastpos == curpos):
					xbmc.executebuiltin('Notification(next,next,4000)')
			lastpos = int(xbmc.PlayList(0).getposition())
		else:
			audio = 0

	def onPlayBackPaused(self):
		if (self.isPlayingAudio()):
			HOME.clearProperty('info')
			xbmc.executebuiltin('Notification(pause,pause,4000)')

	def onPlayBackResumed(self):
		if (self.isPlayingAudio()):
			HOME.clearProperty('info')
			xbmc.executebuiltin('Notification(play,play,4000)')
            	
	def onPlayBackEnded(self):
		if (audio == 1 and xbmc.PlayList(0).getposition() == xbmc.PlayList(0).size() - 1):
			global playing
			playing = 0
			HOME.clearProperty('info')

	def onPlayBackStopped(self):
		if (audio == 1):
			global playing
			playing = 0
			HOME.clearProperty('info')
		
player = MusicPlayer()

while 1:
	xbmc.sleep(10)