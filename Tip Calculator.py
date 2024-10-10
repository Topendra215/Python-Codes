
print("Welcome to the tip calculator!")
Bill=float(input("The amount of bill :"))
percent=float(input("What Percentage of Bill you wanna tip: "))
amount_of_tip=float(Bill*(percent/100))

Total_Bill=(Bill + amount_of_tip)

person=int(input("Bill to be divided among how many person: "))
one_person_bill=float(Total_Bill/person)
round_off_bill=round(one_person_bill,2)
print(f"One Person should have to pay {round_off_bill}$")
