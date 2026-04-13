
def calculate_answer(lst):
    #lstを並び替え
    lst.sort()
    #出力値を初期化
    answer=0
    
    #リストが空になるまで計算
    while lst:
        #最大の数を選んで answerに足す。
        answer+=lst.pop()
        #最小の数を選んで、answerに足す。
        if lst:
            answer+=lst.pop(0)
        
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