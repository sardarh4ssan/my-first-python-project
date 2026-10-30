i=1
while i<=100:
    print(i)
    i+=1
i=100
while i>=1:
    print(i)
    i-=1
i=1
while i<=10:
    print(3*i)
    i+=1
nums=[1,2,3,4,5,6,7,8,9]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1
num=(1,2,3,4,5)
x=4
idx=0
while idx<len(num):
    if(num[idx]==x):
        print("found at idx",idx)
    idx+=1
list=[1,2,3,4,5,6,7,8,9,10]
for num in list:
    print(num)
list=[1,2,3,4,5,6,7,8]
x=3
idx=0
for num in list:
    if(num==x):
        print("found",idx)
    idx+=1
for i in range(1,101):
    print(i)
for i in range(100,0,-1):
    print(i)
for i in range(3,33,3):
    print(i)
n=5
sum=0
for i in range(1,n+1):
    sum+=i
print("total sum",sum)
n=7
sum=0
i=1
while i<=7:
    sum+=i
    i+=1
print(sum)
n=5
fact=1
i=1
while i <=n:
    fact*=i
    i+=1
print(fact)
for i in range(1,11):
    print(i)
for i in range(10,0,-1):
    print(i)
for i in range(1,20,2):
    print(i)
for i in range(5):
    print("hello python")
i=1
sum=0
for i in range(1,101):
    sum+=i
    i+=1
print(sum)
# num=int(input("enter the number"))
# for i in range(1,11):
#     print(num*i)
count=0
for i in range(1,51):
    if i %5==0:
        count+=1
print(count)
list=[4,7,2,9,1]
largest=list[0]
for i in list:
    if i > largest:
        largest=i
print(largest)
list=[2,5,8,11,14]
count=0
for i in list:
    if i %2==0:
        count+=1
print(count)
n=7
i=1
fact=1
while i <=n:
    fact*=i
    i+=1
print(fact)
word=("python")
reverse=""
for i in word:
    reverse=i+reverse
print(reverse)
list=[2,3,4,5,6,8,7,9]
sum=0
for i in list:
    if i%2==0:
        sum+=i
        i+=1       
print(sum)
num=(1,2,3,4,5,6,7,0)
for i in num:
    if i ==0:
        break
    print(i)
for i in range(1,6):
    print("*"*i)
Num=[12,45,7,89,34,89,23]
largest=Num[0]
second=Num[0]
for i in Num:
    if i >largest:
        second=largest
        largest=i
print(second)
Number=58392
count=0
while Number>0:
    Number=Number//10
    count+=1
    print(count)


    

    

        


    
