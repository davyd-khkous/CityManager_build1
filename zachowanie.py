from tkinter import filedialog
import json
#funkcj zachowanie słowników miasta oraz wydarzeń(event_map oraz wydarzenia były stworzone by przekształcił funkcje w słowniku na str
def zapisz_gre_json(city, wydarzenia):
    filename = filedialog.asksaveasfilename(defaultextension=".json",
                                            filetypes=[("JSON files", "*.json")])
    if filename:
        with open(filename, "w") as f:
            json.dump({"city": city, "wydarzenia": wydarzenia}, f)

#funkcja wczytania zachowań
def wczytaj_gre_json(city, wydarzenia):
    from tkinter import filedialog
    import json

    filename = filedialog.askopenfilename(defaultextension=".json",
                                          filetypes=[("JSON files", "*.json")])
    if filename:
        with open(filename, "r") as f:
            data = json.load(f)
            city.update(data["city"])
            wydarzenia.update(data["wydarzenia"])
