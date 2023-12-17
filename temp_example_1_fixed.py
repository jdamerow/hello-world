NORMAL_LOW = 97 # normal human body temperature lower end 
NORMAL_HIGH = 99 # normal human body temperature higher end

def sort_temperatures (measurements):
    low = []
    normal = []
    high = []
    
    for temperature in measurements: 
        if temperature < NORMAL_LOW:
            low.append(temperature)
        elif temperature > NORMAL_HIGH: 
            high.append(temperature)
        else:
            normal.append(temperature)

    return low, normal, high

temperature_measurements_1 = [98, 99, 97, 95.2, 100, 101.1]
temperature_measurements_2 = [98.2, 97, 97.1, 98.8, 100.2, 99]

low_1, normal_1, high_1 = sort_temperatures(temperature_measurements_1) 
low_2, normal_2, high_2 = sort_temperatures(temperature_measurements_2)
