#define for easier math
#For this section, I will say I did use AI to simplify the math because I kept on writing similar calculations for each individual item. I asked AI to help me figure out what I could do in order to improve the math in my code, and that's when I found out about the `def` function, or `define`. It made it so much easier to be able to create all these different repetitive calculations in only a couple lines for each item instead of printing out the same math over and over again. I used the AI as ai learning aid, but I did make sure to review the code to make sure that I understood it. AI was only used for this particular section and in the other math parts, such as lines 41 through 47, but everything else is typed by myself. 

def item_total(price, quantity):
    """Returns the price multiplied by the quantity."""
    return price * quantity


def calculate_subtotal(*amounts):
    """Returns the total of all the item amounts added together."""
    return sum(amounts)


def calculate_discount(subtotal, discount_percent):
    """Returns the discount amount based on the subtotal and discount percent."""
    return subtotal * discount_percent / 100


def calculate_final_total(subtotal, discount_amount):
    """Returns the subtotal minus the discount amount."""
    return subtotal - discount_amount

#inputs for store info items and discount
store_name = input("Enter the store name: ")

item1_name = input("Enter the name of item 1: ")
item1_price = float(input(f"Enter the price of {item1_name}: "))
item1_quantity = int(input(f"Enter the quantity of {item1_name}: "))

item2_name = input("Enter the name of item 2: ")
item2_price = float(input(f"Enter the price of {item2_name}: "))
item2_quantity = int(input(f"Enter the quantity of {item2_name}: "))

item3_name = input("Enter the name of item 3: ")
item3_price = float(input(f"Enter the price of {item3_name}: "))
item3_quantity = int(input(f"Enter the quantity of {item3_name}: "))

discount_percent = float(input("Enter the discount percent (enter 0 for no discount): "))

#calculations for subtotal discount and total
item1_amount = item_total(item1_price, item1_quantity)
item2_amount = item_total(item2_price, item2_quantity)
item3_amount = item_total(item3_price, item3_quantity)

subtotal = calculate_subtotal(item1_amount, item2_amount, item3_amount)
discount_amount = calculate_discount(subtotal, discount_percent)
total = calculate_final_total(subtotal, discount_amount)

#bringing everything together into the recept
print()
print(store_name.upper())
print(f"{item1_name} x{item1_quantity}: ${item1_amount:.2f}")
print(f"{item2_name} x{item2_quantity}: ${item2_amount:.2f}")
print(f"{item3_name} x{item3_quantity}: ${item3_amount:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: ${discount_amount:.2f}")
print(f"Total: ${total:.2f}")

# 