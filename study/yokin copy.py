def keisan(num_ginko, wariai, yokin):
    
    #最初の帳簿総額
    choubo=0

    #銀行の数だけchouboに差し引かれたyokinを足していく
    for i in range(num_ginko):
        choubo+=yokin
        yokin*=(1-wariai)
        
    return choubo

def main():
#値入力
    num_ginko=int(input('銀行の数入力'))
    wariai=float(input('手元に残す割合'))
    
    #最初の預金額(変わる可能性もあるのでこちらの関数に入れている)
    yokin=100


    result=keisan(num_ginko, wariai,yokin)
    
    print(result)

main()