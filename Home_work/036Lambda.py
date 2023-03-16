
def print_operation_table(operation, num_rows, num_columns):
    for row in range(1, num_rows+1):
        for column in range(1, num_columns+1):
            print(operation(row,column), end=" ")
        print()

print(print_operation_table(lambda x,y: x*y, 6, 6))        