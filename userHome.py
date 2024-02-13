import StringDisplay as sd
import csv
user=''
def viewbooks():
    sd.display('-------------------------- Books --------------------------\n\n')
    with open('books.csv',encoding='utf-8') as f:
        file=csv.reader(f)
        for i in file:
            if i==['']:
                continue
            for j in i:
                print(j,end='  ')
            # print()
    print('\n\n')
    home(user)


def reservebook():
    pass


def home(us):
    user=us
    sd.display(f'Hello {us},\nWelcome To Library Inventry System\n'
               'Please Choose Any Option From Below\n'
               '1. View Books\n'
               '2. Reserve Book\n')
    inp=None
    try:
        inp=int(input('Enter Your Choice : '))
    except (Exception):
        sd.display('Please Enter Correct Choice\n\n')
        home(user)
    if inp == 1:
        viewbooks()
    elif inp ==2:
        reservebook()
    else:
        sd.display('Invalid Input\nPlease Try Again\n')
        home(user)
        exit(0)
