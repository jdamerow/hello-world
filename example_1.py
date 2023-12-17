input = [98, 99, 97, 95., 100, 101.1]
los = []
norms = []
highs = []

for x in input:
    if x < 97:
        los.append(x)
    elif x > 99:
        highs.append(x)
    else:
        norms.append(x)
