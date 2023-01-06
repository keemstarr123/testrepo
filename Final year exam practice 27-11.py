heavy_users = 0
moderate_users = 0
water_usage = int(input("Please enter your water usage: "))

while water_usage != 0:
    price = 0
    if water_usage <= 100:
        price += 10
    elif water_usage <= 200:
        price = 10 + (water_usage-100)*0.5
    else:
        price = 10 + 0.5*100 + (water_usage-200) * 0.6
    print("Your water bill is RM:", price)
    if price <=80:
        moderate_users +=1
        print("You are moderate user.\n")
    else:
        heavy_users += 1
        print("You are heavy user.\n")
    water_usage = int(input("Please enter your water usage: "))



print("""
Summary Page
------------
""")
print("Number of heavy users:", heavy_users)
print("Number of moderate users:", moderate_users)

input("\nPress Enter to Escape")
