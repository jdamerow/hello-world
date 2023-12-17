input = [98, 99, 97, 95., 100, 101.1]
losValue = []
norms = []
highs = []

for x in input:
  if x < 97:
        losValue.append(x)
  elif x > 99:
        highs.append(x)
  else:
        norms.append(x)
