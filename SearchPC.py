import os
from sys import argv

print(argv)

searchStr = argv[2]

def searchDir(dirCurrent):

    try:
        flag1 = True
        try:
            main_directory = os.listdir(dirCurrent)
        except:
            print("Unable to list the directory:  " + dirCurrent)
            flag1 = False
            
        if (flag1 == True):
            for item in main_directory:

                item_path = os.path.join(dirCurrent, item)
                if os.path.isdir(item_path) == True:
                    searchDir(item_path)
                else: 
                    try:
                        f = open(item_path, 'r')
                        file_contents = f.read()
                        if searchStr in file_contents:
                            print("************************************************************************found in file " + item_path)     
                    except:
                        print("Unable to read file:  " + item_path)
    except:
        print("Unable to read files in the directory " + dirCurrent)
            
searchDir(argv[1])            