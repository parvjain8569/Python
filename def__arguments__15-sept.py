
# positional argument 


                                   # def Greet():   # def make the word "greet" a fuction (anything in this indetifier)
                                   #     print(f"hello students ...")
                                   
                                   # Greet()
                                   
                                   
                                   # def signup(username,password):   # (username,password) this si called as argument 
                                   #     print(f"username is {username},password is {password} ") # as we order both (username,password) so we call both of them 
                                   
                                   # signup(1618,"parv jain")



# keyword argument 
                                               
                                               # def signup(username,password):
                                               #     print(f"username is {username},password is {password} ")
                                               
                                               # signup(password="1618",username="parv jain")
                                               
 # default argument 
                                               
                                               # def dbconection(host="localhost",port=1120):
                                               #     print("serven is runing on {host} and port no. is {port}")
                                               
                                               #dbconection(3673)
                                               
                                               # signup(1618,"parv jain")


# variable length argument

                                               # def sumAll(*nums):
                                               #         sum=0
                                               #         for val in nums:
                                               #          sum = sumAll
                                               #         print(f"sum of number is {sum}")
                                               # sumAll(18,24,36,4,8)


#   dictionary 
                                                # def display_info(**person):
                                                #     for key, value in person.items():
                                                #        print(f"{key}:{value}")
                                                # display_info(name="parv",age="18",city="tohana")


# 'call by value' and 'call by refrence' ka matlb paper mai aa sakta hai 


                                                # def printnum(num):
                                                #     num=100
                                                #     print(num)
                                                # num=10
                                                # print(num)
                                                # printnum(num)


def add_to_list(my_list):
    my_list.append(4)
numbers = [1,2,3]
add_to_list(numbers)
print(numbers)  # output:[1.2.3] origanal is changed 




