import csv
import StringDisplay as sd

us=''

def viewbooks():
    sd.display('-------------------------- Books --------------------------\n\n')
    with open('books.csv',encoding='utf-8') as f:
        file=csv.reader(f)
        for i in file:
            if i==['']:
                continue
            for j in i:
                print(j,end='  |  ')
            print()
    print('\n\n')
    home(us)



def addbook():
    sd.display('--------------------- Add Book ---------------------\n')
    id=input('Enter Book Id : ')
    name=input('Enter Book Name : ')
    author=input('Enter Author Name : ')
    date=input('Enter Published Date : ')
    price=input('Enter Price : ')
    copies=input('Enter No. of Copies : ')

    if id=='' or name=='' or author=='' or date=='' or price=='' or copies=='':
        sd.display('Please Enter All Details Of Book\n')
        addbook()
        exit(0)
    with open('books.csv','a',encoding='utf-8') as f:
        file=csv.writer(f)
        file.writerow([id,name,author,date,price,copies])
        f.close()
    print('\n\n')
    home(us)


def home(user):
    us=user
    print('Hello ',user)
    string='Welcome To Admin Page,\nChoose Any Option\n' \
           '1. View Books\n2. Add Books\n'
    sd.display(string)
    inp=int(input('Enter Your Choice'))
    if(inp==1):
        viewbooks()
    elif inp==2:
        addbook()
