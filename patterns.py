# n=5 
# for i in range(n):
#     for j in range(n-i):
#         print("* ",end="")
#     print()

# rows = 5
# for i in range(1, rows + 1):
    
#     for j in range(rows - i):
#         print("  ", end="")
    
    
#     for k in range(i):
#         print("* ", end="")
    
#     # Move to the next line
#     print()


# n = 5

# # Top Row
# print("* " * n)

# # Middle Rows (n-2 rows)
# for i in range(n - 2):
#     print("* " + "  " * (n - 2) + "* ")

# # Bottom Row
# print("* " * n)




# n=5 
# for i in range(n):
#     for j in range(i+1):
#         print("* "+" "*((j+1)or(i-1)),end="")
#     print()/


# n = 5

# # 1. The Tip (Row 1)
# print("*")

# # 2. The Hollow Middle (Rows 2 to n-1)
# # Each middle row needs (i) sets of TWO spaces to match the grid
# for i in range(1, n - 1):
#     print("* " + "  " * (i - 1) + "*")

# # 3. The Base (Row n)
# print("* " * n)





n = 11  # Total rows (must be odd for a perfect diamond)
h = n // 2

# Top half + Middle row (0 to h)
for i in range(h + 1):
    stars = 2 * i + 1
    space2=stars+1
    spaces = (n - stars) // 2
    print(" " * spaces + "*" * stars)

for i in range(h-1,-1,-1):
    stars = 2 * i + 1
    spaces = (n - stars) // 2
    print(" " * spaces + "*" * stars)

