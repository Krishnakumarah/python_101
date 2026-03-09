def find_occurrences(text, pattern):
    
    count = 0
    positions = []

    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
            positions.append(i)

    if count > 0:
        return (True, count, positions)
    else:
        return (False, 0, [])


text = input()
pattern = input()

result = find_occurrences(text, pattern)
print(result)