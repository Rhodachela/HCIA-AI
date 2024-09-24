x = 20
y = 10

product = x * y
print(product)

count = 0
def increment():
    global count
    count +=1
    
increment()
print(count)

def outer_function ():
    x = 10

    def inner_function():
        nonlocal x
        x += 5
    inner_function()
    print("Modified value of x from inner function : ", x)
    
outer_function()


def greeting(name):
    print(f"Hello {name}")

greet = greeting("Jane")

def calculate_area(length, width):
    area = length * width
    return area

calculation = calculate_area(50, 100)
print(f"The area of the rectangle is: {calculation}")


def checker (number):
    if number %2 == 0:
        print(f"The number {number} is even")
    else:
        print("The number is odd")
checker(52)
