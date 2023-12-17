normal_low = 97 # normal human body temperature lower end
temperature_measurements_1 = [98, 99, 97, 95.2, 100, 101.1]

normal_temperature_1= [] 
high_temperatures_2=[]
normal_high = 99 # normal human body temperature higher end
low_temperatures_1 = [] 
low_temperatures_2 = []
normal_temperature_2 = []
high_temperatures_1 = []

for temperature in temperature_measurements:
    if temperature < normal_low:
        low_temperatures_1.append(temperature)
    elif temperature > normal_high: 
        high_temperatures_1.append(temperature)
    else:
        normal_temperature_1.append(temperature)
        
temperature_measurements_2 = [98.2, 97, 97.1, 98.8, 100.2, 99]
for temperature in temperature_measurements_2:
    if temperature < normal_low:
        low_temperatures_2.append(temperature)
    elif temperature > normal_high:
        high_temperatures_2.append(temperature) 
    else:
        normal_temperature_2.append(temperature)
