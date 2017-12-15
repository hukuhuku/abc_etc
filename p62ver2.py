import numpy as np
n = 3
a = [3,5,8]
m = [3,2,2]
K = 17

dp = np.array([[False for i in range(K+1)]for i in range(n+1)])

if __name__ == '__main__':
    