while True:
    try:
        a=int(input('First number'))
        b=int(input('Second number'))
        print(a<b)
        if a<10:
            raise Exception("First number should always be greater then b")
        print(a/b)
        
    except ZeroDivisionError:
        print("Zero number cannot be divided")
    
    except ValueError:
        print("invalid input")
        
    except:
        print("something went wrong!!, Please try Again")
        
        
   