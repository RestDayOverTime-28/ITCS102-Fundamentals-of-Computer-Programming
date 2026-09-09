# Global Freight Calculator

# BASE VARIABLE INPUTS
senderName = str(input("Input <Sender Name> ---> "))
typeofItem = str(input("Input <Type of Item> ---> "))
isFragile = str(input("Is it Fragile? (Y/N) ---> "))
weight = float(input("Input <Weight> (in kg) ---> "))
distance = float(input("Input <Distance> (in km) ---> "))
isExpress = str(input("Is it Express? (Y/N) ---> "))
isInternational = str(input("Is it International? (Y/N) ---> "))

# CONFIRM BOOLEANS
if isFragile == "Y":
    isFragile = True
elif isFragile == "N":
    isFragile = False

if isExpress == "Y":
    isExpress = True
elif isExpress == "N":
    isExpress = False

if isInternational == "Y":
    isInternational = True
elif isInternational == "N":
    isInternational = False

# CALCULATIONS
base_cost = (weight * 2.50) + (distance * 0.15)
if ((weight <= 2.0) and (distance <= 100) and (not isExpress) and (not isInternational)):
    Total = 0 # FREE SHIPPING
elif (isExpress and isInternational):
    Total = (base_cost * 1.40) + 50 # INTERNATIONAL EXPRESS
elif ((isExpress) or ((isInternational) and (weight > 20))):
    Total = (base_cost * 1.20) + 25 # EXPRESS OR HEAVY INTERNATIONAL
elif ((weight > 30) or (distance > 1000)):
    Total = base_cost + 30 # OVERSIZED
else:
    Total = base_cost # STANDARD RATE

# CONVERT BOOLEAN VARIABLES FOR THE PRINT STATEMENT (YES/NO)
if isFragile:
    isFragile = "Yes"
else:
    isFragile = "No"

if isExpress:
    isExpress = "Yes"
else:
    isExpress = "No"

if isInternational:
    isInternational = "Yes"
else:
    isInternational = "No"

# TOTAL
print(
    "Name of Sender:", senderName,
    "\nType of Item:", typeofItem,
    "\nFragile:", isFragile,
    "\nWeight (kg):", str(weight) + "kg",
    "\nDistance (km):", str(distance) + "km",
    "\nExpress:", isExpress,
    "\nInternational:", isInternational
    )

if Total != 0:
    print("\nTotal: ", "$" + str(Total) + "0") # should print Total: $XX.X0
else:
    print("\nTotal: ", "$" + str(Total) + ".00") # should print Total: $0.00
    

# TEST CASES
#  Weight    Distance   Express?  Int'l?   Expected Output
# 1  1.5 kg    50 km      False     False    $0.00
# 2  10.0 kg   200 km     True      True     $127.00
# 3  25.0 kg   100 km     False     True     $118.00
# 4  5.0 kg    1200 km    False     False    $222.50
# 5  10.0 kg   200 km     False     False    $55.00

# Does it work? Oh heck yeah it does :D