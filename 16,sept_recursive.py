# recursive fuction 


                                  # def facto(n):
                                  #     if n==1:
                                  #         return 1
                                  #     else:
                                  #         return n*facto(n-1)
                                      
                                  # print(facto(5))

#17 sept = test pad pr que kra tha 


# def fact(n):
# n=int(input("uahduia"))
# res=1
# for i in range (n+1):
#         if n==0 or n==1:
#             return 1
#         else:
#             res=res*i
# return res


# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1)

# number =  int(input().strip());
# result = 0;
# sum=number
# while number>0:
#     result= result + ((number%10)**3)
#     sum=sum//10
#     print(result)



# number =  int(input().strip());
# result = 0;
# temp = number 
# while temp>0:
#     d= temp%10
#     d= d**3
#     result=result+d
#     temp=temp//10
#     d=0




# n = int(input())

# for i in range(n):
#     if i == 0 or i == n: 
#         print("*" * n)
#     else:                   
#         print("*" + " " * (n-2) + "*")


# n = int(input())

# for i in range(n):
#     print("*" * n)
      

# for row in range(1,6):
#     for col in range(1,6):
#         if row==1 or row==5 or col==1 or col==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n = int(input("Enter size: "))

# for row in range(1, n+1):
#     for col in range(1, n+1):
#         if row==col :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     (print())



# n = int(input("Enter size: "))

# for row in range(n, 0, -1):          # row = n down to 1
#     for col in range(1, n+1):
#         if   row == col :
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()




# i = 1
# while i < 10:
#     i += 2
#     if i == 5:
#         continue
#     print("CodeQuotient")

n=int(input("enter the value :"))
sum=0
for i in range(1,n+1):
    
    i+=1
    sum=i*i
    print(sum)
