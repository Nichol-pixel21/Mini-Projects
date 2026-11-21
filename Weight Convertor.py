weight = float(input("Enter your weight"))
unit = input("Kilograms or Pounds?(K or P)")

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L" :
    weight = weight/ 2.205 
    unit = "Kg"
else : 
    print(f"This {unit} shit ain't valid.")

print(f"YO so your weight is {round(weight), 2} {unit}")