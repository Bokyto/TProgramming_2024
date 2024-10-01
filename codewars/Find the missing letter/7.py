def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if ord(chars[i]) + 1 != ord(chars[i + 1]):
            return chr(ord(chars[i]) + 1)

result1 = find_missing_letter(['a', 'b', 'c', 'd', 'f'])
print(result1) 

result2 = find_missing_letter(['O', 'Q', 'R', 'S'])
print(result2) 