"""
    挿入ソート(i-1番目の要素までは並び替え済みと仮定して)
    (データの状態(數)に依存しないらしい)
    3,5,2,4,1
    3,5,2,4,1(I=1)
    2,3,5,4,1(i=2)
    2,3,4,5,1(i=3)
    1,2,3,4,5(i=4)
"""

def insertion_sort(arr):
    for i in range(len(arr)):
        tmp = arr[i] #ある値を持ち上げる
        j = i-1
        while j >=0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp; 
    return arr
print(insertion_sort([3,5,2,4,1]))