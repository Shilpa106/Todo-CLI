n=int(input())
checked = 0
for divisor in range(2, n//2+1):
    if(n%divisor ==0):
        print('no is not prime!')
        checked=1
        break

if(n==1):
    print('no is not prime!')
    checked=1

if(not checked):
    print("No is prime!")