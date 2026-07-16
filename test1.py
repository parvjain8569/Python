# class AgeError(Exception):
#     pass

# try:
#     age = int(input("Enter age: "))

#     if age < 0:
#         raise AgeError("Age cannot be negative")

#     elif age == 0:
#         raise AgeError("Age cannot be zero")

#     elif age < 18:
#         raise AgeError("Not Eligible for voting")

#     else:
#         print("Eligible for voting")

# except AgeError as e:
#     print(e)

# except ValueError:
#     print("Age must be an integer value")






# a=int(input())
# b=int(input())
# c=a*b

# if c%2==0:
#     print(a+b)
# else:
#     print(a-b)


# class negative_error(Exception):
#     pass
# try:
#     name=input("enter your name: ").lower().strip()
#     age=int(input("enter your age: "))
#     credit_score=int(input("enter credit score: "))
    
#     if age>=21 and age<=100 and credit_score >700:
#         print("Loan Approved!")
#     if age <21 or age >100  or credit_score <=700:
#         print("Loan Rejected")
#     if age <0 or age >100:
#         raise negative_error("Unrealistic inputs")
# except ValueError as e:
#     print("Invalid Input")
    
# except negative_error as e:
#     print(e)
# except Exception as e:
#     print(e)


str=input("enter number")
new_str=""
for i in str:
    if i.isalpha()==False and i.isdigit()==True:
        new_str+=i
        

sum=0
for i in new_str:
    sum+=int(i)

print(sum)