#py2代码
fileNames = ['1.py', 'index.html', 'jiji.php', 'lian.java', 'rhel.cpp', 'word.docx', 'cf.xlsx']


for tempName in fileNames:
    position = tempName.rfind('.')
    print tempName[position:]

print "-----------------------------------"

i = 0
length = len(fileNames)
while i < length:
    tempName = fileNames[i]
    position = tempName.rfind('.')
    print tempName[position:]
    i +=