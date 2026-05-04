from csv import *
import csv
from helper import *
from presentatie import *

  
 
inkomsten = {
    "aardbeien-ijs-totaal" : "1000",
    "vanille-ijs-totaal" : "2000",
    "chocolade-ijs-totaal" : "1500",
    "waterijsjes-totaal" : "750"}

presenteer(inkomsten, totaal=som(inkomsten))    
print("===========================")  
print(f"totaal : {som(inkomsten)} euro")   


with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key, value]) 
    
