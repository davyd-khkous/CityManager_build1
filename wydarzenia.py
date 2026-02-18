import random
#wydarzenie suszy = - 20 jedzenie
def susza(city):
    city["Jedzenie"] -= 20
    if city["Jedzenie"] < 0:
        city["Jedzenie"] = 0
    return "Susza: stracono 20 jedzenia"

#wydarzenie powodzi(losowo rujnuje 1 losowy budynek jakiegokolwiek typu
def pawodz(city):
    budynki = city["Budynki"]
    wybrany = random.choice(list(budynki.keys()))
    if budynki[wybrany] > 0:
        budynki[wybrany] -= 1
        return f"Powódź zniszczyła: {wybrany}"
    else:
        return "Powódź nie wyrządziła szkód"

#wydarzenie ataku = -20 populacji oraz -30 pieniędzy
def atak(city):
    city["Populacja"] -= 20
    if city["Populacja"] < 0:
        city["Populacja"] = 0
    city["Pieniędze"] -= 30
    if city["Pieniędze"] < 0:
        city["Pieniędze"] = 0
    return "Atak: stracono 20 populacji i 30 pieniędzy"

#słownik dla wydarzeń(dla poprawnej pracy json)
event_map = {
    "susza": susza,
    "pawodz": pawodz,
    "atak": atak
}


#zaplanowanie losowe wydarzenia z trzech każde 7-21 dni
def planuj_wydarzenie(wydarzenia):
    dni = random.randint(7, 21)
    wydarzenia["dni_do_wydarzenia"] = dni
    wydarzenia["nadchodzace_wydarzenie"] = random.choice(list(event_map.keys()))
    wydarzenia["ostrzezenie"] = ""

#wprowadza zaplanowanie jeśli nie ma, zmnniejsza dzień do wydarzenia
def sprawdz_wydarzenie(wydarzenia, city):
    if wydarzenia["nadchodzace_wydarzenie"] is None:
        planuj_wydarzenie(wydarzenia)
        return None
    wydarzenia["dni_do_wydarzenia"] -= 1

#od pięciu dni przed wydarzeniem występuje osztrzeżenie
    if 0 < wydarzenia["dni_do_wydarzenia"] <= 5:
        wydarzenia["ostrzezenie"] = f"Wydarzenie nastąpi za {wydarzenia['dni_do_wydarzenia']} dni!"
        return None

#wywouje sie wydarzenie po nastąpinieniu terminu
    if wydarzenia["dni_do_wydarzenia"] <= 0:
        func_name = wydarzenia["nadchodzace_wydarzenie"]
        func = event_map[func_name]
        msg = func(city)

#reset po wyłołaniu
        wydarzenia["nadchodzace_wydarzenie"] = None
        wydarzenia["dni_do_wydarzenia"] = 0
        wydarzenia["ostrzezenie"] = ""
        return msg

    return None