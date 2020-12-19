arr = []
arr_sum = []
for _ in range(6):
    arr.append(list(map(int, input().split())))



for i in range(len(arr)):
    for j in range(len(arr[i])):
        if (j+2 < 6) and (i+2 < 6):
            total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
print(total)