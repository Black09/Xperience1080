import xbmc

function = 'Action(%s)' % sys.argv[1]
setFocusTo = 'SetFocus(%s)' % sys.argv[2]
setFocusBackTo = 'SetFocus(%s)' % sys.argv[3]

xbmc.executebuiltin(setFocusTo)
xbmc.executebuiltin(function)
xbmc.executebuiltin(setFocusBackTo)

if (len(sys.argv) > 4):
	xbmc.sleep(100)
	getLabel = 'Control.GetLabel(%s)' % sys.argv[4]
	folderLabel = xbmc.getInfoLabel(getLabel)
	mainFolder = xbmc.getLocalizedString(20108)
	if (folderLabel == mainFolder):
		xbmc.executebuiltin(setFocusTo)



