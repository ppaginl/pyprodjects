items = ["pencil", "ereser", "notebook", "sharpener"]
stock_count = [10, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(items, stock_count)}
print("Full inventory", inventory)

in_stock_items = [item for item in items if inventory[item] > 0]
print("items in stock:", in_stock_items)

chosen_item = input("which itemdi you want to buy?")

if chosen_item not in inventory or inventory [chosen_item] == 0:
 
 print(chosen_item, "is out of stock! stopping the checker.") 
 exit()

prices = [10, 5, 40, 15, 20]
markup = int(input(" enter the markup amount to add to every price :" ))
mark_up_prices = list (map(lambda p:p + markup, prices))
print("marked up prices", mark_up_prices)