print("Ein Spiel, in dem du ein Zahl zwischen 0 und 100 erraten musst:")
# ein randum, die ganze Zahlen zwischen 0 und 100 generiert
import random
obere_Grenze = 100; untere_Grenze = 0        # Grenze einfügen
# wenn ein print gegeben dann sieht man den gewürfelte Zahl
gewürfelte_Zahl = random.randint(untere_Grenze , obere_Grenze)
# Ein_Zahl=None um den while schleife immer den input drückt bis das Ziel
Ein_Zahl = None
Zähler= 0                                        # um den Zähler der Schleife zu darstellen
gewinn_Versuch = 3
while  Ein_Zahl != gewürfelte_Zahl:
    Ein_Zahl = int(input("Bitte geben Sie Ihre Zahl von 0 bis 100 : "))
    if  gewürfelte_Zahl == Ein_Zahl:
        print("yaaaah, Ihre Zahl ist die richtige Zahl, :) Herzlichen Glückwunsch")
    elif gewürfelte_Zahl< Ein_Zahl:
        print("Ihre Zahl ist größer als die richtige Zahl")
        Zähler = Zähler + 1
    else:
        print("Ihre Zahl ist kleiner als die richtige Zahl ): ")
        Zähler = Zähler + 1
print(" Sie haben " + str(Zähler) + " Versuche benötigt")

if Zähler <= gewinn_Versuch:
    print("Sie haben 100$ gewonnen vom Automat")
else:
    print("Versuchen Sie bitte mit weniger als " + str(gewinn_Versuch) + " Versuchen um Geld zu erhalten")
