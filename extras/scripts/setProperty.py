import xbmcgui

# grab the home window
HOME = xbmcgui.Window(10000)

if (len(sys.argv) > 2):
	HOME.setProperty(sys.argv[1],sys.argv[2])
elif (len(sys.argv) <= 2):
	HOME.clearProperty(sys.argv[1])