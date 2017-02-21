import os
import xbmcaddon

__addon__ = xbmcaddon.Addon()
program = __addon__.getSetting('emulationstation_path')
noexit = __addon__.getSetting('emulationstation_noexit')
if noexit == 'true':
    os.execv(program, [program, '--no-exit'])
elif noexit == 'false':
    os.execlp(program, program)

