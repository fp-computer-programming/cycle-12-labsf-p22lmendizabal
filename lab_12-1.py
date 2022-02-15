# author: LM (AMDG) 2/15/22
from fileinput import close


ofile = open('my_file.txt', "w")
ofile.write('LM 2/15/22 \n Hello World \n I have been playing soccer')
ofile.close()
