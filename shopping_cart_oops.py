class ShoppingCart:
    def __init__(self,fruits,veggies,cookies,cake,chocolate,juice):
        self.fruits=fruits
        self.veggies=veggies
        self.cookies=cookies
        self.cake=cake
        self.chocolate=chocolate
        self.juice=juice
    
    def add(self,brownie):
        self.brownie=brownie
        print("Added item:",self.brownie)


