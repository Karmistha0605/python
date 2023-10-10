#ask user list of  fruit and store it in list
f1=input("Enter your first fruit:")
f2=input("Enter your second fruit:")
f3=input("Enter your third fruit:")
f4=input("Enter your fourth fruit:")
f5=input("Enter your fifth fruit:")
f6=input("Enter your sixth fruit:")

fruits=(f1, f2, f3, f4, f5, f6)
print(fruits)

#ask user email and password and store in list in dictionary format
my_list=[]
while True:
    email=input("Enter user's email")
    password=input("Enter user's password")
    my_dictionary=[{'email':email,
               'pass':password
    
}]
    my_list.append(my_dictionary)
    print(my_list)


