# C to F converter
print("Enter a temp in Celsius to convert to Fahrenheit")
temp = float(input("Celsius "))
print((temp * 9/5) + 32)
print("Would you like to convert from Farhneheit to Celsius? ")
answer=input()
if answer=="Y" or "y":
     print("Enter a temp in Fahrenheit to convert to Celsius")
     tempF = float(input("Fahrenheit "))
     print((tempF - 32) * 5/9)
else:
     print("Thanks for playing!")

