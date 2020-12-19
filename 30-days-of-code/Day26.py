returned_date = list(map(int, input().split()))
expected_date = list(map(int, input().split()))



if returned_date[1:] == expected_date[1:]:
    days = returned_date[0] - expected_date[0]
    print(days * 15)
    
elif returned_date[2] == expected_date[2] and returned_date[1] > expected_date[1]:
    months = returned_date[1] - expected_date[1]
    print(500 * months)
    
elif returned_date[2] > expected_date[2]:
    print(10000)

else:
    print(0)