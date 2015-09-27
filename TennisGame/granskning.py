#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
# Titel: Tennismatch
# F�rfattare: Amanda Stensland
# Datum: 2014-08-27
#
# Programmet simulerar en tennist�vling
# d�r man kan v�lja tv� spelare som ska
# spela en tennismatch.
#
# Programmet lagrar spelarna i en fil
# "spelare.txt" n�r programmet inte k�rs.
# Varje rad i filen inneh�ller en spelare
# beskriven i f�ljande format:
#
# <NAMN>/<SPELADEMATCHER>/<VUNNAMATCHER>/<VINSTPROCENT>
#
# Spelarna och deras resultat sparas endast
# till filen n�r man v�ljer "Avsluta"-alternativet
# och inte automatiskt efter varje match.

import random

# class Spelare -------------------------------------- 
#
# attribut:
#   namn            -   spelarens namn
#   speladeMatcher  -   antal spelade matcher
#   vunnaMatcher    -   antal vunna matcher
#   vinstprocent    -   vinstchans
#
# metoder:
#    def __init__    -    IN: namn, speladeMatcher, vunnaMatcher, vinstprocent
#    def __str__     -    UT: Returnerar namnet p� spelaren.

class Spelare:
    def __init__(self, namn, speladeMatcher, vunnaMatcher, vinstprocent):
        self.namn = namn
        self.speladeMatcher = int(speladeMatcher)
        self.vunnaMatcher = int(vunnaMatcher)
        self.vinstprocent = float(vinstprocent)
        
    def __str__(self):
        return self.namn
    
# class T�vling -------------------------------------- 
#
# attribut:
#   lista[]             -   objekt av Spelare samlas i listan.
#
# metoder:
#   def __init__        -    IN: filnamn - �r en string med namnet p� filen med
#                                          information om spelare.
#   def meny()          -    Visar en lista med alternativ f�r anv�ndaren.
#   def l�s()           -    Tar emot filnamnet p� filen som ska l�sas.
#                                L�ser in information fr�n textfilen och skapar 
#                                Spelare-objekt som sedan l�ggs till i lista[].
#                                IN: filnamn (string med filets namn)
#   def l�ggTillSpelare -    Fr�gar anv�ndaren efter namn och skapar sen ett 
#                                nytt Spelare-objekt.
#   def spara()         -    Sparar information i lista[] till textfil.
#   def v�ljSpelare()   -    Fr�gar efter 2 spelare som ska t�vla. Startar
#                                sedan en match.
#   def visaSpelare()   -    Visar en lista med alla spelare.
#   def sortera()       -    Sorterar listan p� vinstprocent.
#                                IN: Lista som ska sorteras.
#                                UT: Sorterad lista.

class T�vling:

    def __init__(self, filnamn):
        # IN: filnamn - �r en string med namnet p� filen med
        # information om spelare.
        self.lista = list()
        self.l�s(filnamn)
        self.filnamn = filnamn

    def meny(self):
    # def: Visar meny med alternativ
        val = ''
        while (val is not '1' and '2' and '3' and '4'):
            val = input('\nV�lkommen till Tennist�vlingen! Vad vill du g�ra?\n1. Spela match\n2. L�gg till spelare\n3. Visa deltagande spelare\n4. Avsluta och spara\n')
            if (val == '1'):
                self.v�ljSpelare()
            elif (val == '2'):
                self.l�ggTillSpelare()
            elif (val == '3'):
                self.visaSpelare()
            elif (val == '4'):
                t�vling.spara()
                print('Sparar...\nTack, hej d�!')
                exit()
            else:
                print('Valet finns inte!')

    def l�s(self, filnamn):
    # def: L�ser fil med spelare.
        try:
            fil = open(filnamn, 'rU')
        except FileNotFoundError:
            # Om filen inte finns. Skapa en ny fil.
            fil = open(filnamn, 'w')
            fil.close()
            fil = open(filnamn, 'rU')
            
        # L�gg till spelare i filen till en lista.
        for rad in fil:
            rad = rad.strip().split('/')
            try:
                nySpelare = Spelare(rad[0], rad[1], rad[2], rad[3])
                self.lista.append(nySpelare)
                ifEmpty(self.lista)
            except IndexError:
                # Om filen inneh�ller fel information. T.ex. saknar radbrytning etc.
                print('v�rdet i textfilen �r fel')
        fil.close()

    # def: L�gger till nya spelare.
    def l�ggTillSpelare(self):
        namn = input('Namn: ')
        if (namn in self.lista):
            print('Det finns redan en spelare som heter s�. V�lj ett annat namn.')
            self.l�ggTillSpelare()
        # Slumpar fram en vinstprocent �t den nya spelaren.
        vinstprocent = str(random.randrange(10,100)/100)
        # Skapar nytt objekt.
        nySpelare = Spelare(namn, 0, 0, vinstprocent)
        # L�gger till i listan med spelare.
        self.lista.append(nySpelare)

    # def: Sparar till fil.
    def spara(self):
        fil = open(self.filnamn, 'w')
        for spelare in self.lista:
            fil.write('{}/{}/{}/{}\n'.format(spelare.namn,
                                           spelare.speladeMatcher,
                                           spelare.vunnaMatcher,
                                           spelare.vinstprocent))
        fil.close()          

    # def: V�ljer spelare som ska t�vla.
    def v�ljSpelare(self):
        # Om det inte finns tillr�ckligt m�nga Spelare-objekt.
        if (len(t�vling.lista) <= 1):
            print('\nDet finns inte tillr�ckligt m�nga t�vlande, det g�r inte att spela en match.')
            self.meny()
        else:
            # Visar lista med spelare att v�lja mellan.
            self.visaSpelare()
            # L�s in namnet p� tv� spelare.
            print('\nSpelarna �r sorterade p� placering.\nV�lj en spelares placering f�r att v�lja den spelaren. \n')
            try:
                spelareA = self.lista[int(input('F�rsta spelaren: '))-1]
                spelareB = self.lista[int(input('Andra spelaren: '))-1]
            # Kontrollerar om spelarna finns i listan.
            except IndexError:
                print('Placeringen existerar inte. �terg�r till menyn.')
                self.meny()
            except ValueError:
                print('Placeringen existerar inte. �terg�r till menyn.')
                self.meny()
        # Startar ny match med de utvalda spelarna.
        Match(spelareA, spelareB)

    # def: Visar spelare i tabell.
    def visaSpelare(self):
        self.lista = self.sortera(self.lista)
        i = 0
        print('\nAktuella spelare: \n')
        mall = "{0:<5} {1:<14} {2:<8} {3:<8} {4}"
        print(mall.format('Plac', 'Namn', 'Spelade', 'Vunna', '%vunna'))
        while (len(self.lista) > i):
            print(mall.format(i + 1,
                              self.lista[i].namn,
                              self.lista[i].speladeMatcher,
                              self.lista[i].vunnaMatcher,
                              self.lista[i].vinstprocent))
            i += 1

    def sortera(self, lista):
    # def: Sorterar spelare p� vinstprocent
    # IN: Lista som ska sorteras.
    # UT: Sorterad lista.
        return sorted(lista, key=lambda spelare: spelare.vinstprocent, reverse=True)
        
# class Match --------------------------------------
# 
# attribut:
#   vinnare     -   n�r matchen �r slut s�tts den till spelaren som vann.
#   spelare[]   -   lista med tv� spelare som t�vlar.
#   bollar[]    -   lista som h�ller koll p� bollar f�r b�da spelarna.
#   games[]     -   lista som h�ller koll p� games f�r b�da spelarna.
#   sets[]      -   lista som h�ller koll p� sets f�r b�da spelarna.
#   servar      -   s�tts random till n�gon av spelarna i b�rjan av matchen.
#   f�rdel      -   s�tts till 1 eller 0 beroende p� vilket spelare som leder.
#                   b�rjar bara g�lla n�r b�da spelarna har 40 po�ng eller �ver.
#   r�knaBollar,
#   r�knaGames,
#   r�knaSet    -   h�ller koll p� antalet bollar, games, sets totalt som har spelats f�r pausfunktionen.
#   printMode   -   om anv�ndaren vill se resultatet f�r bollar, games eller sets.
#   intervall   -   antalet bollar, games, sets som anv�ndaren valt att hoppa �ver.
#
# metoder:
#   def __init__()      -   IN: spelareA, spelareB - spelare som ska spela matchen.
#   def v�ljPrintMode() -   Fr�gar hur ofta anv�ndaren vill se resultatet under
#                               matchen.
#                               UT: printMode - best�mmer om spelet ska pausas p� bollar, game eller set.
#                                   intervall - best�mmer efter hur m�nga bollar, game eller set som spelet
#                                           ska pausas.
#   def spelaBollen()   -   Spelar och slumpar sedan vinstchansen f�r att se
#                               vem som vann bollen.
#   def gePo�ng()       -   Ger po�ng till spelaren som vann bollen. Kollar om
#                               po�ngen avgjorde gamet, setet eller matchen.
#                               IN: vannBoll - spelaren som vunnit bollen.
#   def po�ng()         -   Omvandlar en spelares antal vunna bollar till po�ng.
#   def visaPo�ng()     -   Skriver ut po�ngst�llningen.
#   def nyttGame()      -   Skapar nytt game.
#                               IN: vannBoll - spelaren som vunnit bollen.
#   def nyttSet()       -   Skapar nytt set.
#                               IN: vannGame - spelaren som vunnit gamet.

class Match:

    def __init__(self, spelareA, spelareB):
    # IN: spelareA, spelareB - spelare som ska spela matchen.
        self.vinnare = None
        self.spelare = [spelareA, spelareB]
        self.bollar = [0,0]
        self.games = [0,0]
        self.sets = [0,0]
        self.servar = random.randrange(0,1)
        self.f�rdel = -1
        self.r�knaBollar = 0
        self.r�knaGames = 0
        self.r�knaSets = 0
        self.printMode, self.intervall = self.v�ljPrintMode()

        # Spelar bollen tills en spelare vunnit och kollar hur ofta
        # matchen ska pausas. Skriver sen ut vem som vann och �terg�r till menyn.
        while (self.vinnare == None):
            self.spelaBollen()
            if (self.printMode == '1' and self.r�knaBollar == self.intervall):
                paus()
                self.r�knaBollar = 0
            elif (self.printMode == '2' and self.r�knaGames == self.intervall):
                self.r�knaGames = 0
                paus()
            elif (self.printMode == '3' and self.r�knaSets == self.intervall):
                self.r�knaSets = 0
                paus()

        # N�r matchen �r slut.
        print('\n*************************\n*** {} vann matchen! ***\n*************************'.format(self.vinnare))
        # Spelarna ges po�ng f�r vunnen match och antal spelade matcher.
        self.vinnare.vunnaMatcher += 1
        self.spelare[0].speladeMatcher += 1
        self.spelare[1].speladeMatcher += 1
        t�vling.meny()


    def v�ljPrintMode(self):
    # def: V�lj intervall f�r po�ngutskrivning.
    # UT: printMode - best�mmer om spelet ska pausas p� bollar, game eller set.
    # intervall - best�mmer efter hur m�nga bollar, game eller set som spelet
    # ska pausas.
    
        printMode = input('\nN�r vill du pausa matchen f�r att hinna se resultatet?\n1. Bollar\n2. Games\n3. Sets\n')
        typ = ''
        while(True):
            if (printMode == '1'):
                typ = 'bollar'
                break
            elif (printMode == '2'):
                typ = 'games'
                break
            elif (printMode == '3'):
                return printMode, 1     # ettan betyder att intervallet f�r set s�tts automatiskt till 1 set
                break
            else:
                printMode = input('Du m�ste v�lja en siffra: ')
                
        intervall = int(input('\nEfter hur m�nga {} ska matchen pausas? '.format(typ)))
        return printMode, intervall

    
    def spelaBollen(self):
    # def: Spela Bollen. Slumpar ut chansen f�r vem som ska vinna.
    
        print('\n{} servar bollen.'.format( self.spelare[self.servar] ))
        
        # Spelarens chans att vinna - r�knas ut med random.
        chans = random.uniform(0.10, 0.99)
        print('Chans:', chans)
        
        # Om chans �r mindre �n servarens vinstprocent s� vinner servaren.
        # Annars vinner den andra spelaren.
        if (float(self.spelare[self.servar].vinstprocent) > chans):
            self.gePo�ng(self.servar)
        else:
            self.gePo�ng(invert(self.servar))
        self.visaPo�ng()

    def gePo�ng(self, vannBoll):
    # def: Ge Po�ng.
    # IN: vannBoll - spelaren som vunnit bollen.
    
        self.r�knaBollar += 1

        # Kollar om vinnaren av bollen har vunnit gamet, 
        # annars ges bara po�ng.
        if (self.bollar[vannBoll] == 3): #Om spelaren som vann bollen har 3 bollar
            if (self.bollar[invert(vannBoll)] == 3): #Om den andra spelaren ocks� har 3 bollar
                if (self.f�rdel == vannBoll): #Om spelaren som vann bollen har f�rdel
                    self.nyttGame(vannBoll) # Vinner gamet
                else:
                    self.f�rdel = vannBoll #Annars Ges f�rdel
                    print(self.spelare[vannBoll], 'vann bollen.') #vinner bollen
            else:
                self.nyttGame(vannBoll)
        else:
            self.bollar[vannBoll] += 1
            print(self.spelare[vannBoll], 'vann bollen.')

    def po�ng(self, bollar):
    # def: Omvandlar antalet vunna bollar till po�ng.
    # IN: bollar - antal bollar som en spelare vunnit.
        
        if (bollar == 0):
            return 0
        elif (bollar == 1):
            return 15
        elif (bollar == 2):
            return 30
        else:
            return 40

    def visaPo�ng(self):
    # def: Visa Po�ng.
    
        # Beskriver mall f�r hur po�ngen ska skrivas ut p� sk�rmen.
        mall1 = '{0:<14} {1:<10} {2:<8} {3}'
        mall2 = '{0:<14} {1:1}{2:<8} {3:<8} {4}'
        print(mall1.format('\nNamn', 'Po�ng', 'Games', 'Set'))
        print(mall2.format(self.spelare[0].namn,
                                        self.po�ng(self.bollar[0]),
                                        "+" if self.f�rdel == 0 else "",
                                        self.games[0], self.sets[0]))
        print(mall2.format(self.spelare[1].namn,
                                        self.po�ng(self.bollar[1]),
                                        "+" if self.f�rdel == 1 else "",
                                        self.games[1], self.sets[1]))

    def nyttGame(self, vannBoll):
    # def: Nytt Game.
    # IN: vannBoll - spelaren som vunnit bollen.

        self.r�knaGames += 1
        self.games[vannBoll] += 1
        self.bollar = [0,0] #Nollst�ller bollar f�r b�da spelarna.
        self.servar = invert(self.servar) #Byter servare.
        self.f�rdel = -1 #Nollst�ller f�rdel.
        
        # Kollar om n�gon har vunnit setet.
        if (self.games[vannBoll] >= 6 and self.games[vannBoll] > (self.games[invert(vannBoll)])): #OM vannboll har mer �n 6 set och har mer games �n den andra spelaren
            self.nyttSet(vannBoll)            
        else:
            print('*** {} vann gamet. ***'.format(self.spelare[vannBoll]))

    def nyttSet(self, vannGame):
    # def: Nytt Set.
    # IN: vannGame - spelaren som vunnit gamet.

        self.r�knaSets += 1
        self.sets[vannGame] += 1
        self.games = [0,0]

        # Kollar om n�gon har vunnit matchen.
        if (self.sets[0] + self.sets[1] == 3):
            if (self.sets[vannGame] == 2):
                self.vinnare = self.spelare[vannGame]
            elif (self.sets[vannGame] == 3):
                self.vinnare = self.spelare[vannGame]
            else:
                self.vinnare = self.spelare[invert(vannGame)]
        else:
            print('*** {} vann setet. ***'.format(self.spelare[vannGame]))

# Funktioner -------------------------------------- 
#
#   def invert()    -   Inverterar talet 1 till 0 och tv�rtom.
#                           IN: talet man vill invertera.
#                           UT: inverterat tal.
#   def paus()      -   Pausar matchen.
#   ifEmpty()       -   Kollar om en lista �r tom. Fr�gar om man
#                           vill skapa en ny spelare (om listan �r tom).
#                           IN: Listan som man vill kontrollera.

def invert(tal):
# def: Inverterar tal
    if (tal == 0):
        return 1
    else:
        return 0

def paus():
# def: Pausar matchen
    input('\n*** Spelet pausat. Tryck enter f�r att forts�tta. ***')

def ifEmpty(lista):
# def: Om en lista �r tom.
# IN: En lista man vill kontrollera om den �r tom.
    if not lista:
        print('Det finns tyv�rr inga deltagande i denna t�vling.')
        ny = input('Vill du l�gga till en ny spelare i t�vlingen? ja/nej').lower()
        if (ny.startswith('j')):
            t�vling.l�ggTillSpelare()
        else:
            exit()

# Main -------------------------------------- 

# Skapar ny t�vling.
t�vling = T�vling('spelare.txt')
# Visar menyn.
t�vling.meny()