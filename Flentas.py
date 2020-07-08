# input from user to enter the number of test cases
test_cases = int(input("Enter the number of test cases: "))
for test_case in range(test_cases):
    # input from user for the 1st line pattern
    pattern_string = input("Enter the pattern: ")
    # input from user for the 2nd line text string
    text_string = input("Enter the text string: ")
    if (pattern_string in text_string) or (pattern_string[::-1] in text_string):
        print("YES")
    else:
        print("NO")
