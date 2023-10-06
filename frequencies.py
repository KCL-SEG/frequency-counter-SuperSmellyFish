"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
# def frequencies(items):
#     frequencies = {}
#     # Your code goes here
#     for i in range(0,len(items)):
#         if isinstance(items[i], str):
#             pass
#         else:
#             items[i] = ''+str(items[i])+''
    
#     items.sort()
#     count = 1

#     # for i, el in enumerate(items[0:len(items)-1:1]):
#     #     if items[i] == items[i + 1]:
#     #         count += 1
#     #     else:
#     #         frequencies[items[i]] = count
#     #         count = 1
    
#     return frequencies

def frequencies(items):
    # Initialize an empty dictionary to store the frequencies.
    freq_dict = {}
    
    # Iterate through the items list.
    for item in items:
        # Convert the item to a string to use it as a key.
        key = str(item)
        
        # Check if the key is already in the dictionary.
        if key in freq_dict:
            # If it's in the dictionary, increment the count.
            freq_dict[key] += 1
        else:
            # If it's not in the dictionary, add it with a count of 1.
            freq_dict[key] = 1
    
    return freq_dict

# Test cases
print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))  # Output: {'a': 2, 'b': 3, 'c': 1}
print(frequencies([100, 'Hello', '100', '100', 100]))  # Output: {'100': 4, 'Hello': 1}


input = [100, 'Hello', '100', '100', 100]

output = frequencies(input)

print(output)