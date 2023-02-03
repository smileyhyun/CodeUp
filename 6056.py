print("---#6056--")
a,b=map(int,input().split())
a=bool(a)
b=bool(b)
print((a and (not b)) or ((not a) and b))       #XOR연산
                                                #참/거짓이 서로 다를 때에만 참