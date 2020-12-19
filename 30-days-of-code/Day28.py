#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    names = []
    for N_itr in range(N):
        firstName, emailID = input().split()

        firstName, emailID = [str(firstName),str(emailID)]
        match = re.search(r'[\w\.-]+@gmail.com', emailID)

        if match:
            
            names.append(firstName)
        
    names.sort()
    for name in names:
        print(name)
        
        
    