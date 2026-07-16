# gender=str(input())
# salary=int(input())
# if gender=="female":
#     print(salary+(salary*(15/100)))
# elif gender=="male":
#     print(salary+(salary*(10/100)))
# else:
#     print("wrong gender")


days=int(input())
if 0<days<=5:
    print(0.5*days)
elif 5<days<=10:
    print(1*days)
elif 10<days<=30:
    print(5*days)
else:
    print("aaba jabaa jabaa ")



import sys

def sum_border_elements():

    try:
        
        line = sys.stdin.readline()
        if not line:
            return 0
        N, M = map(int, line.split())
    except EOFError:
        return 0
    except ValueError:
    
        print("Error: Invalid input for N and M.")
        return


    border_sum = 0
    matrix = []

   
    for i in range(N):
        try:
           
            row_line = sys.stdin.readline()
            if not row_line:
               
                return 0
           
            row_elements = list(map(int, row_line.split()))
            
           
            if len(row_elements) != M:
                print(f"Warning: Row {i+1} has {len(row_elements)} elements, expected {M}.")
                
            matrix.append(row_elements)

           
            for j in range(M):
               
                is_on_row_border = (i == 0) or (i == N - 1)
                
                
                is_on_col_border = (j == 0) or (j == M - 1)
                
                
                if is_on_row_border or is_on_col_border:
                    border_sum += matrix[i][j]

        except ValueError:
            print(f"Error: Invalid integer input in row {i+1}.")
            return
        except EOFError:
            return 0
            
    
    print(border_sum)




def find_row_maximums_ultra_minimal():
    r = int(input())
    c = int(input())

    row_maximums = []

    for i in range(r):
        row_line = input()
        
        row_elements = [int(x) for x in row_line.split()]

        max_in_row = max(row_elements)
            
        row_maximums.append(max_in_row)
            
    print(row_maximums)






def column_maximum():
    r = int(input())
    c = int(input())

    first_row_line = input()
    column_max = [int(x) for x in first_row_line.split()] 

    for i in range(1, r):
        row_line = input()
        current_row = [int(x) for x in row_line.split()]

        for j in range(c):
            if current_row[j] > column_max[j]:
                column_max[j] = current_row[j]
            
    print(column_max)