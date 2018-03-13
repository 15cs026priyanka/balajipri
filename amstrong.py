lower=1000
upper=900
for x in range(lower,upper+1):
    order=len(str(num))
sum=0
temp=num
while temp>=0:
    digit=temp%10
    if num==sum:
        print(num)  
