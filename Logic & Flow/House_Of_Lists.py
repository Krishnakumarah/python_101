def house_of_lists(list_of_lists):
    # Write code here
    sum_of_list=[n for n in list_of_lists if sum(n)<50]
    result=[n for inner in sum_of_list for n in inner if n<5]
    return result