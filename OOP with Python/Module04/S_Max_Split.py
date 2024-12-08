def count_balanced_substrings(s):
    balance = 0
    count = 0
    result = []

    current_substring = []
    
    for char in s:
        current_substring.append(char)
        if char == 'L':
            balance += 1
        elif char == 'R':
            balance -= 1
        
        if balance == 0:
            count += 1
            result.append(''.join(current_substring))
            current_substring = []

    # Output results
    print(count)
    for substring in result:
        print(substring)

# Example Input/Output
count_balanced_substrings("LLRRLLLRRR")
count_balanced_substrings("LLLRRR")
