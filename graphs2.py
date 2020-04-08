# graphing the various wolf populations

import matplotlib.pyplot as plt 
import math
import os 
import sys

def transpose(xs):
    return [[xs[i][j] for i in range(len(xs))] for j in range(len(xs[0]))]

domain_size = {
    "wisconsin":  169640,
    "michigan":   250490,
    "minnesota":  225180,
    "idaho"    :  216630,
    "washington": 184830,
    # "Oregon":     255030,
}

for state in domain_size.keys():
    filename = state + ".csv"
    data_dir = "/Users/harrison/wolves/data"
    file = open(data_dir + '/' + filename, "r")
    # state = filename[:-4].capitalize()
    data = transpose([list(map(float, line.strip().split(","))) for line in file])
    data += [[]]
    # print(data)
    for i in range(1, len(data[0])):
        data[2] += [data[1][i]/data[1][i-1]]
    plt.plot(data[0][1:], data[2], '-', label = state.capitalize())

plt.title("Wolf Growth Rates in 5 American States")
plt.xlabel("Year Recorded")
plt.ylabel("Size of Wolf Population Based on Previous Year")
# plt.yscale("log")
plt.legend(loc='best')
plt.show()