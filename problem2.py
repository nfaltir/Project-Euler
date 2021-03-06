fibonacci_dictionary = {}  # create dictionary, implement memoization


def fibonacci(n):
    if n in fibonacci_dictionary:
        return fibonacci_dictionary[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)  # recursive function

    # store value and return it

    fibonacci_dictionary[n] = value
    return value


print("\n==========Fibonacci Sequence==========\n")

# ask user to enter max length of fibonacci sequence
#sequence_length = int(input("Enter max length of sequence:"))

#create variables to enforce algo rules
maxNum = 4000000
prevNum = 0
evenFibSum = 0  
count = 0

while prevNum < maxNum:
    prevNum = fibonacci(count)
    if prevNum %2 == 0 and prevNum < 4000000:
        evenFibSum = evenFibSum + prevNum
        print(count, prevNum)

    count = count + 1

print("Total even sum: ", evenFibSum)
