import json

from tqdm import tqdm

pse_english = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Boron",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Ne": "Neon",
    "Na": "Sodium",
    "Mg": "Magnesium",
    "Al": "Aluminium",
    "Si": "Silicon",
    "P": "Phosphorus",
    "S": "Sulfur",
    "Cl": "Chlorine",
    "Ar": "Argon",
    "K": "Potassium",
    "Ca": "Calcium",
    "Sc": "Scandium",
    "Ti": "Titanium",
    "V": "Vanadium",
    "Cr": "Chromium",
    "Mn": "Manganese",
    "Fe": "Iron",
    "Co": "Cobalt",
    "Ni": "Nickel",
    "Cu": "Copper",
    "Zn": "Zinc",
    "Ga": "Gallium",
    "Ge": "Germanium",
    "As": "Arsenic",
    "Se": "Selenium",
    "Br": "Bromine",
    "Kr": "Krypton",
    "Rb": "Rubidium",
    "Sr": "Strontium",
    "Y": "Yttrium",
    "Zr": "Zirconium",
    "Nb": "Niobium",
    "Mo": "Molybdenum",
    "Tc": "Technetium",
    "Ru": "Ruthenium",
    "Rh": "Rhodium",
    "Pd": "Palladium",
    "Ag": "Silver",
    "Cd": "Cadmium",
    "In": "Indium",
    "Sn": "Tin",
    "Sb": "Antimony",
    "Te": "Tellurium",
    "I": "Iodine",
    "Xe": "Xenon",
    "Cs": "Caesium",
    "Ba": "Barium",
    "La": "Lanthanum",
    "Hf": "Hafnium",
    "Ta": "Tantalum",
    "W": "Tungsten",
    "Re": "Rhenium",
    "Os": "Osmium",
    "Ir": "Iridium",
    "Pt": "Platinum",
    "Au": "Gold",
    "Hg": "Mercury",
    "Tl": "Thallium",
    "Pb": "Lead",
    "Bi": "Bismuth",
    "Po": "Polonium",
    "At": "Astatine",
    "Rn": "Radon",
    "Fr": "Francium",
    "Ra": "Radium",
    "Ac": "Actinium",
    "Rf": "Rutherfordium",
    "Db": "Dubnium",
    "Sg": "Seaborgium",
    "Bh": "Bohrium",
    "Hs": "Hassium",
    "Mt": "Meitnerium",
    "Ds": "Darmstadtium",
    "Rg": "Roentgenium",
    "Cn": "Copernicium",
    "Nh": "Nihonium",
    "Fl": "Flerovium",
    "Mc": "Moscovium",
    "Lv": "Livermorium",
    "Ts": "Tennessine",
    "Og": "Oganesson",
    "La": "Lanthanum",
    "Ce": "Cerium",
    "Pr": "Praseodymium",
    "Nd": "Neodymium",
    "Pm": "Promethium",
    "Sm": "Samarium",
    "Eu": "Europium",
    "Gd": "Gadolinium",
    "Tb": "Terbium",
    "Dy": "Dysprosium",
    "Ho": "Holmium",
    "Er": "Erbium",
    "Tm": "Thulium",
    "Yb": "Ytterbium",
    "Lu": "Lutetium",
    "Ac": "Actinium",
    "Th": "Thorium",
    "Pa": "Protactinium",
    "U": "Uranium",
    "Np": "Neptunium",
    "Pu": "Plutonium",
    "Am": "Americium",
    "Cm": "Curium",
    "Bk": "Berkelium",
    "Cf": "Californium",
    "Es": "Einsteinium",
    "Fm": "Fermium",
    "Md": "Mendelevium",
    "No": "Nobelium",
    "Lr": "Lawrencium"
}

pse_german = {
    "H": "Wasserstoff",
    "He": "Helium",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Bor",
    "C": "Kohlenstoff",
    "N": "Stickstoff",
    "O": "Sauerstoff",
    "F": "Fluor",
    "Ne": "Neon",
    "Na": "Natrium",
    "Mg": "Magnesium",
    "Al": "Aluminium",
    "Si": "Silicium",
    "P": "Phosphor",
    "S": "Schwefel",
    "Cl": "Chlor",
    "Ar": "Argon",
    "K": "Kalium",
    "Ca": "Kalzium",
    "Sc": "Scandium",
    "Ti": "Titan",
    "V": "Vanadium",
    "Cr": "Chrom",
    "Mn": "Mangan",
    "Fe": "Eisen",
    "Co": "Cobalt",
    "Ni": "Nickel",
    "Cu": "Kupfer",
    "Zn": "Zink",
    "Ga": "Gallium",
    "Ge": "Germanium",
    "As": "Arsen",
    "Se": "Selen",
    "Br": "Brom",
    "Kr": "Krypton",
    "Rb": "Rubidium",
    "Sr": "Strontium",
    "Y": "Yttrium",
    "Zr": "Zirkonium",
    "Nb": "Niob",
    "Mo": "Molybdän",
    "Tc": "Technetium",
    "Ru": "Ruthenium",
    "Rh": "Rhodium",
    "Pd": "Palladium",
    "Ag": "Silber",
    "Cd": "Cadmium",
    "In": "Indium",
    "Sn": "Zinn",
    "Sb": "Antimon",
    "Te": "Tellur",
    "I": "Jod",
    "Xe": "Xenon",
    "Cs": "Caesium",
    "Ba": "Barium",
    "La": "Lanthan",
    "Hf": "Hafnium",
    "Ta": "Tantal",
    "W": "Wolfram",
    "Re": "Rhenium",
    "Os": "Osmium",
    "Ir": "Iridium",
    "Pt": "Platin",
    "Au": "Gold",
    "Hg": "Quecksilber",
    "Tl": "Thallium",
    "Pb": "Blei",
    "Bi": "Bismut",
    "Po": "Polonium",
    "At": "Astat",
    "Rn": "Radon",
    "Fr": "Francium",
    "Ra": "Radium",
    "Ac": "Actinium",
    "Rf": "Rutherfordium",
    "Db": "Dubnium",
    "Sg": "Seaborgium",
    "Bh": "Bohrium",
    "Hs": "Hassium",
    "Mt": "Meitnerium",
    "Ds": "Darmstadtium",
    "Rg": "Roentgenium",
    "Cn": "Copernicium",
    "Nh": "Nihonium",
    "Fl": "Flerovium",
    "Mc": "Moscovium",
    "Lv": "Livermorium",
    "Ts": "Tennessine",
    "Og": "Oganesson",
    "La": "Lanthan",
    "Ce": "Cer",
    "Pr": "Praseodym",
    "Nd": "Neodym",
    "Pm": "Promethium",
    "Sm": "Samarium",
    "Eu": "Europium",
    "Gd": "Gadolinium",
    "Tb": "Terbium",
    "Dy": "Dysprosium",
    "Ho": "Holmium",
    "Er": "Erbium",
    "Tm": "Thulium",
    "Yb": "Ytterbium",
    "Lu": "Lutetium",
    "Ac": "Actinium",
    "Th": "Thorium",
    "Pa": "Protactinium",
    "U": "Uran",
    "Np": "Neptunium",
    "Pu": "Plutonium",
    "Am": "Americium",
    "Cm": "Curium",
    "Bk": "Berkelium",
    "Cf": "Californium",
    "Es": "Einsteinium",
    "Fm": "Fermium",
    "Md": "Mendelevium",
    "No": "Nobelium",
    "Lr": "Lawrencium"
}


def find_elements(text, found, pse):
    if text == "":
        return found
    c1 = text[0]
    f1 = found.copy()
    for k, v in pse.items():
        if k.lower() == c1.lower():
            f1.append(v)
            f1 = find_elements(text[1:], f1, pse)

    if len(text) < 1:
        return found
    c2 = text[0:2]
    f2 = found.copy()
    for k, v in pse.items():
        if k.lower() == c2.lower():
            f2.append(v)
            f2 = find_elements(text[2:], f2, pse)

    if len(f1) > len(f2):
        return f1
    else:
        return f2


def elements_to_text(elements, pse):
    out = ""
    for e in elements:
        out += str(list(pse.keys())[list(pse.values()).index(str(e).title())])
    return out


def console_run(pse, dict_path='element_words_dictionary.json'):
    data = load_data(dict_path)

    while True:
        text = input("Enter text to find elements: ").lower()
        print("Finding elements...", end="\r")
        if text in data.keys():
            f = str(data[text])
            print("Found word in data: " + f)
        else:
            found = find_elements(text.lower(), [], pse)
            if len(text) == len(elements_to_text(found, pse)) and len(found) > 0:
                print("Found elements: " + " ".join(found))
                if input("Would you like to save this word? (y/N) ") == "y":
                    data.update({text.lower(): " ".join(found)})
                    save_data(data, dict_path)
            else:
                print("No elements found")
        print("")


def save_data(data, path='element_words_dictionary.json', log=True):
    if data != {}:
        if log:
            print("Saving..", end="\r")
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f)
        if log:
            print("Saved dict")


def load_data(path='element_words_dictionary.json'):
    with open(path, 'r', encoding="utf-8") as f:
        f.read()
        if f.read() == "" or f.read() == "{}":
            data = {}
        else:
            data = json.load(f)
    return data


def add_if_not_in_dict(word, data, pse):
    if word.lower() not in data.keys():
        found = find_elements(word.lower(), [], pse)
        if len(word.lower()) == len(elements_to_text(found, pse)) and len(found) > 0:
            data.update({word.lower(): " ".join(found)})


def run_through_txt_file(path, pse, dict_path='element_words_dictionary.json', encoding="utf-8"):
    data = load_data(dict_path)

    with open(path, encoding=encoding) as f:
        words = f.read().split("\n")

    for word in tqdm(words):
        add_if_not_in_dict(word.lower(), data, pse)

    save_data(data, dict_path)


def run_through_json_file_keys(path, pse, dict_path='element_words_dictionary.json', encoding="utf-8"):
    data = load_data(dict_path)

    with open(path, encoding=encoding) as f:
        words = json.load(f)

    for word in tqdm(words.keys()):
        add_if_not_in_dict(word.lower(), data, pse)

    save_data(data, dict_path)


if __name__ == '__main__':
    run_through_txt_file("english_words.txt", pse_german, "element_words_dictionary_german.json", "utf-8")
