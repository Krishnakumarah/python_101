def manage_set(set1, element_to_add, element_to_remove):
    # Write code here
    set1.add(element_to_add)
    set1.discard(element_to_remove)
    if 5 in set1:
        return "5 is in the set"
    else:
        return "5 is not in the set"
