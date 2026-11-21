unit = input("Hello Monkey, watcha doin ? Come on now enter your temperautre unit: (F/C/K)")
temperature = float(input("Enter your stupid temperature."))

if unit == "C" :
    temperature = round((9 * temperature) / 5 + 32 )
    print(f"The temperature in Fahrenheit is : {temperature} F")

elif unit == "F" :
    temperature = (round((temperature - 32) * 5)/ 9)
    print(f"The temperatrure in Celcius is : {temperature} C")

else : 
    print (f"Dumbo, this{unit} or {temperature} ain't gonna work.")

