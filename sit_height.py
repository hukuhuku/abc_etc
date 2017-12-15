    N = int(input())
    a = []
    for i in range(N):
      a.append(int(input()))

    a_dict = {k: v for v, k in enumerate(sorted(list(set(a))))} #
    for i in range(N):
        print(a_dict[a[i]])
