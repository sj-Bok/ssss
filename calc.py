# get two integer parameters
# return sum
def plus(x, y):
    return x+y
def minus(x,y):
    return x-y
def gob(x,y):
    return x*y
def mod(x,y):
    return x/y

# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus 2:minus 3:gob 4:mod")
        check = int(input())
        if check == 1:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", plus(x,y))

        if check == 2:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", minus(x,y))

        if check == 3:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", gob(x,y))
        
        if check == 4:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            print("answer : ", mod(x,y))
            
        elif check > 4:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
