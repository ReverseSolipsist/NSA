import urllib
import re

char = 'A'

inf = 'c:/Users/mnadolsky/Desktop/' + char + '.txt'
f = open(inf,'w')

url = 'http://www.crosswordsolver.org/' + char + '-words'
words = urllib.urlopen(url).read()

start = words.find("<div class='container body'>")
print start
end = words.find("""<div class='mpu-ad' id="mpu-ad-1"></div>""",start)
print end

words = words[start:end]
words = re.sub(r'<.*?>',' ',words)
words = re.sub(r'  +','\n',words)

f.write(words)
f.close()
