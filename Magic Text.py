#!/usr/bin/env python3
# Program that condences text
#
# Copywrite Cat Inc, All rights reserved.
# Programmed by Samuel Davenport, member of Cat Inc.
#
# DISCLAIMER:
# Additinal programs used in this program
# may contain code or code based off other code
# not owned by Cat Inc.

PREBOOTERR = 'NULL'
try:
    tmp = 1
    import os, subprocess, time
    tmp = 2
    from colorama import Fore
    tmp = 3
    import maths
except ImportError:
    if not tmp == 3:
        PREBOOTERR = 'A module failed to import'
    else:
        PREBOOTERR = 'Maths module failed to import'

DEV = False
STOPERRCATCHING = False
NAME = 'Magic Text'
__version__ = '0.0.4'
MUST = (str(NAME+'.py'), 'maths.py')
pyinstallered = True
ISTERM = False
global lookup
global dictmod
global dictinfo

def printz(s='', sep=' ', end='\n', file='default', flush=False):
    global ISTERM
    if file == 'default':
        file = os.sys.stdout
    if ISTERM:
        if file == os.sys.stderr:
            s = Fore.RED+str(s)+Fore.RESET
        termRun('echo '+str(s))
    elif str(s).isprintable():
        if file == 'default':
            file = os.sys.stdout
        print(s, sep=sep, end=end, file=file, flush=flush)

class file:
    # File Loading
    def loadict(sel):
        global lookup
        global dictmod
        global dictinfo
        tmp = False
        try:
            with open(str(sel), mode='r', encoding='utf-8') as loadfile:
                lookup = []
                for line in loadfile:
                    lookup.append(str(line))
        except IOError:
            lookup = ["['"+str(int(time.time()))+"', '0']", 'cat']
            tmp = True
        dictmod = 'str'
        dictinfo = maths.strlist(lookup[0])
        del lookup[0]
        if tmp:
            file.svdict(sel)
    
    def svdict(name):
        global lookup
        global dictinfo
        global dictmod
        if dictmod == 'str':
            with open(str(name), mode='w', encoding='utf-8') as savefile:
                dictinfo[1] = str(int(dictinfo[1])+1)
                if len(dictinfo) == 2:
                    dictinfo.append('')
                dictinfo[2] = str(int(time.time()))
                savefile.write(str(dictinfo) + '\n')
                for word in lookup:
                    savefile.write(str(word)+'\n')
                savefile.close()
    pass

class MagicText:
    def chmod(read, mode):
        data = read
        tmp = []
        for i in range(26):
            tmp.append(chr(i + 65).lower())
        tmp.append("'")
        read = tuple(tmp)
        tmpdata = []
        if str(mode) == 'num':
            for word in data:
                wordtmp = []
                for letter in word:
                    lettertmp = str(read.index(letter))
                    if len(lettertmp) == 1:
                        lettertmp = str('0' + lettertmp)
                    wordtmp.append(lettertmp)
                wordtmp = str(''.join(wordtmp))
                tmpdata.append(str(wordtmp))
            data = tuple(tmpdata)
        if str(mode) == 'str':
            for numword in data:
                word = []
                count = 0
                past = ''
                for num in numword:
                    if not bool(count):
                        count = 1
                        past = str(num)
                    else:
                        count = 0
                        letter = read[int(str(past) + str(num))]
                        word.append(letter)
                word = str(''.join(word))
                tmpdata.append(word)
            data = tuple(tmpdata)
        return tuple(data)

    def getinput(question, example):
        printz()
        printz(str(question))
        out = input('')
        printz()
        if str(type(out)) == str(type(example)):
            toret = out
        elif str(type(int(out))) == str(type(example)):
            toret = str(out)
        else:
            printz('Please Try Again')
            toret = MagicText.getinput(question, example)
        return toret
    
    def setup(mode):
        global lookup
        global dictmod
        tmp = []
        #Fix wordz
        for word in lookup:
            tmp.append(word.rstrip())
        lookup = tuple(tmp)
        #Convert to num-mode if in selected modes
        if mode in (1, 3):
            if dictmod != 'num':
                lookup = tuple(MagicText.chmod(lookup, 'num'))
                dictmod = 'num'
        #Convert to str-mode if in selected modes
        if mode in (2, 3, 4):
            if dictmod != 'str':
                lookup = MagicText.chmod(lookup, 'str')
                dictmod = 'str'
    
    def nlconv(inp, mode):
        #Number Letter Convert
        rng = []
        for i in range(90):
            rng.append(i+10)
        if not bool(mode):
            num = int(inp)
            if num in rng[0:26]:
                toret = str('1'+chr(num+55))
            elif num in rng[26:52]:
                toret = str('2'+chr(num+29))
            elif num in rng[52:78]:
                toret = str('3'+chr(num+3))
            elif num in rng[78:90]:
                toret = str('4'+chr(num-23))
            else:
                toret = str(num)
        else:
            tmp = list(str(inp))
            if int(tmp[0]) == 1:
                toret = int(ord(tmp[1])-55)
            elif int(tmp[0]) == 2:
                toret = int(ord(tmp[1])-29)
            elif int(tmp[0]) == 3:
                toret = int(ord(tmp[1])-3)
            elif int(tmp[0]) == 4:
                toret = int(ord(tmp[1])+23)
            else:
                toret = 1
        return toret
    
    def magicify(txt):
        global lookup
        problems = (' ')
        #seperate sentence into individual words
        words = maths.seperate(str(txt))
        tmp = []
        for i in range(len(words)):
            if words[i] in problems or words[i].isdigit() or words[i].isdecimal():
                cats = 'best'
            else:
                tmp.append(words[i])
        words = tmp
        #make the words plain-text
        for i in range(len(words)):
            words[i] = str(maths.mkplain(words[i]))
        #make the words list into a num-string list
        words = list(MagicText.chmod(tuple(words), 'num'))
        #make num-words into true ints
        for i in range(len(words)):
            words[i] = int(words[i])
        #make a minni lookup with true ints
        minilookup = []
        for i in lookup:
            minilookup.append(int(i))
        #find what the word's position in the dictionary is and +1 add to pos
        pos = []
        for word in words:
            if word in minilookup:
                pos.append(int(minilookup.index(word) + 1))
        #make pos values hex
        tmp = []
        for i in pos:
            dtmp = list(hex(int(i)))
            del dtmp[0:2]
            tmp.append(str(''.join(dtmp)))
        pos = tmp
        tmp = []
        #make hex pos condenced useing nlconv
        for number in pos:
            if str(number).isdigit():
                #if it's a digit, do magic to the digits
                leng = len(list(str(int(number))))
                if leng == 1:
                    tmp.append(str(number))
                elif leng == 2:
                    tmp.append(str(MagicText.nlconv(number, 0)))
                elif leng == 3:
                    dtmp = list(str(number))
                    dtmpi = MagicText.nlconv(int(''.join(dtmp[0:2])), 0)
                    tmp.append(str(dtmpi+dtmp[2]))
                elif leng == 4:
                    dtmp = list(str(number))
                    dtmpi = MagicText.nlconv(int(''.join(dtmp[0:2])), 0)
                    dtmpii = MagicText.nlconv(int(''.join(dtmp[2:4])), 0)
                    tmp.append(str(dtmpi+dtmpii))
                else:
                    tmp.append(str(number))
            else:
                #if it's hex, leave it alone
                tmp.append(str(number))
        data = list(str(maths.seplist(tmp, ' ')))
        del data[len(data)-1]
        data = str(''.join(data))
        return data
    
    def unmagicify(txt):
        global lookup
        #make lookups for other parts of the program
        problems = (' ')
        letters = []
        for i in range(26):
            letters.append(chr(i+65))
        letters = tuple(letters) #letters = A - Z
        #seperate sentence into individual words
        data = maths.seperate(str(txt))
        tmp = []
        for i in range(len(data)):
            if not data[i] in problems:
                tmp.append(data[i])
        data = tuple(tmp)
        #decode hex pos values
        read = []
        for part in data:
            tmp = list(part)
            if str(part).isdigit() and len(tmp) == 1:#if it's a 1 digit hex pos
                read.append(str(part))
            elif str(part).islower():#if it's just true hex
                read.append(str(part))
            elif str(tmp[0]).isdigit() and str(tmp[1]) in letters: #if it's a nlconv thing
                if len(tmp) == 2:#if it's just a regular one
                    read.append(str(MagicText.nlconv(str(part), 1)))
                elif len(tmp) == 3:#if it's a len3 one
                    read.append(str(MagicText.nlconv(str(part), 1))+str(tmp[2]))
                elif len(tmp) == 4:#if it's a double one
                    dtmp = str(MagicText.nlconv(''.join(tmp[0:2], 1)))
                    read.append(dtmp+str(MagicText.nlconv(''.join(tmp[2:4], 1))))
        data = read
        #make data back into true hex
        for i in range(len(data)):
            data[i] = str('0x'+data[i])
        #make hex back into readable pos
        pos = []
        for hexz in data:
            pos.append(int(hexz, base=16) - 1)
        #make words based on pos - 1
        words = []
        for read in pos:
            try:
                words.append(lookup[read])
            except IndexError:
                words.append('InvalidWord')
        #formatting
        sentance = list(str(maths.seplist(words, ' ')).title())
        del sentance[len(sentance)-1]
        sentance = str(''.join(sentance))
        return str(sentance)
        
    def addtodict(dictname):
        global lookup
        problems = (' ')
        printz('Press Return with no other charecters to stop!')
        while True:
            try:
                printz()
                dainput = input('Input : ')
            except KeyboardInterrupt:
                break
            if dainput.rstrip() == '':
                break
            dainput = list(maths.seperate(str(dainput)))
            data = []
            for i in range(len(dainput)):
                data.append(str(maths.mkplain(dainput[i])))
            printz()
            for word in data:
                if not str(word) in lookup and not word in problems and not len(lookup) > 9998:
                    lookup = list(lookup)
                    lookup.append(word)
                    lookup = tuple(lookup)
                    printz('Added Word "'+word.title()+'"')
                elif len(lookup) > 9998:
                    printz('ERR: Cannot have more than 9999 words in each dictionary', file=os.sys.stderr)
            printz()
            time.sleep(0.1)
        printz()
        printz('Saving...')
        file.svdict(dictname)
        time.sleep(2)
    
    def mergedicts(one, two):
        global lookup
        problems = (' ')
        MagicText.setup(5)
        dicti = lookup
        file.loadict(two)
        MagicText.setup(5)
        dictii = lookup
        newdict = []
        for word in dicti:
            tmp = str(maths.mkplain(word))
            if not tmp in newdict and not tmp in problems:
                if not len(newdict) > 9998:
                    newdict.append(tmp)
                else:
                    break
        for word in dictii:
            tmp = str(maths.mkplain(word))
            if not tmp in newdict and not tmp in problems:
                if not len(newdict) > 9998:
                    newdict.append(tmp)
                else:
                    break
        if len(newdict) > 9998:
            printz('ERR: Cannot have more than 9999 words in each dictionary', file=os.sys.stderr)
        lookup = tuple(newdict)
    
    def main():
        global lookup
        global dictmod
        printz('Please select a dictionary file, or enter the name of a new one.')
        printz('(Program does not handle non-txt files)')
        printz()
        dirconts = list(os.listdir(os.getcwd()))
        tmp = []
        for filename in dirconts:
            if '.txt' in filename:
                tmp.append(filename)
        dicts = tmp
        if len(dicts) > 0:
            printz('Pre-Existing Dictionaries:')
            dicts = list(str(''.join(tmp)).split(sep='.txt'))
            del dicts[len(dicts)-1]
            for i in range(len(dicts)):
                printz(str(i+1)+'. '+dicts[i].title())
            printz()
            dictname = str(input('Dictionary Number or New Dictionary Filename : '))
        else:
            dictname = str(input('New Dictionary Filename (no extention) : '))
        dictmod = 'str'
        if dictname.isdigit() and len(dicts) > 0:
            dictname = dicts[int(dictname)-1]
        dictname = dictname+'.txt'
        if dictname in dirconts:
            new = ' '
        else:
            new = ' New '
        printz()
        printz('Selected'+new+'Dictionary "'+dictname.title()+'"')
        file.loadict(dictname)
        time.sleep(2)
        while True:
            printz()
            while True:
                clearterm()
                printz('Please Select An Option:')
                printz('1. Magicification')
                printz('2. Un-Magicification')
                printz('3. Add to Selected Dictionary')
                printz('4. Sort Selected Dictionary')
                printz('5. Merge Selected Dictionary and Another Together')
                printz('6. Stats of Currently Selected Dictionary')
                printz('7. Credits')
                printz('8. Quit')
                printz()
                mode = input('Option : ')
                printz()
                if mode.isdigit():
                    if int(mode) in (1, 2, 3, 4, 5, 6, 7, 8):
                        break
                    else:
                        printz()
                        clearterm()
                        printz('Please Try Again.', file=os.sys.stderr)
                        cats = input('Press Return to continue ')
            clearterm()
            mode = int(mode)
            MagicText.setup(mode)
            printz()
            clearterm()
            if not mode-2 > 0: # modes 1 and 2
                printz()
                tmp = 'magicification'
                if bool(mode-1):#mode is 2
                    tmp = str('un-' + tmp)
                dainput = input('Input for %s : ' % tmp)
                printz()
                if not dainput.rstrip() == '':
                    if not bool(mode-1): #if mode is 1
                        output = MagicText.magicify(dainput)
                        MagicText.setup(2)
                        redo = MagicText.unmagicify(str(output))
                    else:#mode is 2
                        output = MagicText.unmagicify(dainput)
                    if not bool(mode-1) and redo.title() != dainput.title(): #if mode is 1
                        printz('WARNING: Some words you used do not exist in the dictionary.', file=os.sys.stderr)
                        for word in maths.seperate(dainput.title()):
                            if not word in maths.seperate(redo.title()):
                                print(word+' Not in Selected Dictionary')
                        printz('Sentence Without Missing Words: %s' % redo)
                        printz()
                    printz('Input was : %s' % dainput)
                    printz('Output is : %s' % output)
                else:
                    printz('ERR: No text to Magicify!', file=os.sys.stderr)
                printz()
                cats = input('Press Return to continue ')
            elif not mode-4 > 0: #modes 3 and 4
                if not bool(mode-3):#mode 3
                    MagicText.addtodict(dictname)
                else:#mode 4
                    printz('Pre-Sort:')
                    printz(maths.seplist(lookup, ', ').title())
                    lookup = list(lookup)
                    lookup.sort()
                    lookup = tuple(lookup)
                    printz()
                    printz('Post-Sort:')
                    printz(maths.seplist(lookup, ', ').title())
                    file.svdict(dictname)
                    printz()
                    cats = input('Press Return to continue ')
            elif not mode-6 > 0: #modes 5 and 6
                if not bool(mode-5):#mode 5
                    dirconts = list(os.listdir(os.getcwd()))
                    tmp = []
                    for filename in dirconts:
                        if '.txt' in filename:
                            tmp.append(filename)
                    dicts = list(str(''.join(tmp)).split(sep='.txt'))
                    del dicts[len(dicts)-1]
                    if not len(dicts) == 1:
                        printz('Pre-Existing Dictionaries:')
                        for i in range(len(dicts)):
                            printz(str(i+1)+'. '+dicts[i].title())
                        printz()
                        while True:
                            try:
                                two = int(input('2nd Dictionary Number : '))
                            except ValueError:
                                printz('Please Try Again.', file=os.sys.stderr)
                                cats = input('Press Return to continue ')
                            else:
                                break
                        two = dicts[int(two)-1]+'.txt'
                        MagicText.mergedicts(dictname, two)
                        name = str(input('New Dictionary Name : '))+'.txt'
                        printz()
                        printz('Added '+str(len(lookup))+' Words to New Dictionary!')
                        printz()
                        ptintz('Done!')
                        file.svdict(name)
                        printz()
                        cats = input('Press Return to continue ')
                    else:
                        printz('ERR: You Cannot Combine Two Dictionaries if Only One Dictionary Exists', file=os.sys.stderr)
                        cats = input('Press Return to continue ')
                else:#mode 6
                    printz('Stats of Currently Selected Dictionary:')
                    printz('Total Words'+" "*6+': '+str(len(lookup)))
                    printz('Space Avalable'+" "*3+': '+str(int(9999-len(lookup))))
                    printz('Space Used'+" "*7+': '+str(len(lookup))+' / 9999')
                    printz('Usage Percentage : '+str(round(maths.findpercent(len(lookup), 9999)))+'%')
                    printz()
                    cats = input('Press Return to continue ')
            elif not mode-8 > 0: #modes 7 and 8
                if not bool(mode-7):#mode 7
                    printz('This is the '+NAME+' Program, v'+__version__)
                    printz('')
                    printz('Copywrite (c) Cat Inc.')
                    printz('All Rights Reserved.')
                    printz()
                    printz('Programmed by Samuel Davenport, member of Cat Inc.')
                    printz()
                    printz('Credit to Anthony Williams for researching an idea')
                    printz('for the sorting algorythm.')
                    printz()
                    printz('Visit github.com/cat-ink for more projects by Cat Inc.')
                    printz()
                    printz('Source Code at https://github.com/CoolCat467/Magic-Text/')
                    printz()
                    cats = input('Press Return to continue ')
                else:#mode 8
                    printz('Thank you for using the '+NAME+' Program v'+__version__+'!')
                    time.sleep(2)
                    break
            else:
                printz('Thank you for using the '+NAME+' Program v'+__version__+'!')
                time.sleep(2)
                break
        printz()

def importRequired():
    tmp = MUST
    tmp = list(str(''.join(tmp)).split(sep='.py'))
    del tmp[len(tmp)-1]
    for i in range(len(tmp)-1):
        if tmp[i] == NAME:
            del tmp[i]
    modules = tmp
    for module in modules:
        try:
            exec('import %s' % module)
        except ImportError:
            raise ImportError('Required module '+module+' Failed to import.')

def startup():
    # Set some globals
    global SYSNAME
    global NODENAME
    global CURFOLD
    SYSNAME = str(os.uname()[0])
    NODENAME = str(os.uname()[1])
    os.chdir(os.path.split(os.sys.argv[0])[0])
    CURFOLD = str(os.path.split(os.getcwd())[1])
    pythontype = os.sys.executable.split(sep='/')[3]
    ##Find Errors:
    error = ''
    # Find out if we are in our own folder
    if CURFOLD != NAME:
        os.chdir(os.path.split(os.sys.argv[0])[0])
        if not pyinstallered:
            # If it's not, fix it.
            src = os.sys.argv[0]
            os.chdir(os.path.split(os.getcwd())[0])
            os.mkdir(NAME)
            dst = os.path.split(os.getcwd())[0] +'/'+NAME+'/'+NAME+'.py'
            subprocess.call(str('cp %s %s' % (src, dst)))
            os.chdir(os.path.split(dst)[0])
            os.remove(src)
            error = '''Program was not in it's own folder, but repaired.
            Please put any additinal files the program came with in the
            new file and restart the program.'''
    if str(error) == '' and not pyinstallered:
        # Make sure we have everything
        contents = os.listdir(os.getcwd())
        lostmodules = []
        for i in MUST:
            if not i in contents:
                lostmodules.append(i)
                lostmodules.append(',\n')
        if len(lostmodules) > 0:
            lostmodules = list(str(''.join(lostmodules)).split(sep='.py'))
            lostmodules = str(''.join(lostmodules)).splitlines()
            for i in range(len(lostmodules)):
                lostmodules.append(lostmodules[0])
                lostmodules.append(' ')
                del lostmodules[0]
            lostmodules = list(''.join(list(lostmodules)[0:int(len(list(lostmodules))-1)]))
            lostmodules = str(''.join(lostmodules[0:int(len(lostmodules)-1)]))
            error = str('Some required module files were not found: '+lostmodules)
    if str(error) != '':
        return str('ERR: '+error)
    else:
        return error

def main():
    # Greet user
    printz('Welcome to the '+NAME+' Program v'+__version__+'!')
    printz('Copywrite (c) Cat Inc.\nAll rights reserved.')
    printz()
    time.sleep(5)
    errors = startup()
    if errors == '':
        if SYSNAME != 'Linux':
            printz('WARNING: Operating System is not Linux.', file=os.sys.stderr)
            printz('Some features may not work and/or cause errors')
            printz('If you would like an official port of this')
            printz('program for your operating system, please')
            printz('contact CoolCat467 on github.com/coolcat467')
            printz()
            printz('Proceed with Caution!')
        importRequired()
        MagicText.main()
    else:
        printz(errors, file=os.sys.stderr)

def detectTerm():
    screen = bool(os.sys.stdout.isatty())
    #tmp = termRun('ps -AF')
    #for i in tmp:
    #    tmpi = tmp[i].rstrip().split()
    #    if len(tmpi) == 9:
    #        if tmpi[0]+' '+tmpi[2]+' '+tmpi[7]+' '+tmpi[8] == '/usr/sbin/cron -f':
    #            cronpid = tmpi[1]
    #        elif NAME in tmpi:
    #            progpid = tmpi[1]
    #iscron = progpid == cronpid
    idle = bool('idlelib' in os.sys.modules)
    return not idle

def termRun(run, out=0):
    if bool(out):
        program = subprocess.Popen(run.split(), stdout=subprocess.PIPE)
        output = program.communicate()
        data = str(output[0].splitlines())
        data = tuple(maths.strlist(str(data)))
    else:
        program = subprocess.Popen(run.split())
        data = ''
    return data

def clearterm():
    if ISTERM:
        termRun('clear')

def terminate():
    printz('Quiting...')
    os.abort()
    exit()

def nuke(supersecretpassword):
    if supersecretpassword == 'Just Do It!!':
        subprocess.call(str('rm -r %s' % CURFOLD))
    terminate()

# Activation Program
if __name__ == '__main__':
    startTime = time.time()
    ISTERM = detectTerm()
    clearterm()
    if DEV:
        printz('DEV Mode = '+str(DEV))
        printz('ErrorCatchingEnabled = '+str(not STOPERRCATCHING))
        printz('RunningFromTerm = '+str(ISTERM))
        printz()
    printz('Copywrite (c) Cat Inc.')
    printz('All Rights Reserved.')
    printz()
    printz('Programmed by Samuel Davenport, member of Cat Inc.')
    #for when this may happen:
    #printz('Programmed by Anthony Williams, based on a template')
    #printz('made by Samuel Davenport, both members of Cat Inc')
    printz()
    if not DEV:
        STOPERRCATCHING = False
    if not STOPERRCATCHING:
        try:
            if PREBOOTERR != 'NULL':
                if not PREBOOTERR.split()[0].lower() == 'maths':
                    raise ImportError(PREBOOTERR)
            main()
        except Exception as e:#Catch errors and make them not scary for end users
            printz()
            printz('An error has occored', file=os.sys.stderr)
            error = str(e)
            if error.isprintable():
                errormessage = str('ERR: %s' % error)
                printz(errormessage, file=os.sys.stderr)
            printz()
            if str(os.uname()[0]) != 'Linux':
                printz('I told you there might be errors!')
                printz()
        except KeyboardInterrupt:
            printz()
            printz('ERR: KeyboardInterrupt', file=os.sys.stderr)
        except SystemExit:
            printz()
            printz('ERR: SystemExit', file=os.sys.stderr)
    else:
        main()
else:
    printz('Bad.')
if not DEV:
    terminate()
