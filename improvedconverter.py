# this block converts the given input, kilometers, to miles
km = float(input("Enter the distance in kilometers: "))
cf = 0.621371 # this is the conversion factor because 1 km ≈ 0.621371 miles
m = km*cf
print("Distance in miles:" ,m)

# this gives them the option to do a second conversion
sc = input('Do you want to convert another distance? (yes/no): ')
if sc == "yes":
    # performs the second conversion 
    sckm = float(input("Enter the distance in kilometers: "))
    scr = sckm*cf
    print("Distance in miles:" ,scr)
else:
    # stops the program if the user declines
    print("Program ended.")
