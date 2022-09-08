import numpy as np

def n_sum(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total


if __name__ == "__main__":
    n = input()
    print("input ",n)
    print("total "n_sum(int(n)))

    #finish