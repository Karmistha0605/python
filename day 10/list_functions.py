#adding data to the list
my_list=[2,3,4,1,6]
my_list.append(10)
print(my_list)

#appending multiple datas from one list to another
list_2 =[5,6,7,8]
my_list.extend(list_2)
print(my_list)

#appends multiple elements that are iterable
my_list.insert(2,87)
print(my_list)

#removing the 1st occurence of an element
my_list.remove(5)
print(my_list)

#removes a specific index
my_list.pop(0)
print(my_list)

#returing index of the first occurence of a element
print(my_list.index(4))


#sorting list in ascending order
my_list.sort()
print(my_list)

# #reversing the order of elements
my_list.reverse()
print(my_list)



