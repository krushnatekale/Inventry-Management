import csv
import time
import login
import StringDisplay as sd

def register():
    with open('users.csv','a',encoding='utf-8') as f:
        file=csv.writer(f)
        user=input('Enter Username : ---> ')
        password=input('Enter Password : ---> ')
        acctype=input('Enter Account type (Admin,User) : ---> ')
        if(user=='' or password=='' or acctype==''):
            sd.display('Please Enter All Data...\nTry Again\n')
            register()
            exit(0)
        file.writerow([user,password,acctype])
        sd.display('Registration Successfull\nPlease Try Logging In\n')
        login.login()
        exit(0)
