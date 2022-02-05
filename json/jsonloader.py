# ScratchPY Online loader
import os
try:
    import pygame
except ImportError:
    os.system("pip install pygame")
    import pygame
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
filename = None
import optparse
parser = optparse.OptionParser()
parser.add_option("-p", "--Program", dest="filename")
(options, args) = parser.parse_args()
filename = options.filename.split("scratchpy://")
filename = filename[1].split("/")
a = requests.get('http://overflowexceptionerror.github.io/Website/scratchpy/users/' + filename[0] + '/projects/' + filename[1] + '.json'
f = open('code.json','w')
f.write(a.text)
f.close()
os.chdir('C:/ScratchPY')
os.system(r'py C:\ScratchPY\client.py')