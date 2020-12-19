def split_and_join(line):
    
    split_text = line.split()
    join_text = "-".join(split_text)
    return join_text

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

