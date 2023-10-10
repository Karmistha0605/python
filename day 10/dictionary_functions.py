my_dictionary={'name':"Shyam",
                'id':"1254",
                'Address':"Tahachal"
    
}
my_other={'name':"Sam",
          'id':"1rwt4",
          'Address':"Thamel"
    
}
#returning keys of a dictionary
print(my_dictionary.keys())

#returning a list of values of a dictonary
print(my_dictionary.values())

#converting into a tuple
print(my_dictionary.items())

#Returning value associating with the key
print(my_dictionary.get('name', "nothing to display"))

#removing and returning the value associated with the key
my_dictionary.pop('id')
print(my_dictionary)

#updates key_value with another dictionary
my_dictionary.update(my_other)
print(my_dictionary)