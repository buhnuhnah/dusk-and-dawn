file = open("rest.txt")
c = ""
index = 0

# hero = input("Hero scene? (y/n) ")
# if(hero == "y"):
#     hero = True
# else:
#     hero = False

hero = False


characters = {"Rene" : "r", "Samuel" : "s", "Alicia" : "a", "Bastion" : "ba", "Mia" : "m", "Aunt" : "am", "Matilda" : "am", "Magno" : "ma", "Levina" : "l"}
heroes = {"Rene" : "b", "Samuel" : "sh", "Alicia" : "f", "Bastion" : "st", "Mia" : "m", "Aunt" : "am", "Matilda" : "am", "Magno" : "ma", "Snapshot" : "sn"}

print()
for line in file:
    if(line[0] == "["):
        for x in line[1:]:
            index += 1
            if x == "]":
                index +=2
                break
            c = c + x

        if(c[:3].upper() == "SFX"):
            print("# " + c)
        else:
            c = c.split(" ")[0]
            if(c in characters.keys()):
                if(hero):
                    print(heroes[c], line[index:-1])
                else:
                    print(characters[c], line[index:-1])
            else:
                print("\"" + c + "\" " + line[index:-1])

        c = ""
        index = 0

    else:
        print("\"" + line[:-1] + "\"")
print()
