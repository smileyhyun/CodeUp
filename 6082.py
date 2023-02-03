print("---#6082--")
a=int(input())

for i in range(1,a+1):
    if (i%3==0 or i%6==0 or i%9==0):
        print("X", end=' ')
    else:
        print(i, end=' ')