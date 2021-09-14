
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
#   AND,  OR, NOT
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

# Not - example
# if applicant has good credit AND doesn't have criminal record
#   Eligible for loan

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print ("Eligible for loan")

# Comparison Operator
#   <,<=,>,>=,==,!=
# if temperature is greater than 30
#   it's a hot day
# otherwise if it's less than 10
#   it's a cold day
# otherwise
#   it's neither hot nor cold

temperature = 10

if temperature > 30:
    print("it's a hot day")
elif temperature<10:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")


# exercise

name="Salman"
length = len(name)
if length < 3:
    print("name must be atleast 3 char long")
elif length > 50:
    print("name can be a max of 50 characters")
else:
    print("name looks good!")


# exercise

#   Weight: 160  (input)
#   (L)bs or (K)g: l  (input)
#   You are 72.0 kilos

weight = input("Weight: ")
measurement_unit = input("(L)bs or (K)g: ")
if measurement_unit.lower() == 'l':
    weight_in_kilos = int(weight) * 0.45359237
    print(f"You are {weight_in_kilos} kilos")
else:
    weight_in_pounds = int(weight)/0.45
    print(f"You are {weight_in_pounds} pounds")