"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range(0,len(items)):
        if isinstance(items[i], str):
            pass
        else:
            items[i] = ''+str(items[i])+''
    
    items.sort()
    count = 1

    for i, el in enumerate(items[:-1]):
        if items[i] == items[i + 1]:
            count += 1
        else:
            frequencies[items[i]] = count
            count = 1

    return frequencies
