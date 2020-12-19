import itertools

# blank list
text_list = []
#take input and split into two as list = ['', '']
take_input = input().split()
# save list element into text
text = take_input[0]
# save list element into num
num = take_input[1]

#loop to convert the string itno list
for i in text:
    text_list.append(i)

# sort the list
text_list.sort()
# join and covert the list into string
sorted_string = "".join(text_list)

# combination_with_replacements using itertools
ls = list(itertools.combinations_with_replacement(sorted_string, int(num)))
blank_str = ""

# convert the list into string
for i in range(len(ls)):
    tuple_to_list = list(ls[i])
    join_list = blank_str.join(tuple_to_list)
    print(join_list)