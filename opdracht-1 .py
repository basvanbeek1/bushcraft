# afstand van de reis 244km
# auto gebruikt 1 liter op de 12km
# 1,67 per liter
# 8 eu per p voor koffie 

Diesel = 1.67
AfstandReis = 244 
AutoVerbruik = 244/12
PerPersoon = 8
HeenEnTerugWeg = (AutoVerbruik + AutoVerbruik)
afronden_op_aantal_decimalen = 2
antwoord = round( AutoVerbruik, afronden_op_aantal_decimalen )

print("Voor de heen en terug reis verbruik je " +  str(antwoord) + (" Liter"))
print("Voor de heen en terugweg betaal je aan benzine " + str(antwoord + Diesel) + (" Euro"))
pri



