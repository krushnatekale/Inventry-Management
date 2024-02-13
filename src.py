import csv
import file as f
logged_in=False

def welcome():
    print('Welcome To Library')
    if(not(logged_in)):
        choice1()

def login():
    username=input('Enter Username : ')
    password=input('Enter Password')
    file=open('users.csv')

def register():
    file=open('users.csv','w',encoding='utf-8')
    d_file=csv.DictWriter(file,['Username','Password','Account_type'])
    username=input('Enter Username : ')
    password=input('Enter Password')
    acctype=input('Enter Account Type \n1.Admin \n2.User\n--->')
    d_file.writerow({f.header[0]:username,f.header[1]:password,f.header[2]:acctype})
    print('Registeration Successfull')

def choice1():
    print('Please Login Or Register........')
    print('Choose Any Option (Enter No Or Name Of The Operation)')
    print('1. Login')
    print('2. Register')
    inp=int(input('Enter Your Choice Here : ------> '))
    if inp==1:
        login()
    elif inp==2:
        register()
    else:
        print('Wrong Choice Please try Again.........')

welcome()
