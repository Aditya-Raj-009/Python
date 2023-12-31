# cook your dish here
T = int(input())
for _ in range(T):
    n = int(input())
    # A better way to split a string in list:
    arr = [int(item) for item in input().split()]
    count = 0
    for i in arr:
        if i>= 1000:
            count += 1
    print(count)

    # OR BY :

    # cook your dish here
    t = int(input())
    for i in range(t):
        n = int(input())
        # Map is a better way to split:
        d = list(map(int, input().split()))
        count = 0
        for i in d:
            if (i >= 1000):
                count = count + 1
        print(count)