import random

count = input("Words to generate(number): ")
count = int(count)
structure = input("Word-structure (X  for consonant, Y for consonant or nothing, O for vocal, Q for vocal or nothing, I for both, T for both or nothing and any non-letter stays):")



vocals = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
both = vocals + consonants

while(True):
    for j in range(count):
        out = ""
        for i in range(len(structure)):
            if structure[i] == "X":
                out += random.choice(consonants)
            elif structure[i] == "Y":
                out += random.choice([random.choice(consonants),""])
            elif structure[i] == "O":
                out += random.choice(vocals)
            elif structure[i] == "Q":
                out += random.choice([random.choice(vocals),""])
            elif structure[i] == "I":
                out += random.choice(both)
            elif structure[i] == "T":
                out += random.choice([random.choice(both),""])
            else:
                out += structure[i]
        print(out)
    input("Press something to continue:")