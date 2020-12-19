
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

d = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))
    
shifted = arr[d:] + arr[:d]

s = map(str, shifted)

new_arr = ' '.join(s)
print(new_arr)

