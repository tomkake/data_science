"""
        I番目とi+1番目を比べてi+1番目の方が小さかったら入れ替える。
        3,5,2,4,1(I = 0)
		3,2,5,4,1
		3,2,4,5,1
		3,2,4,1,5
		2,3,4,1,5(i=1)
		2,3,4,1,5
		2,3,1,4,5
		2,1,3,4,5(i=2)
        1,2,3,4,5(i=3)
"""
def bubble_rort(arr):
    change_place = True
    while change_place:
        print(arr)
        change_place = False
        for i in range(len(arr) - 1): #len(arr)-1 出ないと IndexError: list index out of range
            if arr[i] > arr[i + 1]:
                arr[i] , arr[i+1] = arr[i + 1] , arr[i]
                change_place = True
    return arr
print(bubble_rort([3,5,2,4,1]))