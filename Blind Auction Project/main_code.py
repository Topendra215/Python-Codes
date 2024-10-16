import art
print(art.logo)
bid_total={}
bid_price=[]
bid_again=True
while bid_again:
    name=input("Enter your name:\n")
    price=int(input("Enter your bid price:\n"))
    bid_price.append(price)

    bid_total[name]=price
    new_bid=input("Is there any more bidder, Enter yes or No: ").lower()

    if new_bid=="yes":
        bid_again=True
        print("\n"*20)
    elif new_bid=="no":
        bid_again=False

print(f"The Highest bidder is {max(bid_total,key=bid_total.get)} with the bid price of ${max(bid_price)}")
