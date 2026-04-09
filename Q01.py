# Q01. Grade Calculator (if-elif-else)
#
# Ask the user for a score (integer, 0-100).
# Print the letter grade using these rules:
#   90-100  → A
#   80-89   → B
#   70-79   → C
#   60-69   → D
#   Below 60 → F
#
# If the score is below 0 or above 100, print "Invalid score".
#
# Sample Input:   Enter your score: 85
# Sample Output:  Grade: B

# --- YOUR CODE HERE ---
mark=int(input("Enter your score: "))
if mark==0 or mark>100:
    print("Invalid Marks.")
else: 
    if mark>=90 and mark<=100:
        print("A")
    elif mark>=80 and mark<=89:
        print("B")
    elif mark>=70 and mark<=79:
        print("C")
    elif mark>=60 and mark<=69:
        print("D")
    else:
        print("F")