from random import randint
import webbrowser

N = S = A = ''

while True:
    command = raw_input("Press enter for an acronym\t['O' for options, 'Q' for quit]")
    if command == '':
        N = open('N.txt','r+')
        S = open('S.txt','r+')
        A = open('A.txt','r+')
        NSA = [N,S,A]
        acronym = ''
        
        for letter in NSA:
            words = list(enumerate(letter))
            rand = randint(0,len(words))
            for i, line in words:
                if i == rand:
                    acronym += line.strip() + '  '

        space = (53 - len(acronym)) / 2
        print '53 ' + str(space) + ' ' + str(len(acronym))
        if len(acronym) % 2 != 0: left = right = space
        else:
            left = int(space)
            right = left + 1
        print str(left), str(right)

        print ''
        print '  .-----------------------------------------------------------------.  '
        print ' /  .-.                                                         .-.  \ '
        print '|  /   \                                                       /   \  |'
        print '| |\_.  |'      + ' ' * left + acronym + ' ' * right +       '|    /| |'
        print '|\|  | /|                                                     |\  | |/|'
        print "| `---' |                                                     | `---' |"
        print '|       |-----------------------------------------------------|       |'
        print '\       |                                                     |       /'
        print ' \     /                                                       \     / '
        print "  `---'                                                         `---'  "
        print ''
   
    elif command == 'Q' or command == 'q': break
    
    elif command == 'O' or command == 'o': print "Input\t\t\tResult\n\n'D'\t\t\tFetch the definitions of the words\n'N', 'S', or 'A' \tAdd the corresponding word to the custom dictionary\n'W'\t\t\tAdd a word of your own to the custom dictionary\n'1', '2', or '3'\tSubtract the corresponding word from the dictionary\n'R'\t\t\tRecover the most recently deleted word (you can do this repeatedly)\n\n"

    elif command == 'D' or command == 'd':
        webbrowser.open('http://dictionary.reference.com/browse/' + acronym.split('  ')[0] +'?s=t',new=1)
        webbrowser.open('http://dictionary.reference.com/browse/' + acronym.split('  ')[1] +'?s=t',new=1)
        webbrowser.open('http://dictionary.reference.com/browse/' + acronym.split('  ')[2] +'?s=t',new=1)

    if N:
        N.close()
        S.close()
        A.close()
        


        


### add ability to add word to custom list, give option to pull words only from this list. Have ability to choose generated word or add your own.
### add ability to subtract word from dictionary. Add subtracted word to a trash file so you can recover if necessary (keep words in order so you can recover last deleted word)
### add decorative border to acronym
### add ability to look up word by scraping dictionary.com
