spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    food_names = []
    for spicy_food in spicy_foods:
        food_names.append(spicy_food["name"])
    return food_names

def get_spiciest_foods(spicy_foods):
    heat_over_5 = []
    for heat in spicy_foods:
        if heat["heat_level"] > 5:
            heat_over_5.append(heat)
    return heat_over_5

def print_spicy_foods(spicy_foods):
    for heat in spicy_foods:
        name = heat["name"]
        cuisine = heat["cuisine"]
        total_peppers = heat["heat_level"] * "🌶"
        print(f"{name} ({cuisine}) | Heat Level: {total_peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for cuisines in spicy_foods:
        if cuisine == cuisines["cuisine"]:
            return cuisines

def print_spiciest_foods(spicy_foods):
    heat_over_5 = []
    for heat in spicy_foods:
        name = heat["name"]
        cuisine = heat["cuisine"]
        if heat["heat_level"] > 5:
            heat_over_5.append(heat)
            total_peppers = heat["heat_level"] * "🌶"
            print(f"{name} ({cuisine}) | Heat Level: {total_peppers}")

def get_average_heat_level(spicy_foods):
    nums = [heat["heat_level"] for heat in spicy_foods]
        
    average = sum(nums) / len(nums)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
