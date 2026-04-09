#import random

#太郎くんの思いついた数字
zirou=[0,1,2,3,4,5,6,7,8,9]
#decision=random.choice(zirou)

answers_list=[0,1,2,3,4,5,6,7,8,9]
answers_number=10

while True:
    #4つの数字を分割してリスト化
    numbers1=input("数字をスペースを区切って４つ提示してください")
    numbers_list=numbers1.split()
    numbers_list=[int(number) for number in numbers_list]



    #次郎くんの回答

    answer=input("YesかNoでお答え下さい").lower()
    #YESなら候補
    if answer=="yes":
        answers_list=list(set(answers_list)&set(numbers_list))
    #Noなら１〜９の中で提示されたもの以外
    elif answer=="no":
        jogai=list(set(zirou)-set(numbers_list))
        answers_list=list(set(answers_list)&set(jogai))
    
    
    #答えを１つに絞れたら終了
    if len(answers_list)==1:
        break
    


print(answers_list)