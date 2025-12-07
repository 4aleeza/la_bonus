print("Gauss Elimination Calculator!\n")

max_col = int(input("Enter Maximum Degree Of The Equations: \n"))
max_row = int(input("Enter The Number Of Equations:\n"))

##i have initialized matrix with 0s

matrix = [[0.0 for i in range(max_col)] for i in range(max_row)]

for i in range(max_row):
    for j in range(max_col):
        coeff = input(f"Enter Coefficient Of x{j}: ")
        matrix[i][j] = float(coeff)


print("Matrix: \n")
for mat in matrix:
    print(mat)

pivot_row = 0

for pivot_col in range(max_col-1): #cuz last column is right hand side in augmented matrix

#finding non zero entry
    pivot = None
    for row in range(pivot_row, max_row):
        if matrix[row][pivot_col] != 0:
            pivot = row
            break

    #if full zero
    if pivot is None:
        continue

    #swapping pivot row into right position
    matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]

    #making pivot =1
    pivot_val = matrix[pivot_row][pivot_col] #assigning the pivot to a variable
    matrix[pivot_row] = [x/pivot_val for x in matrix[pivot_row]] #performin matrix operating on the whole row to make the pivot 1

    
