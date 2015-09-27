#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
# Titel: Tennismatch
# Författare: Amanda Stensland
# Datum: 2014-08-27
#
# Programmet simulerar en tennistävling
# där man kan välja två spelare som ska
# spela en tennismatch.
#
# Programmet lagrar spelarna i en fil
# "spelare.txt" när programmet inte körs.
# Varje rad i filen innehåller en spelare
# beskriven i följande format:
#
# <NAMN>/<SPELADEMATCHER>/<VUNNAMATCHER>/<VINSTPROCENT>
#
# Spelarna och deras resultat sparas endast
# till filen när man väljer "Avsluta"-alternativet
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
#    def __str__     -    UT: Returnerar namnet på spelaren.

class Spelare:
    def __init__(self, namn, speladeMatcher, vunnaMatcher, vinstprocent):
        self.namn = namn
        self.speladeMatcher = int(speladeMatcher)
        self.vunnaMatcher = int(vunnaMatcher)
        self.vinstprocent = float(vinstprocent)
        
    def __str__(self):
        return self.namn
    
# class Tävling -------------------------------------- 
#
# attribut:
#   lista[]             -   objekt av Spelare samlas i listan.
#
# metoder:
#   def __init__        -    IN: filnamn - är en string med namnet på filen med
#                                          information om spelare.
#   def meny()          -    Visar en lista med alternativ för användaren.
#   def läs()           -    Tar emot filnamnet på filen som ska läsas.
#                                Läser in information från textfilen och skapar 
#                                Spelare-objekt som sedan läggs till i lista[].
#                                IN: filnamn (string med filets namn)
#   def läggTillSpelare -    Frågar användaren efter namn och skapar sen ett 
#                                nytt Spelare-objekt.
#   def spara()         -    Sparar information i lista[] till textfil.
#   def väljSpelare()   -    Frågar efter 2 spelare som ska tävla. Startar
#                                sedan en match.
#   def visaSpelare()   -    Visar en lista med alla spelare.
#   def sortera()       -    Sorterar listan på vinstprocent.
#                                IN: Lista som ska sorteras.
#                                UT: Sorterad lista.

class Tävling:

    def __init__(self, filnamn):
        # IN: filnamn - är en string med namnet på filen med
        # information om spelare.
        self.lista = list()
        self.läs(filnamn)
        self.filnamn = filnamn

    def meny(self):
    # def: Visar meny med alternativ
        val = ''
        while (val is not '1' and '2' and '3' and '4'):
            val = input('\nVälkommen till Tennistävlingen! Vad vill du göra?\n1. Spela match\n2. Lägg till spelare\n3. Visa deltagande spelare\n4. Avsluta och spara\n')
            if (val == '1'):
                self.väljSpelare()
            elif (val == '2'):
                self.läggTillSpelare()
            elif (val == '3'):
                self.visaSpelare()
            elif (val == '4'):
                tävling.spara()
                print('Sparar...\nTack, hej då!')
                exit()
            else:
                print('Valet finns inte!')

    def läs(self, filnamn):
    # def: Läser fil med spelare.
        try:
            fil = open(filnamn, 'rU')
        except FileNotFoundError:
            # Om filen inte finns. Skapa en ny fil.
            fil = open(filnamn, 'w')
            fil.close()
            fil = open(filnamn, 'rU')
            
        # Lägg till spelare i filen till en lista.
        for rad in fil:
            rad = rad.strip().split('/')
            try:
                nySpelare = Spelare(rad[0], rad[1], rad[2], rad[3])
                self.lista.append(nySpelare)
                ifEmpty(self.lista)
            except IndexError:
                # Om filen innehåller fel information. T.ex. saknar radbrytning etc.
                print('värdet i textfilen är fel')
        fil.close()

    # def: Lägger till nya spelare.
    def läggTillSpelare(self):
        namn = input('Namn: ')
        if (namn in self.lista):
            print('Det finns redan en spelare som heter så. Välj ett annat namn.')
            self.läggTillSpelare()
        # Slumpar fram en vinstprocent åt den nya spelaren.
        vinstprocent = str(random.randrange(10,100)/100)
        # Skapar nytt objekt.
        nySpelare = Spelare(namn, 0, 0, vinstprocent)
        # Lägger till i listan med spelare.
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

    # def: Väljer spelare som ska tävla.
    def väljSpelare(self):
        # Om det inte finns tillräckligt många Spelare-objekt.
        if (len(tävling.lista) <= 1):
            print('\nDet finns inte tillräckligt många tävlande, det går inte att spela en match.')
            self.meny()
        else:
            # Visar lista med spelare att välja mellan.
            self.visaSpelare()
            # Läs in namnet på två spelare.
            print('\nSpelarna är sorterade på placering.\nVälj en spelares placering för att välja den spelaren. \n')
            try:
                spelareA = self.lista[int(input('Första spelaren: '))-1]
                spelareB = self.lista[int(input('Andra spelaren: '))-1]
            # Kontrollerar om spelarna finns i listan.
            except IndexError:
                print('Placeringen existerar inte. Återgår till menyn.')
                self.meny()
            except ValueError:
                print('Placeringen existerar inte. Återgår till menyn.')
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
    # def: Sorterar spelare på vinstprocent
    # IN: Lista som ska sorteras.
    # UT: Sorterad lista.
        return sorted(lista, key=lambda spelare: spelare.vinstprocent, reverse=True)
        
# class Match --------------------------------------
# 
# attribut:
#   vinnare     -   när matchen är slut sätts den till spelaren som vann.
#   spelare[]   -   lista med två spelare som tävlar.
#   bollar[]    -   lista som håller koll på bollar för båda spelarna.
#   games[]     -   lista som håller koll på games för båda spelarna.
#   sets[]      -   lista som håller koll på sets för båda spelarna.
#   servar      -   sätts random till någon av spelarna i början av matchen.
#   fördel      -   sätts till 1 eller 0 beroende på vilket spelare som leder.
#                   börjar bara gälla när båda spelarna har 40 poäng eller över.
#   räknaBollar,
#   räknaGames,
#   räknaSet    -   håller koll på antalet bollar, games, sets totalt som har spelats för pausfunktionen.
#   printMode   -   om användaren vill se resultatet för bollar, games eller sets.
#   intervall   -   antalet bollar, games, sets som användaren valt att hoppa över.
#
# metoder:
#   def __init__()      -   IN: spelareA, spelareB - spelare som ska spela matchen.
#   def väljPrintMode() -   Frågar hur ofta användaren vill se resultatet under
#                               matchen.
#                               UT: printMode - bestämmer om spelet ska pausas på bollar, game eller set.
#                                   intervall - bestämmer efter hur många bollar, game eller set som spelet
#                                           ska pausas.
#   def spelaBollen()   -   Spelar och slumpar sedan vinstchansen för att se
#                               vem som vann bollen.
#   def gePoäng()       -   Ger poäng till spelaren som vann bollen. Kollar om
#                               poängen avgjorde gamet, setet eller matchen.
#                               IN: vannBoll - spelaren som vunnit bollen.
#   def poäng()         -   Omvandlar en spelares antal vunna bollar till poäng.
#   def visaPoäng()     -   Skriver ut poängställningen.
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
        self.fördel = -1
        self.räknaBollar = 0
        self.räknaGames = 0
        self.räknaSets = 0
        self.printMode, self.intervall = self.väljPrintMode()

        # Spelar bollen tills en spelare vunnit och kollar hur ofta
        # matchen ska pausas. Skriver sen ut vem som vann och återgår till menyn.
        while (self.vinnare == None):
            self.spelaBollen()
            if (self.printMode == '1' and self.räknaBollar == self.intervall):
                paus()
                self.räknaBollar = 0
            elif (self.printMode == '2' and self.räknaGames == self.intervall):
                self.räknaGames = 0
                paus()
            elif (self.printMode == '3' and self.räknaSets == self.intervall):
                self.räknaSets = 0
                paus()

        # När matchen är slut.
        print('\n*************************\n*** {} vann matchen! ***\n*************************'.format(self.vinnare))
        # Spelarna ges poäng för vunnen match och antal spelade matcher.
        self.vinnare.vunnaMatcher += 1
        self.spelare[0].speladeMatcher += 1
        self.spelare[1].speladeMatcher += 1
        tävling.meny()


    def väljPrintMode(self):
    # def: Välj intervall för poängutskrivning.
    # UT: printMode - bestämmer om spelet ska pausas på bollar, game eller set.
    # intervall - bestämmer efter hur många bollar, game eller set som spelet
    # ska pausas.
    
        printMode = input('\nNär vill du pausa matchen för att hinna se resultatet?\n1. Bollar\n2. Games\n3. Sets\n')
        typ = ''
        while(True):
            if (printMode == '1'):
                typ = 'bollar'
                break
            elif (printMode == '2'):
                typ = 'games'
                break
            elif (printMode == '3'):
                return printMode, 1     # ettan betyder att intervallet för set sätts automatiskt till 1 set
                break
            else:
                printMode = input('Du måste välja en siffra: ')
                
        intervall = int(input('\nEfter hur många {} ska matchen pausas? '.format(typ)))
        return printMode, intervall

    
    def spelaBollen(self):
    # def: Spela Bollen. Slumpar ut chansen för vem som ska vinna.
    
        print('\n{} servar bollen.'.format( self.spelare[self.servar] ))
        
        # Spelarens chans att vinna - räknas ut med random.
        chans = random.uniform(0.10, 0.99)
        print('Chans:', chans)
        
        # Om chans är mindre än servarens vinstprocent så vinner servaren.
        # Annars vinner den andra spelaren.
        if (float(self.spelare[self.servar].vinstprocent) > chans):
            self.gePoäng(self.servar)
        else:
            self.gePoäng(invert(self.servar))
        self.visaPoäng()

    def gePoäng(self, vannBoll):
    # def: Ge Poäng.
    # IN: vannBoll - spelaren som vunnit bollen.
    
        self.räknaBollar += 1

        # Kollar om vinnaren av bollen har vunnit gamet, 
        # annars ges bara poäng.
        if (self.bollar[vannBoll] == 3): #Om spelaren som vann bollen har 3 bollar
            if (self.bollar[invert(vannBoll)] == 3): #Om den andra spelaren också har 3 bollar
                if (self.fördel == vannBoll): #Om spelaren som vann bollen har fördel
                    self.nyttGame(vannBoll) # Vinner gamet
                else:
                    self.fördel = vannBoll #Annars Ges fördel
                    print(self.spelare[vannBoll], 'vann bollen.') #vinner bollen
            else:
                self.nyttGame(vannBoll)
        else:
            self.bollar[vannBoll] += 1
            print(self.spelare[vannBoll], 'vann bollen.')

    def poäng(self, bollar):
    # def: Omvandlar antalet vunna bollar till poäng.
    # IN: bollar - antal bollar som en spelare vunnit.
        
        if (bollar == 0):
            return 0
        elif (bollar == 1):
            return 15
        elif (bollar == 2):
            return 30
        else:
            return 40

    def visaPoäng(self):
    # def: Visa Poäng.
    
        # Beskriver mall för hur poängen ska skrivas ut på skärmen.
        mall1 = '{0:<14} {1:<10} {2:<8} {3}'
        mall2 = '{0:<14} {1:1}{2:<8} {3:<8} {4}'
        print(mall1.format('\nNamn', 'Poäng', 'Games', 'Set'))
        print(mall2.format(self.spelare[0].namn,
                                        self.poäng(self.bollar[0]),
                                        "+" if self.fördel == 0 else "",
                                        self.games[0], self.sets[0]))
        print(mall2.format(self.spelare[1].namn,
                                        self.poäng(self.bollar[1]),
                                        "+" if self.fördel == 1 else "",
                                        self.games[1], self.sets[1]))

    def nyttGame(self, vannBoll):
    # def: Nytt Game.
    # IN: vannBoll - spelaren som vunnit bollen.

        self.räknaGames += 1
        self.games[vannBoll] += 1
        self.bollar = [0,0] #Nollställer bollar för båda spelarna.
        self.servar = invert(self.servar) #Byter servare.
        self.fördel = -1 #Nollställer fördel.
        
        # Kollar om någon har vunnit setet.
        if (self.games[vannBoll] >= 6 and self.games[vannBoll] > (self.games[invert(vannBoll)])): #OM vannboll har mer än 6 set och har mer games än den andra spelaren
            self.nyttSet(vannBoll)            
        else:
            print('*** {} vann gamet. ***'.format(self.spelare[vannBoll]))

    def nyttSet(self, vannGame):
    # def: Nytt Set.
    # IN: vannGame - spelaren som vunnit gamet.

        self.räknaSets += 1
        self.sets[vannGame] += 1
        self.games = [0,0]

        # Kollar om någon har vunnit matchen.
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
#   def invert()    -   Inverterar talet 1 till 0 och tvärtom.
#                           IN: talet man vill invertera.
#                           UT: inverterat tal.
#   def paus()      -   Pausar matchen.
#   ifEmpty()       -   Kollar om en lista är tom. Frågar om man
#                           vill skapa en ny spelare (om listan är tom).
#                           IN: Listan som man vill kontrollera.

def invert(tal):
# def: Inverterar tal
    if (tal == 0):
        return 1
    else:
        return 0

def paus():
# def: Pausar matchen
    input('\n*** Spelet pausat. Tryck enter för att fortsätta. ***')

def ifEmpty(lista):
# def: Om en lista är tom.
# IN: En lista man vill kontrollera om den är tom.
    if not lista:
        print('Det finns tyvärr inga deltagande i denna tävling.')
        ny = input('Vill du lägga till en ny spelare i tävlingen? ja/nej').lower()
        if (ny.startswith('j')):
            tävling.läggTillSpelare()
        else:
            exit()

# Main -------------------------------------- 

# Skapar ny tävling.
tävling = Tävling('spelare.txt')
# Visar menyn.
tävling.meny()