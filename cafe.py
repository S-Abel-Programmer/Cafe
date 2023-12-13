''' Create a cafe menu with 4 items, then show stock values 
    / retail values to gain total stock worth'''
best_cafe = "Stephen's Cafe of Wonders"


menu = ["Hot Drinks", "Muffins", "Paninis", "Ice Creams"]  # Items for sale

stock = {"Hot Drinks": 1000,            # each item held in stock values
         "Muffins": 500,
         "Paninis": 500,
         "Ice Creams": 500 }

price = {"Hot Drinks": 2,               # retail selling price per item
         "Muffins": 1.50,
         "Paninis": 2.50,
         "Ice Creams": 2 }


values = sum(stock.values()) * sum(price.values())      # calculation for stock * selling price

print("Welcome to " + best_cafe + "\n")
for key in stock:
    print("You have " + key + " to sell and have ",
           stock[key], "in stock")     # how to pull the information from dictionary with no [] or ,
print("")

for key in price:
    print("Using you current selling price of " + key + " at £",
           price[key])
print("")

print("Your total stock valuation using the retail selling price is: £",int(values), "\n")
print("SELL AS MANY AS YOU CAN, soon you will be a Millionaire :-)")          # fingers crossed :-)
