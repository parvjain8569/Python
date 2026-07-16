# strings 

p="parv  "
p1="jain"
p2='''my name 
is 
pervysage'''
print(p)
print(p1)
print(p2)


name="i live in haryana  "
for index in range (len(name)):
    print(name[index],end=" ")
print()


# methode 2 membership operator 

for ch in name:
    print(ch,end=" ")


# str is class and string is object and string is imutable 

s="ram"
print(id(s))
s="shyam"
print(id(s))



# stribg methode 
s2="aman"
s3="AMAN"
s="hey fan's"
s1="hey i am here" 
print(s1.title())
print(s1.swapcase())
print(s2.upper())
print(s3.lower())
print(s.capitalize())

s="hey i am here am "
print(s.find("am"))
print(s.rfind("am"))

#question 
string=input("write the sentence ").lower()
vovel=0
cosonent=0
v=('a','e','i','o','u')
for ch in string:
    if ch in v:
        vovel+=1
    elif ch !=v and ch !=" ":

        cosonent+=1
        
    
print(vovel)
print(cosonent)
# question 
str=input().lower()
special=0
alphabed=0
number=0
for ch in str:
    if ch.isalpha()==True:
        alphabed+=1
    elif ch.isnumeric() ==True:
        number+=1
    else:
        special+=1
print(number,alphabed,special)







