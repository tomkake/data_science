"""
    (I番目を保存してその中で一番小さいものと入れ替える)
    3,2,4,1,5(I = 0)
    1,2,4,3,5
    1,2,4,3,5
    1,2,3,4,5
"""
def select_sort(arr):
    for i in range(len(arr)):
        print(arr)
        min_place = arr.index(min(arr[i:])) #一番小さい値の位置を持ってくる。list_name.index(max_or_min(list_name))で最大値か最小値のindex番号を持ってくる。
        arr[i] , arr[min_place] = arr[min_place] , arr[i]
    return arr
print(select_sort([3,2,4,1,5]))