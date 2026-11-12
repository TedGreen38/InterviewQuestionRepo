"""A collection of Python functions for interview questions."""


# Imports
import math

# Constants


# Reverse the input string by slicing from end to start with [::-1].
# Python slicing uses [start:stop:step]; here, start and stop are omitted,
# and step is -1, which walks backward through the string.
def reverseString(s):
    return s[::-1]

# Count how many vowels appear in the input string.
# The function lowercases the string so uppercase letters are counted too,
# then iterates over each character and increments the total whenever it is
# one of the vowels in "aeiou".
def countVowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)

# Add together each digit in the input number.
# The function converts the number to a string so it can iterate through each
# character, converts each character back to an integer, and sums them.
def sumOfDigits(n):
    return sum(int(digit) for digit in str(n))

# Calculate the factorial of the input number.
# The function initializes a result variable to 1, then multiplies it by each
# number from 1 to n.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

# Generate the nth Fibonacci number using iterative updates.
# The function keeps two values, a and b, representing the previous and current
# Fibonacci numbers. Each loop iteration shifts them forward by assigning
# a = b and b = a + b, and returns the final a after n steps.
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# check if the input number is prime.
# The function first handles small numbers and even numbers, then checks odd
# divisors up to the square root of n. If any divisor evenly divides n, it is not prime.
def isPrime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    for divisor in range(3, math.isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False

    return True

# Find the maximum value in a list of numbers.
def findMax(nums):
    largest = nums[0]
    for value in nums:
        if value > largest:
            largest = value
    return largest

# Find the second largest value in a list of numbers.
def secondLargest(nums):
    # Both start below every allowed value.
    largest = second = float("-inf")
    for x in nums:
        if x > largest:
            second = largest  # the old maximum drops to second place
            largest = x
        elif largest > x > second:
            second = x
    return second

# Count how many even numbers are in a list of numbers.
def countEvens(nums):
    count = 0;
    for value in nums:
        if (value % 2  == 0):
            count += 1
    return count

# Check if the input year is a leap year.
# A year is a leap year if it is divisible by 4, except for years that are
# divisible by 100, unless they are also divisible by 400.
def isLeapYear(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False

# Calculate the greatest common divisor (GCD) of two numbers using the
# Euclidean algorithm. The function repeatedly replaces the larger number
# with the remainder of dividing the larger by the smaller, until one of the
# numbers becomes zero. The other number is then the GCD.
def greatestCommonDivisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Calculate the least common multiple (LCM) of two numbers.
# The function uses the relationship between GCD and LCM: lcm(a, b) = abs(a * b) // gcd(a, b).  
def leastCommonMultiple(a, b):
    """Calculate the least common multiple (LCM) of two numbers."""
    return abs(a * b) // greatestCommonDivisor(a, b)

# Reverse the digits of the input number.
# The function converts the number to a string, reverses the string using slicing, and converts it back to an integer.
# For example, reverseDigits(12345) returns 54321.
def reverseDigits(n):
    numString = str(n)
    return int(numString[::-1])

# Check if the input number is an Armstrong number.
# An Armstrong number is a number that is equal to the sum of its own digits raised to
# the power of the number of digits. 
# For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.
def isArmstrong(n):
    digits = str(n)
    return sum(int(digit) ** len(digits) for digit in digits) == n

# Check if the input string is a palindrome.
# A palindrome is a string that reads the same forwards and backwards. The function compares the string to its reverse using slicing.
# For example, isPalindrome("racecar") returns True.
def isPalindrome(s):
    """Check if the input string is a palindrome."""
    return s == s[::-1]

# Count the number of digits in the input number.
# The function converts the number to a string and returns its length.
# For example, countDigits(12345) returns 5.
def countDigits(n):
    return len(str(n))

# Calculate the running sum of a list of numbers.
# The running sum is a new list where each element at index i is the sum of all elements from index 0 to i in the original list.
# For example, the running sum of [1, 2, 3] is [1, 3, 6].
def runningSum(nums):
    total = 0
    result = []

    for num in nums:
        total += num
        result.append(total)

    return result

# Find the maximum number of consecutive 1s in a binary array.
# The function iterates through the array, counting consecutive 1s and updating the maximum count
# whenever a 0 is encountered. It returns the maximum count of consecutive 1s found.
# For example, findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) returns 3.
def findMaxConsecutiveOnes(nums):
    current, best = 0, 0

    for num in nums:
        if num == 1:
            current += 1
            best = max(best, current)
        else:
            current = 0

    return best

# Convert a decimal number to its binary representation as a string.
# The function repeatedly divides the number by 2, prepending the remainder (0 or 1) to the binary string until the number becomes 0.
# For example, toBinary(10) returns "1010".
def toBinary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        # The remainder is the lowest bit that is left. it is prepended to the binary string.
        binary = str(n % 2) + binary
        n //= 2
    
    return binary

# Convert a binary string to its decimal representation as an integer.
# The function iterates over the binary string in reverse order, multiplying each digit by 2
# raised to the power of its index and summing the results to get the decimal value.
# For example, toDecimal("1010") returns 10.
def toDecimal(s):
    """Convert a binary string to its decimal representation as an integer."""
    decimal = 0
    for index, digit in enumerate(reversed(s)):
        decimal += int(digit) * (2 ** index)
    return decimal

def main():
    # Test the functions with example inputs (Beginner Level Problems)
    print("reverseString:", reverseString("hello"))
    print("countVowels:", countVowels("Interview"))
    print("sumOfDigits:", sumOfDigits(12345))
    print("factorial:", factorial(5))
    print("fib:", fib(7))
    print("isPrime:", isPrime(17))
    print("findMax:", findMax([3, 1, 8, 2]))
    print("secondLargest:", secondLargest([3, 1, 8, 2]))
    print("countEvens:", countEvens([1, 2, 3, 4, 6]))
    print("isLeapYear:", isLeapYear(2024))
    print("greatestCommonDivisor:", greatestCommonDivisor(48, 18))
    print("leastCommonMultiple:", leastCommonMultiple(12, 18))
    print("reverseDigits:", reverseDigits(12345))
    print("isArmstrong:", isArmstrong(153))
    print("isPalindrome:", isPalindrome("racecar"))
    print("countDigits:", countDigits(12345))
    print("runningSum:", runningSum([1, 2, 3, 4]))
    print("findMaxConsecutiveOnes:", findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
    print("toBinary:", toBinary(10))
    print("toDecimal:", toDecimal("1010"))

if __name__ == "__main__":
	main()
