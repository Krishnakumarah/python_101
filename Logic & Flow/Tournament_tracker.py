# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
all_matshes=list(match1.intersection(match2,match3))

# 2. Find players who participated in exactly two matches
exactly_matches1=(match1.intersection(match2))
exactly_matches2=(match2.intersection(match3))
exactly_matches3=(match1.intersection(match3))
exactly_two_matches = list(exactly_matches1.symmetric_difference(exactly_matches2).symmetric_difference(exactly_matches3))
# 3. Find players who participated in only one match

# 4. Count total unique players

# 5. Find players in Match 1 only

# Print results in the specified format
print("Players in all matches: ",all_matshes)
print("Players in exactly two matches: ",exactly_two_matches)