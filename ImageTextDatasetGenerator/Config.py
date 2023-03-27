import os

width = 1381
height = 900
fontSize = 20
fontPath = 'fonts/arial/arial.ttf'
imageDir = 'data/images/'
textDir = 'data/text/'
imageExt = '.png'
maxAllowedSentenceLen = 170
datasetItemsCount = 100

if not os.path.exists(imageDir):
    os.makedirs(imageDir)
if not os.path.exists(textDir):
    os.makedirs(textDir)