'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here

    if n < 0:
        return 0
    elif n < 1:
        return 1
    return eating_cookies( n-1) + eating_cookies( n-2) + eating_cookies( n-3)

    ...

def eating_cookies2(n):
    # Your code here

    if n < 0:
        return 0
    elif n < 1:
        return 1
    return eating_cookies( n-1) + eating_cookies( n-2) + eating_cookies( n-3)

    ...

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster \
to eat {num_cookies} cookies")
