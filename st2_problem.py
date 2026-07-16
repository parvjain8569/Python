# 1 question 

# def curated_list(scores):
#     if any(score < 0 or score > 100 for score in scores):
#         print("Invalid input")
#         return
#     res = list(map(lambda x: min(x + 5, 100), scores))
#     value = list(filter(lambda x: x >= 40, res))
#     print(value)

# curated_list=([80, 60,70])


# 2 question 


# raw=input().split()
# map=map(lambda x:x.replace("",""), raw)
# clean=map(lambda x:x.strip().capitalize(),map)
# result=list(filter(lambda x:len(x)>=3,clean ))
# print(result)

# 3 question 


# s="zebra"
# res =s[0]
# max=ord(s[0])
# for i in range(1,len(s)):
#   if ord(s[i])>max:
#     max=ord(s[i])
#     res=s[i]
# print(f"{res}={max}")


def reverse_substring(s, start, end):
 
  part1_before = s[:start]
  part2_substring = s[start:end+1]
  part3_after = s[end+1:]
  
  part2_reversed = part2_substring[::-1] 
  

  return part1_before + part2_reversed + part3_after


original_string = "abcdefghij"
start_index = 2
end_index = 6

result = reverse_substring(original_string, start_index, end_index)

print(f"Original: {original_string}")
print(f"Result:   {result}")