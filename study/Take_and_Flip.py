
def calculate_answer(lst):
    #出力値を初期化
    answer=0
    
    #リストが空になるまで計算
    while lst:
        #最大の数を選んで削除
        First_max_number=max(lst)
        lst.remove(First_max_number)
        #出力値に代入
        answer+=First_max_number
        
        #最小の数を選んで削除、まだ要素がある時計算
        if lst:
            Second_min_number=min(lst)
            lst.remove(Second_min_number)
            #出力値に代入
            answer+=Second_min_number
        
        
    return answer
    

def main():
    num_number=int(input('整数の個数'))
    number=input('スペースで区切って整数を入力')
    
    #入力された整数値をリスト化
    lst=list(map(int,number.split()))
    
    if num_number==len(lst):
        answer=calculate_answer(lst)
        print(answer)
    else:
        print("整数の数が一致しません")

main()