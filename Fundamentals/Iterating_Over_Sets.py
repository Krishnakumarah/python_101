def iterate_and_filter_set(input_set):
    # Write code here
    return{x for x in input_set if x <=10}

def filter_and_square_set(input_set):
    # Write code here
    return (x**2  for x in  input_set if x % 2 !=0)
