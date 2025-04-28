grocery_prices = {
    'mango' : 20,
    'milk' : 26,
    'banana' : 10,
    'bread' : 50,
    }
grocery_quantities = {
    'mango' : 10,
    'milk' : 2,
    'banana' : 6,
    'bread' : 3,
    }

bill = 0
for item in grocery_prices:
    if item in grocery_quantities:
        bill += grocery_prices[item] * grocery_quantities[item]

print("total bill: ", bill)
