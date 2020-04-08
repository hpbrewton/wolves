# graphing the various wolf populations

import matplotlib.pyplot as plt 
import math
import os 
import sys

def transpose(xs):
    return [[xs[i][j] for i in range(len(xs))] for j in range(len(xs[0]))]

domain_size = {
    "Wisconsin":  169640,
    "Michigan":   250490,
    "Minnesota":  225180,
    "Idaho"    :  216630,
    "Washington": 184830,
    "Oregon":     255030,
}

state = sys.argv[1]
filename = state + ".csv"
data_dir = "/Users/harrison/wolves/data"
file = open(data_dir + '/' + filename, "r")
# state = filename[:-4].capitalize()
data = transpose([list(map(float, line.strip().split(","))) for line in file])
for i in range(len(data[0])):
    data[1][i] /= domain_size[state]
plt.plot(data[0], data[1], '-')

plt.title("Wolf Densities in " + state)
plt.xlabel("Year Recorded")
plt.ylabel("Wolves Per Kilometer Squared (log scale)")
plt.yscale("log")
# plt.legend(loc='best')
plt.show()