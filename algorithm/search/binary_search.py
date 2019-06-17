"""
    線形探索の場合データが格納されている配列を一つずつ最初から最後まで見ていったが二分探索ではソート済みのデータの配列を半分にしてtargetが前にあるのか後ろにあるかを見ていきながらtargetを探す方法
"""
data = [1,2,3,4,5,6,7,8,9,10]
target = 6
def binary_search(data,target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target: 
            return True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
print(binary_search(data,target))