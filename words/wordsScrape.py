import urllib
import re

chars = ['N','S','A']

for char in chars:
    inf = char + '.txt'
    f = open(inf,'a')

    # Retrieve source
    url = 'http://www.crosswordsolver.org/' + char + '-words'
    words = urllib.urlopen(url).read()

    # Find word list
    start = words.find("<div class='container body'>")
    end = words.find("""<div class='mpu-ad' id="mpu-ad-1"></div>""",start)

    # Filter everything from the source but the word list and arrange it into a column
    words = words[start:end]            #Eliminates all text except the block that includes the words
    words = re.sub(r'<.*?>',' ',words)  #Replaces all text between brackets and the brackets themselves with a single space
    words = re.sub(r'  +','\n',words)   #Replaces all whitespace longer than one character with a newline character

    # Eliminate the intro
    words = words[words.find(char,words.find(char,words.find(char)+1)+1):]

    f.write(words)
    f.close()
