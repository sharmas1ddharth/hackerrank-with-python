input_num = input().split()


rows = int(input_num[0])
width = int(input_num[1])

for i in range (0, int (rows / 2)): 
    pattern = ".|." * ((2 * i) + 1) 
    print (pattern.center (width, '-'))
        
print("WELCOME".center(width, "-"))


for i in range(int(rows/2), 0):
    pattern = ".|." * ((2 * i) - 1)
    print(pattern.center(width, '-'))
    i = i-1    
    