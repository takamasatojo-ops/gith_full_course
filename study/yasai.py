
yasai=int(input("野菜の数"))
niku=int(input("肉の数"))
bai=int(input("肉は野菜の何倍たべる必要があるか"))
goukei=int(input("全体で何個まで食べられるか"))

answer = min(
    yasai,
    niku // bai,
    goukei // (1 + bai)
)

print(answer)