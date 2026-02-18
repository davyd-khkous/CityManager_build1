#funkcja produkująca 10 jedzenia na każdą farmę
def produkcja_jedzenia(city):
    ilość_farm = city["Budynki"]["Farmy"]
    produkcja = ilość_farm * 10
    city["Jedzenie"] += produkcja

#użytek jedzenie 1 na 1 osobę oraz zmniejszenie szczęścia jeśli nie wystarcza
def użytek_jedzenia(city):
    populacja = city["Populacja"]
    city["Jedzenie"] -= populacja
    if city["Jedzenie"] < 0:
        city["Szczęście"] -= 5
        city["Jedzenie"] = 0

#funkcja pojemności budynku
POJEMNOŚĆ_BUDYNKU = 5
def pojemność_budynku(city):
    budynki = city["Budynki"]["Budynki 1 LVL"]
    pojemnosc = budynki * POJEMNOŚĆ_BUDYNKU
    return pojemnosc

#funkcja zmniejsza szczęście jeśli nie wystarcza pojemności budynku oraz jeśli nie ma jedzenia
def update_szczescia(city):
    pojemnosc = pojemność_budynku(city)
    if city["Populacja"] > pojemnosc:
        city["Szczęście"] -= 2.5
    if city["Jedzenie"] == 0:
        city["Szczęście"] -= 5

#ograniczanie szczęścia nie mniej niż 0 i nie więcej niż 100
def ogranicz_szczescie(city):
    if city["Szczęście"] > 100:
        city["Szczęście"] = 100
    elif city["Szczęście"] < 0:
        city["Szczęście"] = 0

#zwiększenie populacji jesli szczęście wiecej niż 80 i wystarcza pojemności
#zwiększenie populacji jesli jedzenie więcej niz populacji na 5 i wystarcza pojemności
#zmniejszenie populacji jesli mniej niz 30 szczęścia
#zmniejszenie szczęścia jeśli jedzenie = 0
def update_populacji(city):
    max_pojemnosc = pojemność_budynku(city)
    if city["Szczęście"] > 80 and city["Populacja"] < max_pojemnosc:
        city["Populacja"] += 1
    if city["Jedzenie"] >= city["Populacja"] + 5 and city["Populacja"] < max_pojemnosc:
        city["Populacja"] += 1
    if city["Szczęście"] < 30 and city["Populacja"] > 0:
        city["Populacja"] -= 1
    if city["Jedzenie"] == 0 and city["Populacja"] > 0:
        city["Populacja"] -= 1

#budowanie farmy - produkuje jedzenie
def zbudowac_farme(city):
    koszt = 30
    if city["Pieniędze"] >= koszt:
        city["Budynki"]["Farmy"] += 1
        city["Pieniędze"] -= koszt
        return "Zbudowano Farme!"
    else:
        return "Nie wystarcza pieniędzy"

#budowanie budynku - produkuje pojemność
def zbudowac_bydynekl1(city):
    koszt = 20
    if city["Pieniędze"] >= koszt:
        city["Budynki"]["Budynki 1 LVL"] += 1
        city["Pieniędze"] -= koszt
        return "Zbudowano Bydynek 1 LVl!"
    else:
        return "Nie wystarcza pieniędzy"

#budowanie kopalni - produkuje pieniądze
def zbudować_kopalnię(city):
    koszt = 40
    if city["Pieniędze"] >= koszt:
        city["Budynki"]["Kopalnia"] += 1
        city["Pieniędze"] -= koszt
        return "Zbudowano kopalnię!"
    else:
        return "Nie wystarcza pieniędzy"

#produkcja jedzenie przez kopalni
def produkcja_kosztów(city):
    ilość_kopalni = city["Budynki"]["Kopalnia"]
    produkcja = ilość_kopalni * 0.5
    city["Pieniędze"] += produkcja