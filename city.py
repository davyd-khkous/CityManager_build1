#stworzenie głownego słownika
def stworczyć_miasto():
    return {
        "Dzień": 0,
        "Pieniędze": 100,
        "Populacja": 10,
        "Jedzenie": 10,
        "Szczęście": 50,
        "Budynki": {
            "Farmy": 1,
            "Budynki 1 LVL": 2,
            "Kopalnia" : 0
        }
    }

#funkcja pokazu miasta(dla konsoli)
def pokaz_miasto(city):
        print(f"Dzień: {city['Dzień']}")
        print(f"Pieniędze: {city['Pieniędze']}")
        print(f"Populacja: {city['Populacja']}")
        print(f"Jedzenie: {city['Jedzenie']}")
        print(f"Szczęście: {city['Szczęście']}")
        print("Budynki:")
        for nazwa, liczba in city["Budynki"].items():
            print(f"  {nazwa}: {liczba}")