s = "babad"
result =""
for i in range(len(s)):
    for j in range(i, len(s)):
        substring = s[i:j+1]
        if substring == substring[::-1] and len(substring) > len(result):
            result = substring
print(result)
