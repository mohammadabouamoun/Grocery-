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

print("You bought:", cart)
total = 0 
for item in cart:
   total += groceries[item]
print("Total = $" + str(total))   
if total > 10:
    print("You spent a lot!")
else:
    print("You spent a little!")       