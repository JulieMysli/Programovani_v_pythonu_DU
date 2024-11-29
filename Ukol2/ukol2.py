import requests
import json


# # ČÁST 1

# OŠETŘENÍ VSTUPU OD UŽIVATELE
while True:
    ico = input("Zadej IČO subjektu, o kterém chceš získat informace:")
    if ico.isdigit() and len(ico) == 8:
        break
    else:
        print("Zadaná hodnota není správná. IČO má přesně 8 číslic.")

# ZADÁNÍ URL ADRESY SE VSTUPEM OD UŽIVATELE
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO"
url = url.replace("ICO", ico)

# STAŽENÍ DAT Z INTERNETU
response = requests.get(url)
data = response.json()

# PŘEVEDENÍ DAT NA JSON
with open("subject.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False)

# VYPSÁNÍ JMÉNA SUBJEKTU A ADRESY
with open("subject.json", encoding="utf-8") as file:
    subject = json.load(file)

if "obchodniJmeno" not in subject:
    print("Zadané IČO nebylo nalezeno.")
else:
    print(subject["obchodniJmeno"])
    print(subject["sidlo"]["textovaAdresa"])



# ČÁST 2

# VSTUP OD UŽIVATELE
subject_name = input("Zadej název subjektu, který chceš vyhledat: ")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

# ODESLÁNÍ REQUESTU S POŽADAVKEM POST
data = f'{{"obchodniJmeno": "{subject_name}"}}'
res = requests.post(
    "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", 
    headers=headers, 
    data=data
)

# POČET NALEZENÝCH SUBJEKTŮ
response_data = res.json()
if "pocetCelkem" in response_data:
    total_number = response_data["pocetCelkem"]
    print(f"Nalezeno subjektů: {total_number}")

    # VYPSÁNÍ SUBJEKTŮ
    economic_subjects = response_data["ekonomickeSubjekty"]
    if economic_subjects:
        for subject in economic_subjects:
            obchodni_jmeno = subject["obchodniJmeno"]
            ico_spolecnosti = subject["ico"]
            print(f"{obchodni_jmeno}, {ico_spolecnosti}")
    else:
        print("Žádné subjekty nebyly nalezeny.")
else:
    print("Výsledek obsahuje příliš mnoho subjektů.")


