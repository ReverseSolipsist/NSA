NSA = ['N','S','A']

for letter in NSA:
    inf = open(letter + 'ps.txt','r')
    noun = open(letter + 'n.txt','w')
    verb = open(letter + 'v.txt','w')
    adj = open(letter + 'j.txt','w')
    adv = open(letter + 'a.txt','w')
    error = open(letter + 'error.txt','w')

    while True:
        line = inf.readline().strip()
        if line == '': break
        print line
        pos = line[:line.find(' ')]
        word = line[line.find(' ')+1:]

        if pos == 'noun': noun.write(word + '\n')
        elif pos == 'verb': verb.write(word + '\n')
        elif pos == 'adjective': adj.write(word + '\n')
        elif pos == 'adverb': adv.write(word + '\n')
        else: error.write(word + '\n')

    inf.close()
    noun.close()
    verb.close()
    adj.close()
    adv.close()
    error.close()
        
