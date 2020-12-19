def average(array):
    # your code goes here
    ls = set(arr)
    sum_ls = sum(ls)
    len_ls = len(ls)
    average = sum_ls/len_ls
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)