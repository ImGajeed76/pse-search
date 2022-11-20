import json

from tqdm import tqdm

pse = {
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


def find_elements(text, found):
    if text == "":
        return found
    c1 = text[0]
    f1 = found.copy()
    for k, v in pse.items():
        if k.lower() == c1.lower():
            f1.append(v)
            f1 = find_elements(text[1:], f1)

    if len(text) < 1:
        return found
    c2 = text[0:2]
    f2 = found.copy()
    for k, v in pse.items():
        if k.lower() == c2.lower():
            f2.append(v)
            f2 = find_elements(text[2:], f2)

    if len(f1) > len(f2):
        return f1
    else:
        return f2


def elements_to_text(elements):
    out = ""
    for e in elements:
        out += str(list(pse.keys())[list(pse.values()).index(e)]) + " "
    return out


def console_run():
    with open('element_words_dictionary.json') as f:
        data = json.load(f)

    while True:
        text = input("Enter text to find elements: ").lower()
        print("Finding elements...", end="\r")
        if text in data.keys():
            f = str(data[text])
            print("Found word in data: " + f)
        else:
            found = find_elements(text.lower(), [])
            if len(text) == len(elements_to_text(found).replace(" ", "")) and len(found) > 0:
                print("Found elements: " + " ".join(found))
                if input("Would you like to save this word? (y/N) ") == "y":
                    data.update({text.lower(): " ".join(found)})
                    with open('element_words_dictionary.json', 'w') as f:
                        json.dump(data, f)
            else:
                print("No elements found")
        print("")


def add_if_not_in_dict(word, data):
    if word not in data.keys():
        found = find_elements(word, [])
        if len(word) == len(elements_to_text(found).replace(" ", "")) and len(found) > 0:
            data.update({word: " ".join(found)})
            print("Saving..", end="\r")
            with open('element_words_dictionary.json', 'w') as f:
                json.dump(data, f)
            print("Saved word: " + word)


def run_through_txt_file(path, encoding="utf-8"):
    with open('element_words_dictionary.json') as f:
        data = json.load(f)

    with open(path, encoding=encoding) as f:
        words = f.readlines()

    for word in tqdm(words):
        add_if_not_in_dict(word.lower(), data)


def run_through_json_file_keys(path, encoding="utf-8"):
    with open('element_words_dictionary.json') as f:
        data = json.load(f)

    with open(path, encoding=encoding) as f:
        words = json.load(f)

    for word in tqdm(words.keys()):
        add_if_not_in_dict(word.lower(), data)


if __name__ == '__main__':
    console_run()


