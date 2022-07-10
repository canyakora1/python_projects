#                           Welcome to the Konoba Burristo Game:


import time


print("Welcome to Konoba Nigeria Limited\n")
name = input("Can I have your name, please?\n")
time.sleep(2)

if name == "Ben":
    evil_status = input("Are you evil? ")
    if evil_status == "Yes":
        print("You owe us money from last year and the year before, so get out now!!!!!!")
        exit()
    else:
        print("I must have mistaken you for an evil Ben")
        time.sleep(2)
else:
    print("You may go in and have your seat and one of our waiters could assist you")

print("Welcome " + name + ", We are at your service.\n")
menu = ("Egusi Soup, Okra Soup, Pepper Soup, Snail Soup, Black soup")

print("Mr " + name + ", we have different orders for your eating pleasure. Kindly choose one\n" + menu)
order = input()

# To set the prices for the menu items ******* Work-In-Progress

if menu == "Egusi Soup":
    price = 10
elif menu == "Okra Soup":
    price = 9
elif menu == "Pepper Soup":
    price = 11.50
elif menu == "Snail Soup":
    price = 15
elif menu == "Black Soup":
    price = 12
#else:
    #print("We dont have that on the menu for today")
    #exit()
print("Thanks " + name + ", your " + order + " would be ready in ten miuntes\n")
time.sleep(2)
drinks = "Coke, Sprite, Gingerale, Fanta, Lemon, Krest\n"
print("Do you want some drinks to go with your " + order + "?, we have\n" + drinks)
order2=input()
time.sleep(3)
print("Thanks " + name + ", your " + order + ", with " + order2 + ", will be ready in just a minute. Thanks for waiting\n")
time.sleep(2)
price_order = 11
price_order1 = 4
print("How much order are you placing today?\n")
no_order = input()
time.sleep(3)
total_price = (price_order + price_order1) * int(no_order)

print("Total price for your orders today is " + str(total_price) + " dollars")
