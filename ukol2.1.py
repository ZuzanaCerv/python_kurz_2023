#Sklad
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

print(sklad)

kod_soucastky = input("Zadej kod soucastky:")
pocet_ks = int(input("Zadej pocet ks:"))

if kod_soucastky not in sklad:
    print(f"Zadana soucastka {kod_soucastky}  neni skladem.")
else:
    if sklad[kod_soucastky]<pocet_ks:
        print(f"Lze prodat pouze omezene mnozstvi {sklad[kod_soucastky]} ks soucastky {kod_soucastky}")
        sklad.pop(kod_soucastky)
    else:
        print(f"Uvedene mnozstvi soucastky {kod_soucastky} mame skladem.")
        sklad[kod_soucastky] -=pocet_ks 

