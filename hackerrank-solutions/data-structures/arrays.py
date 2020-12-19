def reverseArray(a):
    a.reverse()
    s = map(str, a) 
    reverse_a = ' '.join(s)
    print(reverse_a)

arr_count = int(input())

arr = list(map(int, input().rstrip().split()))

res = reverseArray(arr)