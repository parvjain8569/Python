list=[1,2,3,4,5,6,7]    
n=int(input("enter the number "))

if n in list:
    print("yes it is in list")
    position = list.index(n)
    print(f"the position of {n} is {position}")
else:
    print("no it is not in the list ")

          

list=[1,2,3,4,5,6,7]  

key =int(input("enter the value : "))
is_find=False

for index in range(0,len(list)):
    if list[index]==key:
        is_find=True
        break

if is_find:
    print(f"key is present at index{index}")
else:
    print("key is not found ")

result= lambda a,b:a+b
print(result(2,3))









list = []  
n = 7


while n <= 100:
    list.append(n) 
    number += 7 

print(list)




a=int(input("enter value of celsius "))
b=32
c=9/5
print((a*c)+b)
    


