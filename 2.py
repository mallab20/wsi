produkt = 'gra'
elementy = ['20 kart', 'pudełko']


#określenie czasu produkcji elementów
czas_gra = int(input("Czas produkcji gry (w tygodniach): "))
czas_opakowanie = int(input("Czas produkcji opakowania (w tygodniach): "))
czas_zestaw_kart = int(input("Czas produkcji zestawu kart (w tygodniach): "))
czas_karton = int(input("Czas produkcji kartonu (w tygodniach): "))
czas_plastik = int(input("Czas produkcji plastikowej części (w tygodniach): "))
#oreślenie startowej dostępności
dostepnosc_gra = int(input("Początkowa dostępność gry (w sztukach): "))
dostepnosc_opakowanie = int(input("Początkowa dostępność opakowań (w sztukach): "))
dostepnosc_zestaw_kart = int(input("Początkowa dostępność zestawów kart (w sztukach): "))
dostepnosc_karton = int(input("Początkowa dostępność kartonów (w sztukach): "))
dostepnosc_plastik = int(input("Początkowa dostępność plastikowych części (w sztukach): "))
#ilość produktów potrzebnych na wskazany dzień
ilosc = input("Podaj ilość gier, które potrzebujesz:")
dzien = input("Podaj nr tygodnia (1-10), na który je potrzebujesz: ")
#zależność w ilości między produktami różnych poziomów