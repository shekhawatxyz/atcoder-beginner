def upperstr(str1):
    ls1 = ""
    for s in str1:
        if s.isupper():
            ls1 += s
    return ls1

n = str(input())
result = upperstr(n)
print(result)
