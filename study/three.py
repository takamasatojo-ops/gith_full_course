minimum=int(input("最小の数"))
maximum=int(input("最大の数"))

for n in range(minimum,maximum):
    if n%3==0 or "3" in str(n):
        print(n)