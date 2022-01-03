# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Target = 600,851,475,143
# what is a prime number?

targetNum = 600851475143


num = int(input("enter a number: "))
factors = []
for i in range(1, num+1):
    if num % i == 0:
        factors.append(i)
print(f"Factors of {num} is: {factors}")
print(f"Max factor is: {max(factors)}")


# optimal solution
n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

print(n)
