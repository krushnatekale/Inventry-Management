import time
import StringDisplay as sd
import login
import os
import register
logged_in=False

def welcome():
    st='Hello,\nWelcome To Library\nPlease Choose Any Option to Continue\n1. Login\n2.Register\n'
    sd.display(st)
    inp=None
    try:
        inp=int(input(':-----> '))
    except (Exception):
        welcome()
    if(inp==1):
        login.login()
        exit(0)
    elif(inp==2):
        register.register()
        exit(0)
    else:
        sd.display('Entered Wrong Choice')
        welcome()
        exit()
welcome()
