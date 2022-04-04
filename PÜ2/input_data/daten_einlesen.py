




from numpy import loadtxt

lines = loadtxt("power_data_1.txt", delimiter=",")
for line in lines:
    print(line)

