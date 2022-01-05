"""
Sequence of numbers and sum:
- Read M and N (if M or N is zero or less, stop the algorithm)
- Check M and N (biggest and smallest)
- Store in biggest/smallest variables
- print range(smallest, biggest + 1)
- print sum range(smallest, biggest + 1)
"""
M = int(input("First Number: "))
N = int(input("Second Number: "))

if M > 0 and N > 0 and M != N:
    if M > N:
        biggest_number = M
        smallest_number = N
    else:
        biggest_number = N
        smallest_number = M
    
    for numbers in range(smallest_number, biggest_number + 1):
        print(numbers)
    
    print(f"Sum: {sum(range(smallest_number, biggest_number + 1))}")