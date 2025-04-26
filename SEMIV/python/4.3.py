unit=int(input("enter units consumed:"))
bill=0
if unit<=10:
    print("zero bill amount")
elif unit<=110:
    bill=(unit-10)*5
    print(bill)
else:
    bill=(unit-10)*5+(unit-110)*10
    print(bill)
    
