import pyautogui as pg
import re
import os
import pyperclip
import time
import unidecode
import clipboard
from datetime import date

'''
Convention of TODO files:

maingenre:                  
    subfolder/genre:        (1 tab) 
        subgenre            (2 tabs) 
        subgenre
        subfolder/genre:    
            subgenre        (3 tabs)
            subgenre
            subgenre General
        subgenre 
        subgenre General
    
    maingenre General

note: -General marks the end of a subfolder, 
      -genre path (gen) cannot have \\ in genre names
      -All gen names must be completely accurate (include the word Music)
      -To start from the beginning, enter the main genre for gen and sub and
            enter 0 for line 3.
    
before starting, open two chrome tabs and snap to right side.
    otherwise
    THIS DOESN'T WORK
'''


def nextl(file):
    line = file.readline()
    line = line.replace(' /', '')
    line = line.replace('Singer/Songwriter', 'Singer_Songwriter')
    if (re.search('(Shortcut)', line) != None):
        line = line.replace(' (Shortcut)', '')
        print("\nYou have done\n" + line + "before.\n")   
    return line


def next_gen():


    time.sleep(0.05)
    
    # read genre.txt
    filet = open('genre.txt', 'r', encoding='utf8')
    # load information from last session
    gen = filet.readline()
    sub = filet.readline()
    lnumb = filet.readline()
    # newline fucks with program, must remove
    gen = gen.rstrip('\n')
    sub = sub.rstrip('\n')
    lnumb = lnumb.rstrip('\n')
    lnumb = int(lnumb)
    filet.close()

    
    general = []

    # genre to increment
    nextfil = open('Genres\\' + re.sub(r'\\[\-\[\]\&\w\s\\]+', '', gen) + '.txt', 'r', encoding='utf8')

    # create array
    jee = gen.split('\\')
    # back to previous directory if just finished 
    # aka. subgenre General
    if (re.search('General', sub) != None):
        gen = jee[:-1]
        jee = jee[:-1]
        gen = '\\'.join(gen)
    else:
        general.append(sub)

    # lfold = last folder of previous subgenre
    lfold = jee[len(jee)-1]

    # number of folders deep ie. number of tabs
    depth = gen.count('\\') + 1

    # initialize
    line = nextl(nextfil)
    dep = line.count('\t')
    inside = False
    compn = 0

    # find last genere line
    # & add to general
    if (gen != sub):
        while (sub != re.sub(r'[\t\n]+', '', line) and line != '' or lnumb > compn):
            
            if (inside == True and dep == depth and not line.isspace()):
                general.append(re.sub(r'[\t\n:]', '', line))

            if (lfold == re.sub(r'[\t\n:]+', '', line)):
                inside = True

            line = nextl(nextfil)
            dep = line.count('\t')
            compn += 1
            
    line = nextl(nextfil)
    lnumb += 1
    # make sure not space
    while (line.isspace() == True):
        line = nextl(nextfil)
        lnumb += 1

    # check if next line is folder or subgenre
    while (re.search(':', line) != None):
        gen += '\\' + re.sub(r'[\n\t:]', '', line)
        line = nextl(nextfil)
        lnumb += 1
    
    sub = re.sub(r'[\n\t]', '', line)

    nextfil.close()


    lfold = sub.replace(' General', '')
    general.append(lfold)
    for i in range(len(general)):
        general[i] = unidecode.unidecode(general[i])
        if (re.search('[Punk]', general[i]) != None):
            general[i] = general[i].replace('[Punk]', 'Punk 1')
        general[i] = re.sub(r'[\[\]\'\!]', '', general[i])
        general[i] = general[i].replace('&', 'and')
        general[i] = general[i].lower()
        general[i] = general[i].replace(' ', '-')
        
    popexcl = 'https://rateyourmusic.com/charts/popular/album,ep,mixtape/all-time/g:' + general[i]
    poplink = popexcl + '/exc:live,archival/'
    toplink = poplink.replace('popular', 'top') + 'pop:1/'
    
    # -1 to remove the general genre
    for i in range(len(general)-1):
        popexcl += ',-' + general[i]
    popexcl += '/exc:live,archival/'

    topexcl = popexcl.replace('popular', 'top') + 'pop:1/'

    # sublink.replace('popular', 'top') + 'pop:1/'

    genlink = 'https://rateyourmusic.com/genre/' + general[len(general)-1] + '/'


    time.sleep(0.05)
    if (input('\nCreate TXT File? y or n\n') == 'y'):

        # goes to correct chrome tab
        pg.moveTo(660, 1060)
        pg.click()
        pg.moveTo(60, 30)
        pg.click()

        # paste chart url decade 2020
        pyperclip.copy(poplink)
        pg.moveTo(220, 80)
        pg.click()
        pg.hotkey('ctrl', 'a')
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        # new tab (must have two tabs open)
        pg.hotkey('ctrl', 'tab')
        # paste genre url
        pyperclip.copy(genlink)
        pg.moveTo(220, 80)
        pg.click()
        pg.hotkey('ctrl', 'a')
        pg.hotkey('ctrl', 'v')
        pg.press('enter')

        # wait for page to load
        time.sleep(4)

        # copy entire page
        pg.hotkey('ctrl', 'a')
        pg.hotkey('ctrl', 'c')   

        time.sleep(1)
        gentext = clipboard.paste()
        # Find number of releases
        gentext = gentext.split()
        for i in range(len(gentext)):
            gentext[i] = gentext[i].replace('(', '')
            gentext[i] = gentext[i].replace(')', '')
            if (re.search(gentext[i], 'releases') != None):
                break
        
        # create path
        if (not os.path.exists('Finished\\' + gen)):
            os.makedirs('Finished\\' + gen)

        gs = open('Finished\\' + gen + '\\' + gentext[i-1].replace(',', '') + ' ' + sub + '.txt', 'w', encoding='utf8')

        
        gs.write('Subgenre: ' + sub + '\n')
        gs.write('Main Genre Path: ' + gen + '\n')
        gs.write('Number of Releases: ' + gentext[i-1] + '\n\n')

        gs.write('Date Created: ' + str(date.today()) + '\n\n')

        gs.write('(Double click to open links in your text editor of choice.\n' +
            '\tSome text editors do not allow opening links.)\n\n')

        gs.write('Genre Link:\n')
        gs.write(genlink + '\n\n')

        gs.write('Best of All Time:\n')
        gs.write(toplink + '\n\n')

        gs.write('Most Popular of All Time:\n')
        gs.write(poplink + '\n\n\n')

        if (re.search('General', sub) != None):
            gs.write('(Exclusive means the chart excludes subgenres within this genre\n' +
                '\tthat can be and have been made into their own txt file)\n\n')
            gs.write('Exclusive Best of All Time:\n')
            gs.write(topexcl + '\n\n')

            gs.write('Exclusive Most Popular of All Time:\n')
            gs.write(popexcl + '\n\n\n')

        print('Number of Releases: ' + gentext[i-1] + '\n')
        dec = input('Specify decade range.\nFor example, "1940-2020"\nType "n" to have no decades\n')

        if (dec != 'n'):
            gs.write('\n\n\n')
            gs.write('Best by Decade:\n\n')

            dec = dec.split('-')
            dec[0] = int(dec[0]) - 10
            dec[1] = int(dec[1])

            for year in range(dec[1], dec[0], -10):
                gs.write(str(year) + '\'s:\n')
                gs.write(toplink.replace('all-time', str(year) + 's') + '\n')

            gs.write('\n\n')
            gs.write('Most Popular by Decade:\n\n')

            for year in range(dec[1], dec[0], -10):
                gs.write(str(year) + '\'s:\n')
                gs.write(poplink.replace('all-time', str(year) + 's') + '\n')

        gs.close()
    
    #if (input('\nMove genre.txt to new genre? y or n\n') == 'y'):

    # Write to genre.txt
    filet = open('genre.txt', 'w', encoding='utf8')
    filet.write(gen + '\n' + sub + '\n' + str(lnumb) + '\n')
    filet.close()

    # repeat
    return True


#debug main
if __name__ == "__main__":

    restart = True
    while (restart == True):
        restart = next_gen()