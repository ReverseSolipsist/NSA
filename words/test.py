###inf = '~/Desktop/' + char + '.txt'
##inf = 'c:/Users/Michael/Desktop/' + 'N' + '.txt'
##f = open(inf,'a')
##f.write('12')
##f.close()

import urllib
import re

#chars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#chars = ['A']
chars = ['N','S','A']

for char in chars:
    inf = 'c:/Users/Michael/Desktop/' + char + '.txt'
    f = open(inf,'a')

    url = 'http://www.crosswordsolver.org/' + char + '-words'
    words = urllib.urlopen(url).read()

    start = words.find("<div class='container body'>")
    end = words.find("""<div class='mpu-ad' id="mpu-ad-1"></div>""",start)

    words = words[start:end]
    words = re.sub(r'<.*?>',' ',words)
    words = re.sub(r'  +','\n',words)

    words = words[words.find(char,words.find(char,words.find(char)+1)+1):]

    f.write(words)
    f.close()
