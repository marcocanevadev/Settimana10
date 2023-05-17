class Pizza:

    pizzarecipes = {'margherita':['mozzarella','pomodoro','basilico'],'diavola':['mozzarella','pomodoro','salamepicc']}
    
    def __init__(self, ingredients):
        self._ingredients = ingredients
        
    @classmethod
    def getIngredients(cls, recipe):
        try :
            return cls.pizzarecipes.get(recipe)
        except Exception:
            raise ValueError
    @classmethod
    def fromRecipe(cls, recipe):
        try:
            return Pizza(recipe)
        except:
            raise ValueError

    def __str__(self):
        return f'Delicious {[k for k, v in self.pizzarecipes.items() if set(v) == set(self._ingredients)]} Bessa made with: {self._ingredients!s}'
    
    

if __name__ == '__main__':
    pizza = Pizza(['pomodoro', 'mozzarella', 'basilico'])
    print(pizza)
    ingredienti = Pizza.getIngredients('margherita') 
    ingre2 = pizza.getIngredients('diavola')
    print(ingredienti)
    print(ingre2)
    p2 = Pizza.fromRecipe(ingredienti)
    p3 = pizza.fromRecipe(ingre2)
    print(p2)
    print(p3)