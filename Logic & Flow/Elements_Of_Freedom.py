def elements_of_freedom(elements):
    # Your solution here
    
    # Step 1: Filter elements with length >= 5
    Filter_elements=[element for element in elements if len(element)>=5]
     
    # Step 2: Convert filtered elements to uppercase
    Filtered_elements=[element.upper() for element in Filter_elements ]
    
    # Step 3: Create a list of unique elements
    unique_elements=[]
    for element in Filtered_elements:
        if element not in unique_elements:
            unique_elements.append(element)
    # Step 4: Return the final result
    return unique_elements