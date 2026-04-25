from algemene_functies import mijn_functie2 


def aanbieding_01():
    a = "aardbei"
    b = "van 4 euro"
    c = "naar 3.60 euro"
    return a, b, c
print("vandaag in de aanbieding: emmertje ijs (1 liter)" + aanbieding_01()[0] + " " + aanbieding_01()[1] + " " + aanbieding_01()[2]) 




def inkomsten_totaal():
    inkomsten_totaal = [220, 430, 125, 160, 205, 90, 345]
    return sum(inkomsten_totaal)
def btw():
    return inkomsten_totaal() / 100 * 9
print("het totaal van alle inkomsten van deze week is " + str(inkomsten_totaal()) + "euro, waarover" + str(btw()) + "euro aan btw betaald moet worden") 


def laag_en_hoog():
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    a = min(inkomsten)
    b = max(inkomsten)
    return a, b
print(laag_en_hoog()) 

def gemiddelde():
    inkomsten = [220, 430, 125, 160, 205, 90, 345]
    return sum(inkomsten) / len(inkomsten)
print("de gemiddelde inkomsten van deze week zijn " + str(gemiddelde()) + "euro") 


def meervoudig():
    invoer_lijst = [10, 5 , 3, 2, 1, 2, 9]
    laag_en_hoog = min(invoer_lijst), max(invoer_lijst)
    return laag_en_hoog
print(meervoudig()) 


def combinatie(invoer_lijst_2):
   def laag_en_hoog(invoerlijst): 
       return min(invoerlijst), max(invoerlijst)
   korte_lijst = laag_en_hoog(invoer_lijst_2)
   return mijn_functie2(korte_lijst[0], korte_lijst[1])
print(combinatie([10, 5 , 3, 2, 1, 2, 9])) 
   