def collatz(number):
    """ check if the number is even 
    or odd and performs some calculations.
    """
    if number % 2  == 0: # even
        print(number // 2)
        return number //2
    elif number % 2 != 0: # odd 
        result = 3*number+1
        print(result)
        return result

try:
    n = input('Enter number: ') # takes user input
    while n !=1: # performs while loop until 'n' becomes 1
        n = collatz(int(n)) # passes 'n' to collatz() function until it arrives at '1'
except ValueError:
    print('Value Error. Please enter integer.')
