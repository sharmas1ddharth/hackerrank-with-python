

# def print_formatted(number):
#     # your code goes here
#     for i in range(number):
#         # decimal
#         i += 1
#         decimal_total = str(i).rjust(1, " ")
#         # octal
#         octal = oct(i).replace("0o","")
#         octal_total = str(octal).rjust(5, " ")
#         # hexadecimal
#         hexadecimal = hex(i).replace("0x", "").upper()
#         hexadecimal_total = str(hexadecimal).rjust(5, " ")
#         # binary
#         binary = bin(i). replace("0b", "")
#         binary_total = str(binary).rjust(5, " ")
        
#         print(str(i), str(octal), str(hexadecimal), str(binary))
        


# if __name__ == '__main__':
#     n = int(input())
#     print(print_formatted(n))
    


def print_formatted(number):
    
    l1 = len(bin(number)[2:])
   
    for i in range(1,number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(oct(i)[2:].rjust(l1,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
        print(bin(i)[2:].rjust(l1,' '),end=" ")
        print("")
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)