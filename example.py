from pydate import activity, food, dessert, pickupline

def main():
    print("Welcome to the PyDate!")
    
    while True:
        print("\nSelect an option:")
        print("1. Food Recommendation")
        print("2. Activity Recommendation")
        print("3. Dessert Recommendation")
        print("4. Pick Up Line")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            cuisine = input("Enter cuisine preference: ")
            price_range = input("Enter price range preference: ")
            meal_type = input("Enter meal type preference: ")
            recommended_food = food(cuisine, price_range, meal_type)
            print("\nRecommended Food:")
            print(recommended_food)
        elif choice == "2":
            indoor = input("Indoor activity? (True/False): ").lower() == "true"
            time = input("Enter preferred time: ")
            recommended_activity = activity(indoor, time)
            print("\nRecommended Activity:")
            print(recommended_activity)
        elif choice == "3":
            dessert_type = input("Enter dessert type: ")
            dessert_price = input("Enter dessert price: ")
            recommended_dessert = dessert(dessert_type, dessert_price)
            print("\nRecommended Dessert:")
            print(recommended_dessert)
        elif choice == "4":
            text_type = input("Do you want a text-based pick-up line? (True/False): ").lower() == "true"
            category = input("Enter pick-up line category: ")
            recommended_line = pickupline(text_type, category)
            print("\nRecommended Pick Up Line:")
            print(recommended_line)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()