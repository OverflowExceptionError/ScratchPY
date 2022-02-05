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
a = requests.get("http://memed64.000webhostapp.com/scratchpy/users/" + filename[0] + "/projects/" + filename[1])
class fopen:
    def read(self, takeback):
        return takeback
program = fopen()
imagedata = program.read(a.text).split("image: ")
datafile = imagedata[0].split("data: ")[1]
b = requests.get("https://memed64.000webhostapp.com/scratchpy/users/" + filename[0] + "/projects/default.spyd", stream=True)
handle = open("C:/ScratchPY/" + datafile, "wb")
for chunk in b.iter_content(chunk_size=512):
    if chunk:  # filter out keep-alive new chunks
        handle.write(chunk)
handle.close()
from zipfile import ZipFile
with ZipFile("C:/ScratchPY/" + datafile, 'r') as zipObj:
    zipObj.extractall('C:/ScratchPY/GS')
window = pygame.display.set_mode((640,480))
pygame.display.set_caption("ScratchPY Desktop Client - Playing " + filename[1])
import GS as playgame
while True:
    if playgame.allowed == None:
        window.fill((255,255,255))
    else:
        pass
    if filename[1] == "program.spy" and filename[0] == "TestUser":
        playgame.project(playgame.tiledraw,playgame.prevdraw,playgame.Sprite1[0],playgame.Sprite1[1])
    else:
        playgame.project()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.update()