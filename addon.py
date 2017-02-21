import os
import subprocess
import xbmcaddon
import xbmc

__addon__ = xbmcaddon.Addon()
program = __addon__.getSetting('emulationstation_path')
quitkodi = __addon__.getSetting('emulationstation_quitkodi')
noexit = __addon__.getSetting('emulationstation_noexit')
if quitkodi == 'true':    
	if noexit == 'true':
	    os.execv(program, [program, '--no-exit'])
	elif noexit == 'false':
	    os.execlp(program, program)
elif quitkodi == 'false':	    
		subprocess.Popen(program, shell=True)

xbmc.executebuiltin( "XBMC.ActivateWindow(0)" )