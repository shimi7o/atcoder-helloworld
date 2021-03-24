# Q. r桁のルーレットがある。各桁は0〜9まである。桁の合計がtotalでアタリ！となる。アタリは何パターンあるか？。

def hoge(r, total):
    if r == 0:
        if total == 0:
            return 1
        return 0

    answer = 0
    for i in range(0, 9):
        answer += hoge(r-1, total-i)
    return answer


print(hoge(2, 3))
