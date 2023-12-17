from collections import Counter

measurements = [[97, 96, 96], [99, 98, 99], [96, 96, 97], [100, 99, 100]]
LOW_TEMP = 97
HIGH_TEMP = 99

def get_average(temperatures):
    return sum(temperatures)/len(temperatures)

def count_average(average, counter):
    if average HIGH_TEMP:
        counter['high'] += 1
        
def calculate_percentage(count, total,x):
    return count/total*100

average_counter = Counter({'low': 0, 'high': 0})

for temperatures in measurements:
    average = get_average(temperatures) 
    print("Average is " + str(average))
    
    if average > LOW_TEMP and average < HIGH_TEMP: 
        continue
        
    count_average(average, average_counter)
    
measurement_count = len(measurements)

print("Low temperatures in {0}%.".format(calculate_percentage(average_counter['low'], measurement_count)))
print("High temperatures in {0}%.".format(calculate_percentage(average_counter['high'], measurement_count)))
