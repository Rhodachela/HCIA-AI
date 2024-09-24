count = 10

def outer_function():
    count = 5
    
    def inner_function():
        count = 2
        print(f"Inner function: {count}")
    
    inner_function()
    print(f"Outer function:{count}")
    
print(f"Global scope:{count}")
outer_function()