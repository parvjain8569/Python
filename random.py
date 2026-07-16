# str = input().strip()
# numbers=list(map(int,input().split()))
# i,j=numbers[0],numbers[1]
# part=""
# new=""
# try:
#     if j>i and len(str)>j and len(str) >i:
#      new=str[i:j+1]
   
#      new = new[::-1]
   
#      part=str[:i]
   
#      part=part+new+str[j+1:]
#      print(part)
    
#     else:
#        print("Invalid")
    
# except Exception as e:
#     print("Invalid",e)



# Q - ST1


roll = int(input())

def cr(roll):
    sum = 0
    print(roll)
    while roll !=0:
     sum += roll % 10
     print(sum)
     roll = roll // 10
     
    if sum <=26:
       print(f"hey {sum}")
      
    else:
       print(sum)
       cr(sum)
    return sum
    

h=cr(roll)
print(h)






