from ingredient_list import *

class Formula:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.invalid = []
    

    def get_ingredients(self):
        return self.ingredients
    
    def check(self):
        for ingredient in self.ingredients:
            if ingredient.status == Status.DEACTIVATED:
                self.invalid.append(ingredient)
            if ingredient.boh <= 0:
                self.invalid.append(ingredient)
        if self.invalid != []:
            return True
        else:
            return False

    def update(self):
        if self.check == True:
            for ingredient in self.ingedients:
                if ingredient.active == False:
                    
