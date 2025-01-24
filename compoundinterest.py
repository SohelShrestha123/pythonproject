#compound interest calculator

p=0
t=0
r=0
n=100
while p<=0:
    p=float(input("Enter a principle: "))

    if p<=0:
        print("Principle can't be 0 or less than 0.")

while r<=0:
    r=float(input("Enter a rate: "))

    if r<=0:
        print("Rate can't be 0 or less than 0.")

while t<=0:
    t=int(input("Enter a time: "))

    if t<=0:
        print("Time can't be 0 or less than 0.")


amount=p*pow((1+r/n),t)

print(f"Your compound ineterst is Rs.{amount:.3f}")