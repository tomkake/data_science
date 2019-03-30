"""
    linear_search : 線形探索
    データが格納されている配列を最初から最後まで順番に見ていく方法
    この方法での問題は配列をすべて探索しなければならないということ
"""
data = [1,2,3,4,5,6,7,8,9,10]
target = 6
def linear_search(data,target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False