print("---#6064--")
#삼항연산자 : [True일때] if a > b else [False일때]
a,b,c=map(int,input().split())
print(c if c < (a if a<b else b) else (a if a<b else b) )