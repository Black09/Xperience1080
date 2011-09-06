import xbmc
import xbmcgui

# grab the home window
HOME = xbmcgui.Window(10000)

HOME.setProperty(sys.argv[1],'1')
xbmc.sleep(300)
HOME.clearProperty(sys.argv[1])