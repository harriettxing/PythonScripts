# To run:
# python ListCommitFilesBySearchStr.py ~search string~

import subprocess, os
from sys        import argv


grepStr = '--grep=' + argv[ 1 ]
print(grepStr)
p1 = subprocess.Popen([ 'git', 'log', '--all', '--pretty=format:"%H"', grepStr ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


fileList =[]

while True:
    line = p1.stdout.readline()
    if line != b'':
#        print(line.rstrip())
        hash = line.rstrip()[1:-1]
        hashStr = hash.decode("utf-8")
        print(hashStr)
        
        c2 = ['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', hashStr]

        p2 = subprocess.Popen(c2, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        while True:
            line2 = p2.stdout.read()
            if line2 != b'':
                fileName = line2.strip()
                fileNameStr = fileName.decode("utf-8")
                a = fileNameStr.split('\n')
                #print(a)
                fileList += a
            else:
                break
                
    else:
        break

# fileList = ['aa', 'bb', 'cc', 'AA', 'BB', 'CC']
fileList.sort() 
fileList2 = sorted(fileList)
i = 0
while i < len(fileList2):
    print(fileList2[i])
    i = i + 1

print("Total number of files: "+ str(len(fileList)))        
      
