voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R): "))

if resistance == 0:
    print("Resistance cannot be zero.")
else:
    current = voltage / resistance
    print(f"Calculated Current: {current:.2f} A")

    if current < 0.5:
        print("Low current")
    elif 0.5 <= current <= 2:
        print("Normal current")
    else:
        print("High current")
      
