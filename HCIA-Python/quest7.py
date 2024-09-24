food = input("Enter your food choice: ").lower()
drink = input("Enter your preferred drink: ").lower()

match food:
    case ("pizza"):
        print(f"{drink} and {food} is the best combo.")
    case ("ugali"):
        print(f"I'd recommend taking this with Mursik.")
    case ("rice"):
        print("Ensure you take water afterwards")
    case _:
        print("You should enter a proper meal")