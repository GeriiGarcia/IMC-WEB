#pyhon function to find height according to weight given IMC

x = [1.5,1.51,1.52,1.53,1.54,1.55,1.56,1.57,1.58,1.59,1.6,1.61,1.62,1.63,1.64,1.65,1.66,1.67,1.68,1.69,1.7,1.71,1.72,1.73,1.74,1.75,1.76,1.77,1.78,1.79,1.80]


IMC = 45


for i in x:
    print(round(i*i*IMC, 3))
    print(",")