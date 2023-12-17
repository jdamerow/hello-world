input = [[97, 96, 96], [99, 98, 99], [96, 96, 97], [100, 99, 100]] 
low_temps = []
low_count = 0
high_count = 0
for value in input:
    
    LOW_TEMP = 97
    average = 0
    if sum(value)/len(value) < LOW_TEMP: 
        average = sum(value)/len(value) 
        low_count += 1
    if average > 99:
        average = sum (value)/len (value) 
        high_count += 1
    average = sum(value)/len(value)
    
    if average > 97 and average < 99: 
        continue

    print("Average is " + str(average))
    
measurement_count = len(input)
low_percent= low_count/measurement_count*100
print("Low temperatures in {0}%.".format(low_percent))
