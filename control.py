import tkinter as tk
from tkinter import messagebox
from main import jeden_dzien
from city import stworczyć_miasto
from wydarzenia import sprawdz_wydarzenie
from processes import (zbudowac_farme,zbudowac_bydynekl1,zbudować_kopalnię)
from zachowanie import zapisz_gre_json, wczytaj_gre_json
#funkcji stworzenia słowniku nadaje sie zmienna
city = stworczyć_miasto()

#stworzenie korzenego okna tkinter z nazwą, rozmiarem, oraz brakiem możliwości zmiany okna
root = tk.Tk()
root.title("City Manager")
root.geometry("320x420")
root.resizable(False, False)

#stworzenie widgetu miasta w korzenym oknie
miasto_label = tk.Label(root,text="",justify="left",anchor="w",font=("Courier", 10))
miasto_label.pack(padx=10, pady=10, fill="x")

#stworzenie widgetu informacji o np. tym, ze zostalo zbudowane, w korzenym oknie
info_label = tk.Label(
    root,
    text="",
    fg="blue",
    font=("Arial", 9)
)
info_label.pack(pady=5)


#funkcaja aktualizacji miasta oraz przypisania
def aktualizuj_miasto():
    budynki_text = ""
    for nazwa, liczba in city["Budynki"].items():
        budynki_text += f"  {nazwa}: {liczba}\n"

    text = (
        f"Dzień: {city['Dzień']}\n"
        f"Pieniędze: {city['Pieniędze']}\n"
        f"Populacja: {city['Populacja']}\n"
        f"Jedzenie: {city['Jedzenie']}\n"
        f"Szczęście: {city['Szczęście']}\n\n"
        f"Budynki:\n{budynki_text}"
    )

    miasto_label.config(text=text)

#funkcja budowy farmy oraz aktualizacji(jest potrzebna dla nacisku)
def zbuduj_farme():
    msg = zbudowac_farme(city)
    info_label.config(text=msg)
    aktualizuj_miasto()

#funkcja budowy kopalni oraz aktualizacji(jest potrzebna dla nacisku)
def zbuduj_kopalnie():
    msg = zbudować_kopalnię(city)
    info_label.config(text=msg)
    aktualizuj_miasto()

#funkcja budowy budynku oraz aktualizacji(jest potrzebna dla nacisku)
def zbuduj_budynek():
    msg = zbudowac_bydynekl1(city)
    info_label.config(text=msg)
    aktualizuj_miasto()

#funkcja przegrania jeśli populacja 0 lub szczęście 0 oraz pokazu ze przegrałesz
def przegranie(city):
    aktualizuj_miasto()
    if city["Populacja"] == 0:
        tk.messagebox.showinfo("Koniec gry", "Populacja spadła do 0! Przegrałeś!")
        root.destroy()
    elif city["Szczęście"] == 0:
        tk.messagebox.showinfo("Koniec gry", "Szczęście spadło do 0! Przegrałeś!")
        root.destroy()


#słownik wydarzeń do funkcji planuj_wydarzenia
wydarzenia = {
    "nadchodzace_wydarzenie": None,
    "dni_do_wydarzenia": 0,
    "ostrzezenie": ""}

#funkcja aktualizacji oraz wyłowania funkcji jednego dnia
def nastepny_dzien():
    jeden_dzien(city)
    msg = sprawdz_wydarzenie(wydarzenia, city)
    aktualizuj_miasto()
#dodanie wizualnego ostrzeżenia(dotyczy osztrzeżenia o wydarzeniach)
    if msg:
        info_label.config(text=msg)
    elif wydarzenia.get("ostrzezenie"):
        info_label.config(text=wydarzenia["ostrzezenie"])
    else:
        info_label.config(text="")
#sprawdzanie czy nie przegrałesz
    przegranie(city)

#nowy widget( w przyszłości do zachowania lub wczytania)
top_frame = tk.Frame(root)
top_frame.pack(side="top", anchor="ne", padx=10, pady=5)

#naciski zachowania oraz wczytania w widgecie top_frame)
tk.Button(top_frame, text="💾 Zapisz",command=lambda: zapisz_gre_json(city, wydarzenia), width=8).pack(side="left", padx=2)
tk.Button(top_frame, text="📂 Wczytaj",command=lambda: wczytaj_gre_json(city, wydarzenia), width=8).pack(side="left", padx=2)


#naciski do grania w głownym oknie
tk.Button(root,text="Zbuduj Farmę (30)", command=zbuduj_farme).pack(fill="x", padx=20, pady=5)
tk.Button(root,text="Zbuduj Kopalnię (40)",command=zbuduj_kopalnie).pack(fill="x", padx=20, pady=5)
tk.Button(root,text="Zbuduj Budynek LVL1 (20)",command=zbuduj_budynek).pack(fill="x", padx=20, pady=5)
tk.Button(root,text="Następny dzień",command=nastepny_dzien).pack(fill="x", padx=20, pady=10)
tk.Button(root,text="Wyjście", command=root.destroy).pack(fill="x", padx=20, pady=10)

#wyłowanie funkcji aktualizacji miasta, głownego ciągu gry oraz określenie że plik jest scryptem a nie modułem(wiem, ze nie obowiązkowe)
aktualizuj_miasto()
root.mainloop()