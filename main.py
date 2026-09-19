""" 
Kirjutame koos programmi, mis küsib kasutajalt, mis päev on homme (tööpäev või puhkepäev), ning väljastab vastuse põhjal sobiva sõnumi. 
Kasutaja sisestab ühe sõna:
"tööpäev!
või "puhkepäev". 
Kui sisestus on "tööpäev", siis kuvatakse ekraanile tekst:
 Ma lähen magama, head ööd!
Kui sisestus on "puhkepäev": kuvatakse ekraanile tekst:
 Veel üks osa Netflixist!
"""
#Alusta programmi.
#Küsi kasutajalt, "Mis päev on homme? (tööpäev/puhkepäev)".
#Salvesta vastus muutujasse day.
#Kui day on võrdne sõnaga "tööpäev", siis väljasta ekraanile: "Ma lähen magama, head ööd!".
#Muidu, kui day on võrdne sõnaga "puhkepäev", siis väljasta ekraanile: "Veel üks osa Netflixist!".
#Muidu (kui sisestus ei olnud õige), sis väljasta ekraanile "Vale väärtus".
#Lõpeta programm.



""" 
day = input("Mis päev on homme? (tööpäev/puhkepäev):")

if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist!")
else:
    print("Vale väärtus") 
"""


#Finantsnõustaja
""" Sa tahad osta endale uue iPhone 17 Pro, aga sa oled otsustanud, et krediiti sa ei võta. Selle asemel oled sa palganud range ja vastutustundliku finantsnõustaja programmi kujul.
See programm:
- Küsib, kui palju sul praegu raha,
- võrdleb seda iPhone 17 Pro hinnaga (näiteks 2 500 eurot),
- ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse. """

""" print("Tere tulemast programmi 'Finantsnõustaja'!")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")

money = int(input("Kui palju sul praegu raha on?"))

if money < 2500:
    print("Sul pole piisavalt raha iPhone 17 Pro ostmiseks. Soovitan sul säästa rohkem raha.")
elif money == 2500:
    print("Sul on täpselt piisavalt raha iPhone 17 Pro ostmiseks. Kui oled kindel, et see on vajalik, võid selle osta.")
else:
    print("Saad osta iPhone 17 Pro ja veel jääb raha üle.") """

#Sammulugeja
""" Sul on eesmärk teha iga päev vähemalt 10 000 sammu. Programm küsib kasutajalt, mitu sammu ta täna tegi, arvutab täitmise protsenti ja annab talle tagasisidet.
- Kui protsent on <50: "Alles poolel teel, aga ära anna alla!"
- Kui protsent on <75: "Hea töö, aga saad veel paremaks!"
- Kui protsent on >=100: "Suurepärane! Sa oled oma eesmärgi täitnud!"" 
"""

""" goal = 10000
steps = int(input("Mitu sammu sa täna tegid?"))

percent = (steps/goal) * 100

print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, anna alla!")
elif percent < 75:
    print("Hea töö, aga saad veel paremaks!")
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Suurepärane! Sa oled oma eesmärgi täitnud!") """

