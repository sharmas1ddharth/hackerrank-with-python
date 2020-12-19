n = int(input())
integer_list = map(int, input().split())

print(n)
a = tuple(integer_list)
print(a)
print(hash(a))