import glob
import os

def renpyImageCreation(directory_dir, file):
    f = open(file, "w")
    for characterFolder in directory_dir:
        for i in os.listdir(characterFolder):
            f.write("image " + i[:-4] + " = \"" + characterFolder + "/"+ i + "\"\n")
        f.write("\n")
    f.close()

def main():
    #dir_list = ["*", "*/", "*/*/"]
    dir_list = ['aunt matilda', 'backgrounds', 'magno', 'mia', 'snapshot', "alicia", "bastion", "rene", "samuel"]
    folder = "image_directory.rpy"

    renpyImageCreation(dir_list, folder)

main()
