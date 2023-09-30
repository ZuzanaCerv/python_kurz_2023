jmeno_email = "Zuzana"
print(jmeno_email +"@czechitas.cz")


jmeno_a_prijmeni = input("Zadej jméno a příjmení: ")
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())


jmeno_list = jmeno_a_prijmeni.split(" ") # list retezcu
jmeno = jmeno_list[0]
prijmeni = jmeno_list[1]
print(jmeno[0] + ". " + prijmeni[0] + ".")

if len(jmeno) > 5:
    print(jmeno[0] + ". " + prijmeni)
else:
    print(jmeno_a_prijmeni)








