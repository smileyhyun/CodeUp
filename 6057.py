print("---#6057--")
a,b=map(int,input().split())
a=bool(a)
b=bool(b)
print((a and b) or ((not a) and (not b)))       #참/거짓이 서로 같을 때에만 참