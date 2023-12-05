class programExerciesGA:
    def __init__(self, food="", pounds=0):
        self.foodName = food
        self.amountOfFood = pounds
        self.standardPrice = 0
        self.__PriceListGA()
        self.calculatedPrice = self.costCalculationGA()

    def __PriceListGA(self):
        if self.foodName == "Dry Cured Iberian Ham":
            self.standardPrice = 177.80
        elif self.foodName == "Wagyu Steaks":
            self.standardPrice = 450.00
        elif self.foodName == "Matsutake Mushrooms":
            self.standardPrice = 272.00
        elif self.foodName == "Kopi Luwak Coffee":
            self.standardPrice = 306.50
        elif self.foodName == "Moose Cheese":
            self.standardPrice = 487.20
        elif self.foodName == "White Truffles":
            self.standardPrice = 3600.00
        elif self.foodName == "Blue Fin Tuna":
            self.standardPrice = 3603.00
        elif self.foodName == "Le Bonnotte Potatoes":
            self.standardPrice = 270.81
        else:
            self.standardPrice = 0.00
    def costCalculationGA(self):
        return self.standardPrice * self.amountOfFood
