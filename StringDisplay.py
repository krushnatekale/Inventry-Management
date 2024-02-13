import time

def display(string):
    for i in string:
        time.sleep(0.001)
        print(i,end='')
