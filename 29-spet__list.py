# list 

                                        #list=[1,2,3,4]
                                        #print(list)                                                             
                                        #print(list[2])


# operation on list



                                                  #l2=[1,2,3,4,"parv","jain"]
                                                  #for val in l2:
                                                  #    print(val,end=" ")
                                                  #print()
                                                  #
                                                  #for i in range(0,len(l2)):
                                                  #    print(l2[i],end=" ")



# l3=[10,20,30]
                                                  
# l3.append(100)
# print(l3)
# l3.insert(2,100)
# print(l3)

# res = l3.pop(3)
# print(res)


# l4=[5,21,32,43,1,4,99,0]

# list.sort(l4)
# print(l4)








# list=[1,2,3,4,5,6,7,8,]

# print(list[2:5])
# print(list[ :5:2])
# print(list[2: ])
# print(list[ :-1])



# list=[1,2,3,4,5,6,7,8,]
# def print_list(l2):
#     for i in range(0,len(l2)):
#         print(l2[i],end=" ")
# print_list(list)


list=[1,2,3,4,5,6,7,8,]
def avg_list(l2):
    sum=0   
    for i in range(0,len(l2)):
        sum+=l2[i]
    return sum
sum=avg_list(list)
print(int(sum/len(list)))




list=[1,2,3,4,5,6,7,8,]
sum=0
for val in list:
    sum=sum+val
n=len(list)
print(sum//n)





# 1
# 2 3
# 4 5 6         print this 