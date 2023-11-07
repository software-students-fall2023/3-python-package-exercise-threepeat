import json
import random
import os
import six

def food(cuisine="French", price_range="medium", type="dinner"):
    if(not isinstance(cuisine, six.string_types) or not isinstance(price_range, six.string_types) or not isinstance(type, six.string_types)):
        return "Your filter is invalid. Try again."
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, '../data/food.json')
    with open(json_path, "r") as file:
        foods = json.load(file)

    filtered_foods = []
    for food in foods:
        cuisine_match = cuisine.lower() == food["cuisine"].lower()
        price_match = price_range.lower() == food["price_range"].lower()
        type_match = type.lower() == food["type"].lower()      
        if cuisine_match and price_match and type_match:
            filtered_foods.append(food)

    if filtered_foods:
        recommended_food = random.choice(filtered_foods)
    else:
        recommended_food = "No food meets your requirements. Try again."
    return recommended_food
