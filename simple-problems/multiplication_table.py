"""
print a multiplication table
"""

def print_multiplication_table():
    """
    doc function 1
    """
    print ("Multiplication table")
    for i in range(1, 11):
        for j in range(1, 11):
            print("{:2} * {:2} = {:3}".format(i, j , i*j))
        print('\n')


def print_multiplication_tables2(n_cols):
    """
    doc function 2
    """
    max_num = 10
    n_rows = max_num // n_cols if max_num % n_cols == 0 else max_num // n_cols + 1
    for row in range(0, n_rows):
        for j in range(1, max_num + 1):
            line = ''
            for col in range(0, n_cols):
                a, b = row * n_cols + col + 1, j
                line += "{:2} * {:2} = {:3}    ".format(a, b , a*b)
            print(line)
        print("\n")

    
if __name__ == "__main__":
    print_multiplication_tables2(5)