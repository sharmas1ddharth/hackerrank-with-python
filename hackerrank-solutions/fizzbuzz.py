def fizzbuzz(ls):
    for i, num in enumerate(ls):
        if num % 3 == 0:
            ls[i] = "fizz"
        elif num % 5 == 0:
            ls[i] = "buzz"
        elif num % 3 == 0 and num % 5 == 0:
            ls[i] = "fizzbuzz"
    print(ls)
    
    
if __name__ == "__main__":
    n = int(input())
    ls = []
    for _ in range(n):
        numbers = int(input())
        ls.append(numbers)
    
    fizzbuzz(ls)

