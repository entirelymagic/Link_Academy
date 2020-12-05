word = input("Introdu cuvantul: ")
j = len(word) - 1
k = 0
isPalindrome = True
while k < j:
    if word[k] != word[j]:
        isPalindrome = False
        break
    k += 1
    j -= 1
print("Cuvantul " + word + (" este " if isPalindrome else "nu este ") + "un palindrom")


u_input = input("Enter your word: ")
is_Palindrome = True
if u_input == u_input[::-1]:
    is_Palindrome = True
else:
    is_Palindrome = False

print("The word " + u_input + (" is " if is_Palindrome else "is not a ") + "palindrome")
