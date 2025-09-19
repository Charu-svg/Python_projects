import numpy as np                                     # 1

def input_int(prompt):                                 # 2
    while True:                                       # 3
        try:                                          # 4
            return int(input(prompt))                 # 5
        except ValueError:                            # 6
            print("Please enter a valid integer.")    # 7

def input_matrix(name="Matrix"):                       # 8
    rows = input_int(f"Enter number of rows for {name}: ")   # 9
    cols = input_int(f"Enter number of columns for {name}: ")#10
    print(f"Enter the elements of {name} row by row (space-separated).")#11
    mat = []                                          #12
    for i in range(rows):                             #13
        while True:                                   #14
            row_str = input(f" Row {i+1}: ")          #15
            parts = row_str.strip().split()           #16
            if len(parts) != cols:                    #17
                print(f"  → Please enter exactly {cols} numbers.")#18
                continue                               #19
            try:                                      #20
                row = [float(x) for x in parts]       #21
                mat.append(row)                       #22
                break                                 #23
            except ValueError:                        #24
                print("  → Please enter valid numbers (e.g. 1 2.5 -3).")#25
    return np.array(mat)                              #26

def print_divider():                                  #27
    print("\n" + "-" * 40)                            #28

def display_matrix(result, title="Result"):           #29
    print_divider()                                   #30
    print(title)                                      #31
    print_divider()                                   #32
    # If result is a scalar (determinant), just print it nicely:
    if np.isscalar(result):                           #33
        print(f" {result:.6g}")                       #34
    else:                                             #35
        # Print each row with readable spacing and rounding
        for row in result:                            #36
            print("  ".join(f"{val:.6g}" for val in row))#37
    print_divider()                                   #38

def menu():                                           #39
    print("\nMatrix Operations Tool")                 #40
    print(" 1. Addition")                              #41
    print(" 2. Subtraction")                           #42
    print(" 3. Multiplication")                        #43
    print(" 4. Transpose")                             #44
    print(" 5. Determinant")                           #45
    print(" 6. Exit")                                  #46
    return input_int("Choose an option (1-6): ")      #47

def main():                                           #48
    while True:                                       #49
        choice = menu()                               #50

        if choice == 1:  # Addition                    #51
            A = input_matrix("Matrix A")               #52
            B = input_matrix("Matrix B")               #53
            if A.shape == B.shape:                     #54
                display_matrix(A + B, "A + B")         #55
            else:                                      #56
                print("⚠ Error: Matrices must have same shape for addition.")#57

        elif choice == 2:  # Subtraction                #58
            A = input_matrix("Matrix A")               #59
            B = input_matrix("Matrix B")               #60
            if A.shape == B.shape:                     #61
                display_matrix(A - B, "A - B")         #62
            else:                                      #63
                print("⚠ Error: Matrices must have same shape for subtraction.")#64

        elif choice == 3:  # Multiplication              #65
            A = input_matrix("Matrix A")               #66
            B = input_matrix("Matrix B")               #67
            if A.shape[1] == B.shape[0]:               #68
                display_matrix(np.matmul(A, B), "A x B")#69
            else:                                      #70
                print("⚠ Error: Number of columns in A must equal number of rows in B.")#71

        elif choice == 4:  # Transpose                   #72
            A = input_matrix("Matrix")                 #73
            display_matrix(A.T, "Transpose of Matrix")#74

        elif choice == 5:  # Determinant                 #75
            A = input_matrix("Square Matrix")          #76
            if A.shape[0] == A.shape[1]:               #77
                det = np.linalg.det(A)                 #78
                display_matrix(det, "Determinant")    #79
            else:                                      #80
                print("⚠ Error: Determinant defined only for square matrices.")#81

        elif choice == 6:  # Exit                       #82
            print("Goodbye! 👋")                       #83
            break                                     #84

        else:                                          #85
            print("⚠ Invalid option. Please choose 1-6.")#86

if __name__ == "__main__":                            #87
    main()                                            #88
