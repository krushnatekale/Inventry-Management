import csv
import adminHome
import userHome
import StringDisplay as sd

def login():
    with open('users.csv',encoding='utf-8') as f:
        file=csv.reader(f)

        username=input('Enter Username : ---> ')
        password=input('Enter Password : ---> ')
        if(username=='' or password==''):
            sd.display('Please Enter All Details')
            login()
        log_in=False
        for row in file:
            if(row[0].lower() == username.lower() and row[1] == password):
                sd.display('Login Successfull\n\n\n')

                if row[2].lower()=='admin':
                    adminHome.home(row[0])
                    exit(0)
                elif row[2].lower()=='user':
                    userHome.home(row[0])
                    exit(0)
                else:
                    sd.display('There Might be an Issue, Please Contact It Service....')
                log_in=True
                break
        if(log_in==False):
            sd.display('Login Unsuccessfull')
            sd.display('Please Try Again\n\n')
            login()
