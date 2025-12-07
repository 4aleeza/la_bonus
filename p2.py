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

#now we have to go at first row first column elemet
#to make it 1

#have to make pivot values = 1 and have to save pivot values 
#to make 1 we divide diagonal values by the value itself

for i in range(max_row):
    pivot = matrix[i][i]
    if (pivot==0):
        print("Cannot Divide 0\n")
        break

    for j in range(max_col):
        matrix[i][j] = matrix[i][j]/pivot

    print("New Matrix:\n")
    for r in matrix:
        print(r)
    print("\n")

    #now we will make every number below leading 1 = 0
    #formula = current row*below element * -1 + below element

    #we need another loop counter to make 0s
    #below 1

  #check all rows uuse k
    for k in range(max_row): 
        
        #skip pivot row
        #so that not subtract itself
        if i != k:
            newzero = matrix[k][i] #we want to turn newzero into 0

            for c in range(max_col):
                matrix[k][c] = matrix[k][c]-(newzero*matrix[i][c])


print("Final Answer:\n")
for r in matrix:
    print(r)
