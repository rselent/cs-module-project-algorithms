'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    singles = []

    for n in arr:
        if n not in singles:
            singles.append( n)
        else:
            singles.remove( n)
    return singles[0]

def single_number2(arr):
    # Your code here
    counts = {}

    for n in arr:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    for num in counts:
        if counts[num] == 1:
            return num

def single_number3(arr):
    # Your code here
    from collections import Counter
    
    counts = Counter(arr)

    for n in counts.elements():
        if counts.get(n) == 1:
            return n

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")