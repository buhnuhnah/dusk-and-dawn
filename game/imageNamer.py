import os

def main():
    characters = ['alicia', 'aunt matilda', 'bastion', 'magno', 'mia', 'rene', 'samuel', 'snapshot']

    for c in characters:
        folder = c + "/"
        for image in os.listdir(c):
            newName = folder + image
            newName = newName.replace("super alicia", "frostbite")
            newName = newName.replace("super bastion", "stoneman")
            newName = newName.replace("super rene", "bolt")
            newName = newName.replace("super samuel", "shadow")
            newName = newName.replace("casual ", "")
            os.rename(folder + image, newName.lower())
main()
