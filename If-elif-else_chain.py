age = 19

if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $25")
else:
    print("Your addmission cost is $40")

# more concise version

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
# adding a sceoned efli block
elif age < 65:
    price = 40
else:       # catchall ( anything els is this)
    price = 20 # changed form 40 to 20
print(f"Your admission cost is ${price}.")

# omitting the els block


age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

