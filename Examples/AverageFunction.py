import statistics

def average_funct(*x):
    # return statistics.mean(x)
    print(x)
    return sum(x)/len(x)


myTup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(average_funct(2, 4, 6, 8, 10))
