import csv

# header=['Username','Password','Account_Type']
# with open('users.csv','w',encoding='utf-8') as file_w:
#     file=csv.DictWriter(file_w,['Username','Password','Account_Type'])
#     file.writeheader()
#     file.writerow({header[0]:'krushna',header[1]:'Pass@123',header[2]:'Admin'})

with open('books.csv','w',encoding='utf-8') as f:
    file=csv.writer(f)
    file.writerow(['Book_id','Book_Name','Author','Published_In','Price','Copies'])
