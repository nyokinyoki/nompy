# -*- coding: utf-8 -*-

import json

with open("ingredients.json", "r", encoding="utf-8") as json_data:
    ingredients = json.load(json_data)

with open("dishes.json", "r", encoding="utf-8") as json_data:
    dishes = json.load(json_data)

print(ingredients)
print(dishes)

print (dishes.keys)
print(list(ingredients.keys()))


class Ingredient:
    def __init__(self, name):
        self.name = name
        self.stats = {}
        for stat in list(ingredients[self.name].keys()):
            self.stats[stat] = ingredients[self.name][stat]

    def getStatsForNumOfUnits(self, units):
        self.multipliedIngredientStats = {}
        for statName in list(ingredients[self.name].keys()):
            if isinstance(self.stats[statName], str):
                # I'm a string, leave me alone!
                self.multipliedIngredientStats[statName] = self.stats[statName]
            else:
                self.multipliedIngredientStats[statName] = self.stats[statName] * units
        return self.multipliedIngredientStats


class Dish:
    def __init__(self, name):
        self.name = name
        self.dishStats = {}
        self.vars = [crispy, mleko]
        #for ingredient in self.vars:
        for ingredient in list(dishes[name].keys()):
            # Quantity is expressed as a number of "unit"s defined in ingredients.json
            # self.quantity = dishes[self.name][ingredient.name]
            self.quantity = dishes[self.name][ingredient]
            for stat in list(ingredients[ingredient].keys()):
                if isinstance(ingredients[ingredient][stat], str):
                    self.dishStats[stat] = ingredients[ingredient][stat]
                else:
                    if stat in self.dishStats:
                        # self.dishStats[stat] += ingredients[ingredient.name][stat] * self.quantity
                        self.dishStats[stat] += (ingredients[ingredient][stat] / ingredients[ingredient][
                            "amount"]) * self.quantity
                    else:
                        # self.dishStats[stat] = ingredients[ingredient.name][stat] * self.quantity
                        self.dishStats[stat] = (ingredients[ingredient][stat] / ingredients[ingredient][
                            "amount"]) * self.quantity

    def getStatsForNumOfDishes(self, units):
        self.multipliedDishStats = {}
        for statName in list(self.dishStats.keys()):
            if isinstance(self.dishStats[statName], str):
                # I'm a string, leave me alone!
                self.multipliedDishStats[statName] = self.dishStats[statName]
            else:
                self.multipliedDishStats[statName] = self.dishStats[statName] * units
        return self.multipliedDishStats

def getIngredientNames():
    return list(ingredients.keys())

def getDishNames():
    return list(dishes.keys())

def getMultipleDishStats(dishList):
    multipleDishObjects = {}
    multipleDishStats = {}
    # Don't override the key if the same dish is selected more than once
    for number, dishName in enumerate(dishList):
        if dishName in multipleDishObjects:
            multipleDishObjects[dishName + str(number)] = Dish(dishName)
        else:
            multipleDishObjects[dishName] = Dish(dishName)

    for dishName in list(multipleDishObjects.keys()):
        for statName in list(multipleDishObjects[dishName].dishStats.keys()):
            if isinstance(multipleDishObjects[dishName].dishStats[statName], str):
                multipleDishStats[statName] = multipleDishObjects[dishName].dishStats[statName]
            else:
                if statName in multipleDishStats:
                    multipleDishStats[statName] += multipleDishObjects[dishName].dishStats[statName]
                else:
                    multipleDishStats[statName] = multipleDishObjects[dishName].dishStats[statName]
    return multipleDishStats


ingredientDict = {}
ingredientDict["Crispy z ječmenovo vlaknino"] = Ingredient("Crispy z ječmenovo vlaknino")

crispy = Ingredient("Crispy z ječmenovo vlaknino")
mleko = Ingredient("Alpsko mleko (3,5)")
print(mleko)
# print(str(ingredients["Alpsko mleko (3,5)"]["calories"]) + " test printa calories")
# mlekokalorije = {}
# mlekokalorije["kcal"] = mleko.stats["calories"]
# print(mlekokalorije)
# mleko.getStatsForNumOfUnits["calories"](2)

kandm = Dish("Kosmiči z mlekom")

print(crispy.stats)
print(crispy.getStatsForNumOfUnits(2))
print(mleko.stats)
print(mleko.getStatsForNumOfUnits(2))
print("wait for it")
print(kandm.getStatsForNumOfDishes(2))
print(list(dishes["Palačinka z Nutello"].keys()))
dish = Dish("Palačinka z Nutello")
print(dish.dishStats)
#somanydishes = getMultipleDishStats(["Palačinka z Nutello", "Kosmiči z mlekom", "Cheese Chips (Chio)"])
somanydishes1 = getMultipleDishStats(["Palačinka z Nutello"])
somanydishes2 = getMultipleDishStats(["Palačinka z Nutello", "Palačinka z Nutello", "Palačinka z Nutello", "Palačinka z Nutello"])

print(somanydishes1)
print(somanydishes2)

