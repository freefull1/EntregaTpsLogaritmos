dicc_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
def romano_a_decimal(num_romano):
    if len(num_romano) == 0:
        return 0
    elif len(num_romano) == 1:
        return dicc_romanos[num_romano]
    else:
        if dicc_romanos[num_romano[0]] < dicc_romanos[num_romano[1]]:
            return dicc_romanos[num_romano[1]] - dicc_romanos[num_romano[0]] + romano_a_decimal(num_romano[2:])
        else:
            return dicc_romanos[num_romano[0]] + romano_a_decimal(num_romano[1:])
  
print(romano_a_decimal('XXXVIII'))