cost=int(input("Enter the cost of bike:"))
if cost>100000:
    print("Tax=15%")
elif cost>50000 and cost<=100000:
    print("Tax=10%")
else:
    print("Tax=5%")