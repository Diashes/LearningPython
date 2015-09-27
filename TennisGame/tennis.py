# -------------------------
# class Spelare
#   namn
#   speladeMatcher
#   vunnaMatcher
#   vinstprocent

class Spelare:
    def __init__(self, namn, speladeMatcher, vunnaMatcher, vinstprocent):
        self.namn = namn
        self.speladeMatcher = speladeMatcher
        self.vunnaMatcher = vunnaMatcher
        self.vinstprocent = vinstprocent

    def __str__(self):
        return self.namn

# -------------------------
# class Tävling
#   lista[]
#
#   def läs()
#   def spara()
#   def väljSpelare()
#   def visaSpelare()
#   def sortera()

class Tävling:
    def __init__(self):
        lista = list()

    def läs(self, filnamn):
        fil = open(filnamn, 'rU')
        for rad in fil:
            rad = rad.strip().split('/')
            nySpelare = Spelare(rad[0], rad[1], rad[2], rad[3])
            self.lista.append(nySpelare)
        fil.close()
        return self.lista
    
    def spara(self):
        fil = open(filnamn, 'w')
        for spelare in self.lista:
            fil.write('{}/{}/{}/{}'.format(spelare.namn,
                                           spelare.speladeMatcher,
                                           spelare.vunnaMatcher,
                                           spelare.vinstprocent))
            fil.close()          
    
    def väljSpelare(self):
        visaSpelare()
        spelareA = self.spelare[int(input('Första spelaren: '))-1]
        spelareB = self.spelare[int(input('Andra spelaren: '))-1]
        return spelareA, spelareB

    def visaSpelare(self):
        self.lista = sortera(self.lista)
        print('Plac\tNamn\tSpelade\tVunna\t%vunna')
        for spelare in self.lista:
            print('{}/{}/{}/{}/{}').format(i+1,
                                           spelare.namn,
                                           spelare.spelade,
                                           spelare.vunna,
                                           spelare.vinstprocent)
        
    def sortera(self, lista):
        return sorted(lista, key=lambda spelare:
                               spelare.vinstprocent,
                               reverse=True)
        
# -------------------------
# class Match
#   vinnare
#   spelare[]
#   bollar[]
#   games[]
#   sets[]
#   servar
#   fördel
#   printMode
#   
#   def spelaBollen()
#   def gePoäng()
#   def nyttGame()
#   def nyttSet()

class Match:
    def __init__(self, spelareA, spelareB):
        self.vinnare = None
        self.spelare = [spelareA, spelareB]
        self.bollar = [0,0]
        self.games = [0,0]
        self.sets = [0,0]
        self.servar = random.randrange(0,1)
        self.fördel = -1
        self.printMode = printMode

    def spelaBollen(self):
        print('{} servar bollen.'.format( self.spelare[self.servar] ))

        chans = random.randrange(1,100)/100

        if (float(self.spelare[self.servare].vinstprocent <= rand)):
            self.gePoäng(self.servare)
        else:
            self.gePoäng(invert(self.servare))

        if (self.printMode == 0):
            self.visaPoäng()

    def gePoäng(self, vannBoll):
        vinnarPoäng = self.bollar[vannBoll]
        förlorarPoäng = self.bollar[invert(vannBoll)]
        vinnarNamn = self.spelare[vannBoll]
        
        if (vinnarPoäng == 3):
            if (förlorarPoäng == 3):
                if (self.fördel == vannBoll):
                    self.nyttGame(vannBoll)
                else:
                    self.fördel = vannBoll
                    print('{} vann bollen'.format(vinnarNamn))
            else:
                self.nyttGame(vannBoll)
        else:
            vinnarPoäng += 1
            print('{} vann bollen'.format(vinnarNamn))

    def omvandlaPoäng(self, bollar):
        if (bollar == 0):
            return 0
        elif (bollar == 1):
            return 15
        elif (bollar == 2):
            return 30
        else:
            return 40

    visaPoäng(self):
        print('Namn\tPoäng\tGames\tSet')
        print('{}\t{}{}\t{}\t{}'.format(self.spelare[0].namn,
                                        self.poäng(self.bollar[0]),
                                        "+" if self.fördel == 0 else "",
                                        self.games[0], self.set[0]))
        print('{}\t{}{}\t{}\t{}'.format(self.spelare[1].namn,
                                        self.poäng(self.bollar[1]),
                                        "+" if self.fördel == 1 else "",
                                        self.games[1], self.set[1]))
    
    def nyttGame(self, vannBoll):
        self.games[vannBoll] += 1
        self.bollar = [0,0]
        self.servare = invert(self.servare)
        self.fördel = -1

        vinnarensGames = self.games[vannBoll]
        förlorarensGames = self.games[invert(vannBoll)]

        if (vinnarensGames > förlorarensGames + 1 and vinnarensGames >= 6):
            self.nyttSet(vannBoll)            
        else:
            print('{} vann gamet.'.format( self.spelare[vannBoll] ))
    
    def nyttSet(self, vannGame):
        self.sets[vannGame] += 1
        self.games = [0,0]

        if (self.set[0] + self.set[1] == 3):
            if (self.set[0] == 2 or self.set[0] == 3):
                self.vinnare = self.spelare[0]
            else:
                self.vinnare = self.spelare[1]

# -------------------------
# def
#   def invert()
#   def paus()

def invert(tal):
    if (tal == 0):
        return 1
    else:
        return 0

def paus():
    return

# -------------------------
# main
        
