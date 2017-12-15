import time
res = [0 for i in range(10000000)]
if __name__ == '__main__':
    start = time.time()
    for i in range(10000000):
        res[i] = i
    elaspsed_time = time.time() - start
    print("elaspsed_time:{0}".format(elaspsed_time) + "[sec]")
    