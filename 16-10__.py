
# assiging grade using map 



marks=[40,50,60,70,80,90]
def grade(grade):
    if grade<60:
        return 'd'
grade=list(map(grade,marks))
print(marks)
print(grade)


# question 
salary=[20000,40000,60000,80000]
def dis(num):
    if num<50000:
        s=(10/100)*num
        return s+num
    else:
        m=(15/100)*num
        return m+num
result=list(map(dis,salary))
print(result)

#  creating a matrix 

matrix = [[1,2,3], [4,5,6],[7,8,9]]

for row in matrix:
  for element in row:
    print(element, end=" ")
print()


# creating a matrix 


for row in range(3):
  for col in range(3):
    print(matrix[row][col], end=" ")
print()



# sum of matrix 
matrix_list = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

total_sum = 0
for row in matrix_list:
    for element in row:
        total_sum += element

print(f"Matrix: {matrix_list}")
print(f"Total Sum: {total_sum}") 


# find that the number is present in the matrix or not 

matrix_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target_number = 12
is_present = False

for row in matrix:
    for element in row:
        if element == target_number:
            is_present = True
            break 
    if is_present:
        break 

if is_present:
    print(f"The number {target_number} is present in the matrix.")
else:
    print(f"The number {target_number} is not present in the matrix.")








