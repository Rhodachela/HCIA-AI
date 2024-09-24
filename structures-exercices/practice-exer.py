favorite_fruits = ["Pineaples", "Melon", "Apples", "Bananas"]
print(favorite_fruits[1])

favorite_fruits = ["Pineaples", "Melon", "Apples", "Bananas"]
favorite_fruits.insert(0, "Mango")
print(favorite_fruits)

my_dict = {
    "book" : "It Ends with Us",
    "author" : "Colleen Hoover",
    "genre" : "Romance"
}

print(my_dict["genre"])

drinks = {
    "soda" : "Fanta Orange",
    "water" : "Keringet",
    "milk" : "Mount Kenya",
    "cocktail" : "tequila Rose",
    "yorghut" : "Vanilla"
}
print(drinks["cocktail"])


import random
random_numbers = [random.randint(1, 10) for i in range (10)]

unique_numbers = set(random_numbers)

print("randoms numbers: ", random_numbers)
print("Unique numbers (after removing duplicates) : ", unique_numbers)