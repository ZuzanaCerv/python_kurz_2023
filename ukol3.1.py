
import json

hodnoceni = []

with open("body.json", mode="r", encoding="utf-8") as file:
    vysledky = (json.load(file))
    print(vysledky)

for jmeno, cislo in vysledky.items():
    if cislo >= 60:
        print(f"{jmeno}: PASS")
    else:
        print(f"{jmeno}: FAIL")

print(hodnoceni)

with open("hodnoceni.json", "w") as outfile:
    json.dump(hodnoceni, outfile, ensure_ascii=False, indent=4)






