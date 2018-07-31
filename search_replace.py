import os, sys

replacement = sys.argv[2]
for dname, dirs, files in os.walk("/var/www/html/vice_dev"):
    for fname in files:
        if (fname[-4:] == '.php'):
            try:
                fpath = os.path.join(dname, fname)
                with open(fpath, 'r') as f:
                    file_content = f.read()
                if "O_index.php" in file_content:
                    print(f.name)
                    file_content = file_content.replace(sys.argv[1], replacement)
                    with open(fpath, "w") as f:
                        f.write(file_content)
                f.close()
            except:
                print("Error in file: " +f.name)
#        fpath = os.path.join(dname, fname)
#        with open(fpath) as f:
#            s = f.read()
#        s = s.replace("O_index.php", replacement)
#        with open(fpath, "w") as f:
#            f.write(s)