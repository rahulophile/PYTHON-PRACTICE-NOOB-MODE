#WAP to convert celcius to farenhite

def farenhite(c) :
    return (c * 9/5) + 32

c = int(input("Enter the degree is celcius : "))
print(f"{c}°C = {farenhite(c)}F")