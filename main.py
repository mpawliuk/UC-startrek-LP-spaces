import numpy as np
import matplotlib.pyplot as plt

f = open("data.csv","r")
data = [[float(line.split(",")[3]), line.split(",")[4][:-1]] for line in f]

tos = np.array([pair[0] for pair in data if pair[1] == "Star Trek"])
tng = np.array([pair[0] for pair in data if pair[1] == "Star Trek: The Next Generation"])
voy = np.array([pair[0] for pair in data if pair[1] == "Star Trek: Voyager"])
ds9 = np.array([pair[0] for pair in data if pair[1] == "Star Trek: Deep Space Nine"])
ent = np.array([pair[0] for pair in data if pair[1] == "Star Trek: Enterprise"])


def norms(data):
  l1 = sum(data)/len(data)
  l2 = sum([x**2 for x in data]) ** 0.5 / len(data)
  l3 = sum([x**3 for x in data]) ** 0.3333 / len(data)
  linf = max(data)
  print(int(l1*10), int(l2*100), int(l3*100), int(10*linf))

norms(tos)
norms(tng)
norms(voy)
norms(ds9)
norms(ent)

plt.plot(np.sort(tos), 'r.-')
plt.plot(np.sort(tng), 'g.-')
plt.plot(np.sort(voy), 'b.-')
plt.plot(np.sort(ds9), 'c.-')
plt.plot(np.sort(ent), 'm.-')
plt.savefig('startrek_ratings_sorted.png')
f.close()
