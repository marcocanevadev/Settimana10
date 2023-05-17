class Pizza:

    pizzarecipes = {'margherita':['pomodoro','mozzarella','basilico'],'diavola':['pomodoro','mozzarella','salamepicc']}
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
            return Pizza(cls.pizzarecipes[[k for k, v in cls.pizzarecipes.items() if v == recipe]])
        except:
            raise ValueError

    def __str__(self):
        return f'Delicious Bessa {self._ingredients!s}'
    
    

if __name__ == '__main__':
    negro = Pizza(['pomodoro', 'basilico', 'mozzarella'])
