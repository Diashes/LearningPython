import random

# Bättre printmode
# pausfunktion som man kan pausa efter x antal bollar

class Spelare:
    
    def __init__(self, namn, speladeMatcher, vunnaMatcher, vinstprocent):
        self.namn = namn
        self.vunnaMatcher = vunnaMatcher
        self.speladeMatcher = speladeMatcher
        self.vinstprocent = vinstprocent

    def __str__(self):
        return self.namn

# Klass Tävling
#   spelarLista - en lista som skapas för att hålla information som läses från en fil med spelarna.
    
class Tävling:
    
    # Skapar lista med spelare som finns i en fil.
    
    def __init__(self):
        self.spelarLista = list()

    def läs(self, filnamn):
        fil = open(filnamn, 'rU')
        for rad in fil:
            rad = rad.strip().split('/')
            spelare = Spelare(rad[0], rad[1], rad[2], rad[3])
            self.spelarLista.append(spelare)
        fil.close()
        return self.spelarLista

    # Sparar lista med spelare till en fil.
    
    def spara(self, filnamn):
        print('Sparar resultat till listan..')
        fil = open(filnamn, 'w')
        for spelare in self.spelarLista:
            fil.write('{}/{}/{}/{}'.format(spelare.namn, spelare.vinstprocent, spelare.speladeMatcher, spelare.vunnaMatcher))
            fil.close()

    def meddelande(self):
        print('\nVälkommen till Tennis Cup 2014!\nNedan finns en lista med alla tävlande.\nVälj spelarens placeringsnummer för att tävla.')
        self.visaSpelare(self.spelarLista)
        valdSpelare1 = input('Spelare A: ')
        valdSpelare1 = self.spelarLista[int(valdSpelare1)-1]
        valdSpelare2 = input('Spelare B: ')
        print()
        valdSpelare2 = self.spelarLista[int(valdSpelare2)-1]
        return valdSpelare1, valdSpelare2

    # Sorterar listan med spelare på vinstprocent.

    def sortera(self, osorteradLista):
        sorteradLista = sorted(osorteradLista, key=lambda sorteradSpelare: sorteradSpelare.vinstprocent, reverse=True)
        return sorteradLista

    # Visar lista med spelare.
    
    def visaSpelare(self, spelarLista):
        i = 0
        print('\nPlacering/Namn/Spelade/Vunna/%Vunna')
        while (len(spelarLista) > i):
            print('{}/{}/{}/{}/{}'.format(i + 1, spelarLista[i].namn, spelarLista[i].speladeMatcher, spelarLista[i].vunnaMatcher, spelarLista[i].vinstprocent))
            i += 1
        print()


class Game:
    def __init__(self, spelareA, spelareB, servare):
        self.spelare = [spelareA, spelareB]
        self.bollar = [0, 0]
        self.servare = servare
        self.fördel = -1
        self.vinnare = -1

    def spelaBollen(self):
        rand = random.randrange(1, 100)/100
        print(rand)
        if (float(self.spelare[servare].vinstprocent) <= rand):
            gePoäng(servare)
        else:
            gePoäng(invert(servare))

    def gePoäng(self, vannBoll):
        if (self.bollar[vannBoll] == 3):
            if (self.bollar[invert(vannBoll)] == 3):
                if (self.fördel == vannBoll):
                    self.vinnare = vannBoll
                else:
                    self.fördel = vannBoll
            else:
                self.vinnare = vannBoll
        else:
            self.bollar[vannBoll] += 1

    def getVinnare(self):
        if (self.vinnare != -1):
            return self.spelare[vinnare]
        else:
            return None






class Set:
    def __init__(self, spelareA, spelareB, servare):
        self.spelare[spelareA, spelareB]
        self.vinnare = -1
        self.games = [Game(spelareA, spelareB, servare), None*5]
        self.aktivtGame = 0

    def nyttGame(self):
        servare = invert(getGame().servare)
        self.aktivtGame += 1
        self.games[self.aktivtGame] = Game(self.spelare[0], self.spelare[1], servare)

    def getGame(self):
        return self.games[self.aktivtGame]
        
    def getVinnare(self):
        if (self.vinnare != -1):
            return self.spelare[vinnare]
        else:
            return None






        
       
class Match:
    
    def __init__(self, spelareA, spelareB):
        self.vinnare = False
        self.sets = [Set(spelareA, spelareB, random.choice([0, 1])), None, None]
        self.spelareA = spelareA
        self.spelareB = spelareB

    def nyttSet(self):
        servare = invert(getSet().getGame().servare)
        self.aktivtGame += 1
        self.games[self.aktivtGame] = Game(self.spelare[0], self.spelare[1], servare) 

    def spela(self):
        getSet().getGame().spelaBollen()

    def getSet(self):
        return

# KLASS MATCH

class Match2:
    def __init__(self, spelareA, spelareB, printMode):
        self.vinnare = None
        self.spelare = [spelareA, spelareB]
        self.bollar = [0, 0]
        self.games = [0, 0]
        self.set = [0, 0]
        self.servare = random.randrange(0, 1);
        self.fördel = -1
        self.printMode = printMode

    def nyttSet(self, vannGame):
        self.set[vannGame] += 1
        self.games = [0, 0]
        if (self.set[0] + self.set[1] == 3):
            if (self.set[0] == 2):
                self.vinnare = self.spelare[0]
            else:
                self.vinnare = self.spelare[1]
        else:
            print(str(self.spelare[vannGame].namn), 'vann setet.')
                
        if (self.printMode == 2):
            self.visaPoäng()

    def nyttGame(self, vannBoll):
        self.games[vannBoll] += 1
        self.bollar = [0, 0]
        self.servare = invert(self.servare)
        self.fördel = -1
        if (self.games[vannBoll] > self.games[invert(vannBoll)]
            + 1 and self.games[vannBoll] >= 6):
            self.nyttSet(vannBoll)
        else:
            print(str(self.spelare[vannBoll].namn), 'vann gamet.')
            
        if (self.printMode == 1):
            self.visaPoäng()

    def spela(self):
        rand = random.randrange(1, 100)/100
        print(str(self.spelare[self.servare].namn), 'servar.')
        if (float(self.spelare[self.servare].vinstprocent) <= rand):
            self.gePoäng(self.servare)
        else:
            self.gePoäng(invert(self.servare))
            
        if (self.printMode == 0):
            self.visaPoäng()

    def gePoäng(self, vannBoll):
        if (self.bollar[vannBoll] == 3):
            if (self.bollar[invert(vannBoll)] == 3):
                if (self.fördel == vannBoll):
                    self.nyttGame(vannBoll)
                else:
                    self.fördel = vannBoll
                    print(str(self.spelare[vannBoll].namn), 'vann bollen.')
            else:
                self.nyttGame(vannBoll)
        else:
            self.bollar[vannBoll] += 1
            print(str(self.spelare[vannBoll].namn), 'vann bollen.')

    def poäng(self, bollar):
        if (bollar == 0):
            return 0
        elif (bollar == 1):
            return 15
        elif (bollar == 2):
            return 30
        else:
            return 40
    
    def visaPoäng(self):
        print('Namn\tPoäng\tGames\tSet')
        print('{}\t{}{}\t{}\t{}'.format(self.spelare[0].namn, self.poäng(self.bollar[0]), "+" if self.fördel == 0 else "", self.games[0], self.set[0]))
        print('{}\t{}{}\t{}\t{}'.format(self.spelare[1].namn, self.poäng(self.bollar[1]), "+" if self.fördel == 1 else "", self.games[1], self.set[1]))


# FUNKTIONER

def invert(tal):
    if (tal == 0):
        return 1
    else:
        return 0

def paus():
    input()


# HUVUDPROGRAM
        
spelareA = Spelare("Amanda", 0, 0, 0.51)
spelareB = Spelare("Jesper", 0, 0, 0.49)
match = Match2(spelareA, spelareB, 0)

while(match.vinnare == None):
    match.spela()

print(str(match.vinnare.namn), 'vann matchen.')


