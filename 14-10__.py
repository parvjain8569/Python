# using map with predefiend function  
def square(num):
    return num*num

number=[1,2,3,4,5]
result=map(square,number)  # map(fuction,itable)
print(result)  # we can not directly print map 
print(list(result)) # this is called map casting 




# map with lambda function 
number=[2,4,6,8]
result=list(map(lambda x: x*2,number))
print(result)




# using map with multiple variable 
list1=[1,2,3]
list2=[4,5,6]
result=list(map(lambda x,y: x+y, list1 ,list2))
print(result)


# we always get the min length of list as output 
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9,10]
result=list(map(lambda x,y,z: x+y+z, list1 ,list2,list3))
print(result)


#converting string to integer using map 
number=["10","20","30"]
result=list(map(int,number))
print(result)




# question 
list1=["a","b","c"]
def upper_case(a):
    return a.upper()


result=list(map(upper_case,list1))
print(result)




# filter methode example 
numbers=[10,15,20,25,30]
# function to check even number 
def is_even(num):
    return num %2 ==0

result=filter(is_even,numbers)
print(list(result))



# question is to filter the words having n 

list1=["rohan","parv","sohan","rohit"]

result=list(map(lambda x:"n" in x ,list1))
print(result)

# using def 
list1=["rohan","parv","sohan","rohit"]
def check_name(n):
    return "n" in n 

res=filter(check_name, list1)
print(res)

# filter out the order less than 1000 value and the number of order worth 1000 
number=[1000,200,500,700,2000,3000,1050]
def order(num):
    return num<=1000
res=filter(order,number)
print(list(res))




# reduce methode 

from functools import reduce               

numbers=[1,2,3,4,5] 

# function to add two number 
def add(x,y):
    return x+y 

result=reduce(add,numbers )
print("sum",result)


