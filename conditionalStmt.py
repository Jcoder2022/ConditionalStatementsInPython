
# if it's hot
   #  It's a  hot day
   # Drink plenty of water
# otherwise if it's cold
    # It's a cold day
    # Wear warm clothes
# otherwise
   # It's a lovely day

weather = "cold"
is_hot = True
is_cold = True

if is_hot:
    print("It's a  hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

    # o/p will be following
    # It's a hot day
    # Drink plenty of water
print("---------------------------------------------------------")

if weather == "hot":
    print("It's a  hot day")
    print("Drink plenty of water")
elif weather == "cold":
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your Day")

    # o/p will be following
    # It's a cold day
    # Wear warm clothes
    # Enjoy your Day

print("---------------------------------------------------------")
is_hot = False
is_cold = False

if is_hot:
    print("It's a  hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")

    # o/p will be following
    # It's a lovely day

# Multiple Conditions
#   AND,  OR
# if applicant has high income AND good credit
#   Eligible for loan

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")


# if applicant has high income OR good credit
#   Eligible for loan

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")










