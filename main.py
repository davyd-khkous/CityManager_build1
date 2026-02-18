from processes import produkcja_jedzenia, użytek_jedzenia, update_szczescia, ogranicz_szczescie, update_populacji, produkcja_kosztów
from city import pokaz_miasto
#głowna funckja miasta - jeden dzień (oraz pokaz w konsoli stanu gry, dla testowania bez GUI)
def jeden_dzien(city):
    produkcja_jedzenia(city)
    użytek_jedzenia(city)
    update_szczescia(city)
    ogranicz_szczescie(city)
    update_populacji(city)
    produkcja_kosztów(city)
    city["Dzień"] += 1
    pokaz_miasto(city)