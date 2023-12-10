import sys

def generate_permutations(s):
    # Generate permutations using recursion
    if len(s) <= 1:
        return [s]
    
    result = []
    for i in range(len(s)):
        rest = s[:i] + s[i+1:]
        result.extend([s[i] + p for p in generate_permutations(rest)])
    
    return result

def custom_sort(char):
    # Define a custom sorting key based on the specified criteria
    if char.isdigit():
        return (0, char)
    elif char.isupper():
        return (1, char)
    else:
        return (2, char)

def main(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            input_str = line.strip()
            permutations = generate_permutations(input_str)
            
            # Sort permutations alphabetically using the custom sorting key
            sorted_permutations = sorted(permutations, key=lambda x: [custom_sort(c) for c in x])
            
            # Print sorted permutations separated by comma
            print(', '.join(sorted_permutations))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input_file")
        sys.exit(1)
    
    input_file = sys.argv[1]
    main(input_file)
