#printing values of a variable
"""a=1
a=2
b=2
print(b)"""

#printing only certain name
"""myname="My name is Karmistha Sthapit
#print(myname[28:0])"""

#printing opposite 
"""mystring="my name is Karmistha"
#print(mystring[::-1])"""

#list

#tuple
"""my_tuple=(
    'a',
    'b',
    324,
    2.2,
    [1,2,3,4],
    ('test,123')
)
print(my_tuple[4][2])
my_tuple[0] = "hello"
print(my_tuple)"""

#set (values cannot be repeated in set)
"""my_set={1,22,765,34,45,21}
print(type(my_set))
print(my_set)"""

#dictionary (single data)
"""person1={
    'name':'Shyam',
    'age':14,
    'gender':'male',
    'languages':[
        'python','java'
    ]
    
}
print(person1['languages'][0])
print(person1['languages'][0][::-1])"""

#dictionary (multiple data using list)
persons=[
    
    {'name':'Gita','age':20,'gender':'female','languages':['python','java']},
    
    {'name':'Shyam','age':14,'gender':'male','languages':['python','java']},
    
    {'name':'tom','age':30,'gender':'male','languages':['python','java']},
]

print(f"""
      My name is {persons[0]['name']}
      and age is {persons[0]['age']}
      and gender is {persons[0] ['gender']}
      and i know different languages like
      1. {persons[0]['languages'][0]}
      2. {persons[0]['languages'][1][1::]}
      """)

print(f"""
      My name is {persons[1]['name']}
      and age is {persons[1]['age']}
      and gender is {persons[1] ['gender']}
      and i know different languages like
      1. {persons[1]['languages'][0]}
      2. {persons[1]['languages'][1]}
      """)
