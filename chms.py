import os,sys,time,datetime
from tkinter import messagebox as mgb
import si
class Installer(object):
    def __init__(self):
        self.propetiesL={'installerVersion':'1.0.0','installerType':'default(normal)'}
    def install(pkg):
        if pkg=='d-com':
            for i in range(101):
                print(' installing d-com:'+str(i*1)+'%',end='\r')
                time.sleep(0.1)
            global comIns
            comIns=True
            time.sleep(0.6)
            print('d-com Installed succssesfully.')
        else:
                        print('Invalid package')
            return('ErrorCode:404')
def linkWinMain():
    pass
def handle(command):
    cmds=command.split(' ')
    if command=='d-com':
        if comIns:
            print('_Dcom -com v1.0.0- v1.0.0')
        return None
    elif cmds[0]=='install':
        try:
            Installer.install(cmds[1])
        except IndexError:
            print('Invalid argumantation')
    elif command=='cls-Scr':
        os.system('cls')
    elif command=='?help':
        print('help comming soon,')
        print('for help,visit:https://rotf.lol/aaabb')
    elif command=='?web.site':
        print('https://web-pgau-vm.w3spaces.com')
    elif command=='ext':
        os.system('exit')
    else:
        print('invalid command or com file')  
while True:
    a=input("virtual(V):// ")
    try:
        handle(a)
    except NameError:
        print('_Dcom not installed,or a NameError happened.')
        time.sleep(0.5)