# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
number=int(input("Enter a number: "))
sum=0
num1=number
while number>0:
    digit=number%10
    sum+=digit
    number=number//10
print(f"Sum of digit of {num1} = {sum}")