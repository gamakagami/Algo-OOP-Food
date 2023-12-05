from programexercise import programExerciesGA

def addToCartGA():
    Foods = []
    numOfFoods = int(input("How many items will you order today? "))

    while numOfFoods<1:
        print("Number of items must be at least 1")
        numOfFoods = int(input("How many items will you order today? "))

    for i in range(numOfFoods):

        print(f"Item #{i+1}-")

        nameOfFood = input("Enter food name: ").title()

        foodAmount = float(input("Enter amount of pounds: "))

        while foodAmount <= 0 :
            foodAmount = float(input("Enter amount of pounds (Number must be greater than 0): "))

        Foods.append(programExerciesGA(nameOfFood, foodAmount))
    
    return Foods
def shoppingCartGA(listOfFood):
    print("Here's a summary of the items purchased:")
    print("---------------------------")
    
    for foodData in listOfFood:


        print(f"Item: {foodData.foodName}")
        print(f"Amount ordered: {foodData.amountOfFood} lbs")

        standardPrice = "{:.2f}".format(foodData.standardPrice)
        print(f"Price per pound: ${standardPrice}")

        calculatedPrice = "{:.2f}".format(foodData.calculatedPrice)
        print(f"Price of order: ${calculatedPrice}")
        print(" ")
     
def totalCostCalculatorGA(listOfFood):
    totalPrice = 0

    for foodData in listOfFood:
        totalPrice += foodData.calculatedPrice
        totalPriceRounded = "{:.2f}".format(totalPrice)
    print(f"Total cost: ${totalPriceRounded}")
def startFunctionGA():
    Food = addToCartGA()
    shoppingCartGA(Food)
    totalCostCalculatorGA(Food)

startFunctionGA()
