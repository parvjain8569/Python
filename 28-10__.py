str=input()
str=str.lower()
vovel=0
cons=0
for ch in str:
    if ch in  ["a","e","i","o","u"]:
        vovel+=1
    else:
        cons+=1
        
print(f"total vowels {vovel} and total consonats {cons}")

str=input()
special,alpha,num=0,0,0
for ch in str:
    if ch.isalpha() == True:
        alpha+=1
    elif ch.isnumeric() == True:
        num+=1
    else:
        special+=1
print(special,alpha,num)

str =input()
if str[::-1] == str:
    print("palindrome")
    
else:
    print("nope")

str=input()
asci=0
for ch in str:
    
    if ord(ch)>asci:
        asci = ord(ch)
print(f"{chr(asci)} and {asci}")

str1=input().strip()
str1=sorted(set(str1))
str2=input().strip()
str2=sorted(set(str2))
if str1==str2:
    print("annogram")
else:
    print("nope")