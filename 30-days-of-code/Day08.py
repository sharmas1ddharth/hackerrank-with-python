n = int(input())
p = dict(input().split() for _ in range(n))
while True:
    try:
        name = input()
        if name in p:
            print(f"{name}={p[name]}")
        else:
            print("Not found")
    except:
        break