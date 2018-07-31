import os, sys

replacement = sys.argv[3]
for dname, dirs, files in os.walk(sys.argv[1]):
    for fname in files:
        if (fname[-4:] == '.php'):
            try:
                fpath = os.path.join(dname, fname)
                with open(fpath, 'r') as f:
                    file_content = f.read()
                if "O_index.php" in file_content:
                    print(f.name)
                    file_content = file_content.replace(sys.argv[2], replacement)
                    with open(fpath, "w") as f:
                        f.write(file_content)
                f.close()
            except:
                print("Error in file: " +f.name)
