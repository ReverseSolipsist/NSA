from random import randint
import webbrowser

explodingmessage = open('data/explodingmessage.txt','r')
print explodingmessage.read()
explodingmessage.close()
explodingmessage = open('data/explodingmessage.txt','w')
explodingmessage.close()
    
N = S = A = ''
letters = ['a','A','v','V','j','J','n','N',]
acronym = ''
default = True
custom = False

while True:
    command = raw_input("Press enter for an acronym\t['O' for options, 'Q' for quit]")

    if len(command) == 3:
        if command[0] in letters and command[1] in letters and command[2] in letters:
            if custom == True:
                Nfile = 'data/N' + command[0] + '.txt'
                Sfile = 'data/S' + command[1] + '.txt'
                Afile = 'data/A' + command[2] + '.txt'
            else:
                Nfile = 'data/Nc' + command[0] + '.txt'
                Sfile = 'data/Sc' + command[1] + '.txt'
                Afile = 'data/Ac' + command[2] + '.txt'
            default = False
            command = ''
            print ''
        elif command == 'res': default = True
        else: print 'Not a command. Try a 3-letter combination of a, j, n, and v. For example: avn'
    
    if command == '':
        if default == True:
##            Nfile = 'data/N' + letters[randint(0,7)].lower() + '.txt'
##            Sfile = 'data/S' + letters[randint(0,7)].lower() + '.txt'
##            Afile = 'data/An.txt'
            if custom == True:
                print custom
                Nfile = 'data/Nc' + letters[randint(0,3)].lower() + '.txt'
                middle = letters[randint(4,7)].lower()
                Afile = 'data/Ac' + middle + '.txt'
                if middle == 'n' or middle == 'N': Sfile = 'data/Sc' + letters[randint(0,5)].lower() + '.txt'
                else: Sfile = 'data/Sc' + letters[randint(0,3)].lower() + '.txt'
            else:
                Nfile = 'data/N' + letters[randint(0,3)].lower() + '.txt'
                middle = letters[randint(4,7)].lower()
                Afile = 'data/A' + middle + '.txt'
                if middle == 'n' or middle == 'N': Sfile = 'data/S' + letters[randint(0,5)].lower() + '.txt'
                else: Sfile = 'data/S' + letters[randint(0,3)].lower() + '.txt'
        
        N = open(Nfile,'r+')
        S = open(Sfile,'r+')   
        A = open(Afile,'r+')
        NSA = [N,S,A]
        acronym = ''
        
        for letter in NSA:
            words = list(enumerate(letter))
            rand = randint(0,len(words))
            for i, line in words:
                if i == rand:
                    acronym += line.strip() + '  '

        space = (53 - len(acronym)) / 2
        if len(acronym) % 2 != 0: left = right = space

        else:
            left = int(space)
            right = left + 1

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
    
    elif command == 'O' or command == 'o': print "Input\t\t\tResult\n\n'D'\t\t\tFetch the definitions of the words\n'N', 'S', or 'A' \tAdd the corresponding word to the custom dictionary\n'W'\t\t\tAdd a word of your own to the custom dictionary\n'1', '2', or '3'\tSubtract the corresponding word from the dictionary\n'R'\t\t\tRecover the most recently deleted word (you can do this repeatedly)\n\n'C'\t\t\tSwitch to or from custom dictionary\n\n"

    elif command == 'C' or command == 'c':
        print custom
        if custom == False: custom = True
        else: custom = False

    elif command == 'D' or command == 'd':
        if acronym:
            webbrowser.open('http://dictionary.reference.com/browse/' + acronym.split('  ')[0] +'?s=t',new=1)
            webbrowser.open('http://dictionary.reference.com/browse/' + acronym.split('  ')[1] +'?s=t',new=1)
            webbrowser.open('http://dictionary.reference.com/browse/' + acronym.split('  ')[2] +'?s=t',new=1)
        else: webbrowser.open('http://www.leekspin.com/')
        print ''

    elif command == 'N' or command == 'n':  
        custom = open('data/Nc' + Nfile[6] + '.txt','a')
        custom.write(acronym[:acronym.find(' ')] + '\n')
        custom.close()
        print Nfile, Nfile[6]
    elif command == 'S' or command == 's':
        custom = open('data/Sc' + Nfile[6] + '.txt','a')
        custom.write(acronym[acronym.find(' ')+1:acronym.rfind(' ')] + '\n')
        custom.close()
    elif command == 'A' or command == 'a':
        custom = open('data/Ac' + Nfile[6] + '.txt','a')
        custom.write(acronym[acronym.rfind(' ')+1:] + '\n')
        custom.close()
        
        

    

#    elif command == 'T' or command 

    if N:
        N.close()
        S.close()
        A.close()
        


        


### add ability to add word to custom list, give option to pull words only from this list. Have ability to choose generated word or add your own.
### add ability to subtract word from dictionary. Add subtracted word to a trash file so you can recover if necessary (keep words in order so you can recover last deleted word)
### add decorative border to acronym
### add ability to look up word by scraping dictionary.com
