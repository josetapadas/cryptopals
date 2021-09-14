message = list('label')
flag = ''.join(list(map(lambda integer: chr(integer), list(map(lambda elm: ord(elm) ^ 13, message)))))
print(flag)