#for reusing codes
"""def hello_world():
    print('hello world')

hello_world()"""

#dynamic datas
"""def hello(name):
    print(f'hello {name}, how are you?')
hello("Ram")
hello("Shyam")"""

"""def hello(name,age,gender):
    print(f'hello {name}, how are you?, your age is {age}, gender is {gender}')
hello("Ram",gender='male',age=12)
hello("Shyam",gender='male',age=65)"""

#for loop in hobby
"""def info(name,hobbies):
    print(f'{name}',)
    for hobby in hobbies:
        print(hobby)
info("Sam",["art","dancing"])"""  

#args
def number(*numbers):
    print(numbers)
    
number(1,2,3,4,5,6,7)

def person(*name):
    for name in names:
        print(name)

person('ram','shyam','hari','krishna')








