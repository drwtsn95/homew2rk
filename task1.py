s = str(input("Insert the string: "))
count_substrings = 0
i = 1
while i != len(s) + 1:
    if len(s) % i == 0:
        if str(s[0:i] * (len(s) // i)) == s:
            count_substrings = len(s) // i
            break
    i += 1
print (count_substrings)