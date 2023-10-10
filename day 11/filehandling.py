import os

import time

try:
    f=open("hello.txt",'a')
    for i in range(11):
        f.write(f"{i+1} hello apartment\n")
        f.close()
        time.sleep(5)
        os.remove('hello.txt')
       
except FileNotFoundError:
    print("File not Found")
#creating a file