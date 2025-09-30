groceries = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2
}
cart = []
while True : 
    ask = input("what do want to buy ? (write done to finish shopping)")
    if ask == "done" : 
        break
    elif ask in groceries:
     cart.append(ask)
    else :
     print("Sorry, we don’t have that item.")
        