# 1. FREQUENCY
def frequency():
    cycles = float(input("Enter number of cycles: "))
    time = float(input("Enter time: "))
    if time != 0:
        print("Frequency =", cycles / time, "Hz")
    else:
        print("Time cannot be zero")

while True:
    frequency()
    reply = input("Continue? ")
    if reply.lower() != "yes":
        break


# 2. PERIOD
def period():
    freq = float(input("Enter frequency: "))
    if freq != 0:
        print("Period =", 1 / freq, "seconds")
    else:
        print("Frequency cannot be zero")

while True:
    period()
    reply = input("Continue? ")
    if reply.lower() != "yes":
        break


# 3. WAVE SPEED
def wave_speed():
    wavelength = float(input("Enter wavelength: "))
    freq = float(input("Enter frequency: "))
    print("Wave speed =", wavelength * freq, "m/s")

while True:
    wave_speed()
    reply = input("Continue? ")
    if reply.lower() != "yes":
        break


# 4. ELECTRIC CURRENT
def electric_current():
    charge = float(input("Enter charge: "))
    time = float(input("Enter time: "))
    if time != 0:
        print("Current =", charge / time, "A")
    else:
        print("Time cannot be zero")

while True:
    electric_current()
    reply = input("Continue? ")
    if reply.lower() != "yes":
        break


# 5. VOLTAGE
def voltage():
    resistance = float(input("Enter resistance: "))
    current = float(input("Enter current: "))
    print("Voltage =", resistance * current, "V")

while True:
    voltage()
    reply = input("Continue? ")
    if reply.lower() != "yes":
        break
