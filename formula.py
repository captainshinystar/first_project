from ingredient_list import *
from ingredient import *

class Formula:
    def __init__(self, name, ingredients, amounts):
        self.name = name
        self.ingredients = ingredients
        self.amounts = amounts
    
    def check(self):
        invalid = 0
        for ingredient in self.ingredients:
            ingredient.update_status()
            if ingredient.status == Status.DEACTIVATED:
                invalid += 1
        if invalid > 0:
            return True
        else:
            return False

    def update(self):
        check1 = self.check()
        if check1 == False:
            return
        else:
            new_ingredients = []
            need_to_order = []
            no_subs = []
            for ingredient in self.ingredients:
                if ingredient.status == Status.ACTIVE:
                    new_ingredients.append(ingredient)
                else:
                    need_to_order.append(ingredient)
                    for ing in ing_list:
                        if (ingredient.form == Form.POWDER and ing.form == Form.POWDER) and (ingredient.name == ing.name):
                            ing.update_status()
                            if ing.status == Status.DEACTIVATED:
                                continue
                            else:
                                new_ingredients.append(ing)
                                break
                        elif (ingredient.form == Form.CREAM and ing.form == Form.CREAM) and (ingredient.type == ing.type):
                            ing.update_status()
                            if ing.status == Status.DEACTIVATED:
                                continue
                            else:
                                new_ingredients.append(ing)
                                break
                    no_subs.append(ingredient)
        self.ingredients = new_ingredients
        check2 = self.check()
        if check2 == True:
            print(f"No substitutions available for {no_subs}.\nCan't create new batch.\nNeed to order: {need_to_order}")
            return
        else:
            print(f"Formula updated. Need to order: {need_to_order}")
            return
