""" Arstid soovitavad juua päevas 2 liitrit vett.
Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.

#Alusta programmi
#Programm arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
- Kui protsent on <50: väljasta: "Joo rohkem vett, keha vajab seda!"
- Kui protsent on <100: väljasta: "Tubli, jätka samas vaimus!"
- Kui protsent on >=100: väljasta: "Suurepärane, sa oled oma päevase eesmärgi täitnud!"
 """

#Alusta programmi
#Küsi kasutajalt, mitu klaasi vett ta juba joonud on.
#Salvesta vastus muutujasse glasses.
#Arvuta, mitu protsenti päevanormist on täidetud (1 klaas = 250 ml, päevanorm = 2 liitrit).
#Salvesta protsent muutujasse percent.
#Kui percent on <50, siis väljasta ekraanile: "Joo rohkem vett, keha vajab seda!".
#Muidu, kui percent on <100, siis väljasta ekraanile: "Tubli, jätka samas vaimus!".
#Muidu (kui percent on >=100), siis väljasta ekraanile: "Suurepärane, sa oled oma päevase eesmärgi täitnud!"
#Lõpeta programm.

""" goal = 2000
glasses = int(input("Mitu klaasi vett sa juba joonud oled?"))
total_intake = glasses * 250
percent = (total_intake / goal) * 100

if percent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, sa oled oma päevase eesmärgi täitnud!") """