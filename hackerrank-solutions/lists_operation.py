# n = int(input())
# ls = []
# i = 0
# e = 0
# for num in range(n):
#     command = input().split()
#     # print(command)
    
#     if 'insert' in command:
#         i = command.index(command[1])
#         e = command[2]
#         ls.insert(i, e)
#         print(ls) #remove this line
    
#     elif 'print' in command:
#         print(ls) 
        
#     elif 'remove' in command:
#         e = command[1]
#         ls.remove(e)
#         print(ls) #remove this line
    
#     elif 'append' in command:
#         e = command[1]
#         ls.append(e)
#         print(ls) #remove this line
        
#     elif 'sort' in command:
#         ls.sort()
#         print(ls) #remove this line
        
#     elif 'pop' in command:
#         ls.pop()
#         print(ls) #remove this line
        
#     elif 'reverse' in command:
#         ls.reverse()
#         print(ls) #remove this line



n = int(input())
ls = []
for num in range(n):
    command = input().split()
    cmd = command[0]
    print(cmd)
    args = command[1:]
    print(args)
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        print(cmd)
        eval("ls."+cmd)
    else:
        print(ls)