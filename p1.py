def print_matrix(mat, msg=""):
    if msg:
        print("\n" + msg)
    for row in mat:
        print([round(x,3) for x in row])
    print()


# --------------------------------------------------
# INPUT
# --------------------------------------------------
print("Gauss Elimination Calculator!\n")

max_col = int(input("Enter Maximum Degree Of The Equations: \n"))
max_row = int(input("Enter The Number Of Equations:\n"))

matrix = [[0.0 for _ in range(max_col)] for _ in range(max_row)]

for i in range(max_row):
    for j in range(max_col):
        matrix[i][j] = float(input(f"Enter Coefficient Of x{j}: "))

print_matrix(matrix, "Initial Matrix:")

# --------------------------------------------------
# GAUSS–JORDAN ELIMINATION
# --------------------------------------------------
pivot_row = 0

for pivot_col in range(max_col - 1):

    # find pivot
    pivot = None
    for row in range(pivot_row, max_row):
        if matrix[row][pivot_col] != 0:
            pivot = row
            break

    if pivot is None:
        continue

    # swap
    matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
    print_matrix(matrix, f"Swapped row {pivot} with row {pivot_row}")

    # make pivot = 1
    pivot_val = matrix[pivot_row][pivot_col]
    matrix[pivot_row] = [x / pivot_val for x in matrix[pivot_row]]
    print_matrix(matrix, f"Made pivot 1 at row {pivot_row}")

    # eliminate other rows
    for r in range(max_row):
        if r == pivot_row:
            continue
        factor = matrix[r][pivot_col]
        matrix[r] = [
            matrix[r][c] - factor * matrix[pivot_row][c]
            for c in range(max_col)
        ]

    print_matrix(matrix, f"Eliminated column {pivot_col}")

    pivot_row += 1


# --------------------------------------------------
# CLASSIFY SOLUTION TYPE
# --------------------------------------------------
# Check for NO SOLUTION
for row in matrix:
    if all(abs(x) < 1e-9 for x in row[:-1]) and abs(row[-1]) > 1e-9:
        print("NO SOLUTION (Inconsistent System)")
        exit()


# compute rank
rank = sum(any(abs(x) > 1e-9 for x in row[:-1]) for row in matrix)
vars = max_col - 1


# --------------------------------------------------
# UNIQUE SOLUTION
# --------------------------------------------------
if rank == vars:
    print("UNIQUE SOLUTION:")
    for i in range(vars):
        print(f"x{i} =", round(matrix[i][-1],3))
    exit()


# --------------------------------------------------
# INFINITE SOLUTIONS
# --------------------------------------------------
print("INFINITE SOLUTIONS (Dependent System)\n")

# find pivot columns
pivot_cols = []
for r in range(max_row):
    for c in range(vars):
        if abs(matrix[r][c] - 1) < 1e-9 and all(abs(matrix[r][k])<1e-9 for k in range(c)):
            pivot_cols.append(c)

free = [i for i in range(vars) if i not in pivot_cols]

print("Free variables:", free)

for r in range(max_row):
    # find pivot in row
    pivot = None
    for c in range(vars):
        if abs(matrix[r][c]-1) < 1e-9:
            pivot = c
            break
    if pivot is None:
        continue

    expr = f"x{pivot} = {round(matrix[r][-1],3)}"
    for f in free:
        if abs(matrix[r][f])>1e-9:
            expr += f" - ({round(matrix[r][f],3)}) t{f}"
    print(expr)
