mum = "Josephine"

def work():
    mum = "Rose"

    def home():
        mum = "Shosh"
        print(f"The home name is {mum}")
    home()
    print(f"The mother's name at home is {mum}")
work()
print(f"The work mum is called {mum}")
