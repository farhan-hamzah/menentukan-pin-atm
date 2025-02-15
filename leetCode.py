pin = str(input())
num = int(pin)
i = 0
while num > 0:
    num = num//10
    i +=1
if i == 4 or i == 6:
    print(True)
else:
    print(False)
