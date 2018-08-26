from math import sqrt, pow


def average(data):
    return float(sum(data)) / len(data)


def std_dev(data):
    avg = average(data)
    return sqrt(sum(pow(x - avg, 2) for x in data) / (len(data) - 1))


def correlation(data_x, data_y):
    n = len(data_x)
    sum_data = 0

    for i in range(n):
        sum_data += data_x[i] * data_y[i]

    numerator = sum_data - (n * average(data_x) * average(data_y))
    denominator = (n - 1) * std_dev(data_x) * std_dev(data_y)

    return float(numerator) / denominator


n = input()

maths = list()
phys = list()
chem = list()

for _ in range(int(n)):
    inp = input().split("\t")
    maths.append(int(inp[0]))
    phys.append(int(inp[1]))
    chem.append(int(inp[2]))

print(round(correlation(maths, phys), 2))
print(round(correlation(phys, chem), 2))
print(round(correlation(chem, maths), 2))
