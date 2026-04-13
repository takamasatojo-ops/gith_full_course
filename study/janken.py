#まずは入力
man=int(input("岩井星人の人数"))
arm=int(input("岩井星人の腕の数"))
janken_kai=[]#それぞれのジャンケン

for i in range(man):
    jan=str(input(f"{1+i}人目の手の形をGCPの中から入力してください"))
    janken_kai.append(jan)

#配列に落とし込む
hairetsu=[list(t) for t in janken_kai]

#正解のリスト
yiwiy9=[]

for i in range(arm):

        #列ごとに考える
    shoubu=[row[i] for row in hairetsu]
    #グーチョキパーの数をカウント
    #その後場合分け、すでに勝った行は削除する。
    #グーチョキパーが同じ列に全て出ていたら勝てない。
    Goo=shoubu.count('G')
    Choki=shoubu.count('C')
    Paa=shoubu.count('P')
    if Goo>0 and Choki>0 and Paa==0:
        yiwiy9.append('G')
        hairetsu=[row for row in hairetsu if row[i] != 'C']
    elif Goo>0 and Choki==0 and Paa>0:
        yiwiy9.append('P')
        hairetsu=[row for row in hairetsu if row[i] != 'G']
    elif Goo==0 and Choki>0 and Paa>0:
        yiwiy9.append('C')
        hairetsu=[row for row in hairetsu if row[i] != 'P']
    elif Goo>0 and Choki==0 and Paa==0:
        yiwiy9.extend(['P'] * (arm - i))
        break
    elif Goo==0 and Choki>0 and Paa==0:
        yiwiy9.extend(['G'] * (arm - i))
        break
    elif Goo==0 and Choki==0 and Paa>0:
        yiwiy9.extend(['C'] * (arm - i))
        break
    elif Goo>0 and Choki>0 and Paa>0:
        yiwiy9=[-1]
        break

print(yiwiy9)






