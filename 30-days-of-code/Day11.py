#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    total_sum = []
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i+2) < 6 and (j+2) < 6:
                total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                total_sum.append(total)
    print(max(total))