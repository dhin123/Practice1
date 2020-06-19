# Given an array arr[] and a position in array, k. Write a function name reverse (a[], k) such that it reverses subarray arr[0..k-1]. Extra space used should be O(1) and time complexity should be O(k).

lst= [1, 2, 3, 4, 5, 6]
k = 4

sublst1 = lst[:k]
print(sublst1[::-1] + lst[k:])