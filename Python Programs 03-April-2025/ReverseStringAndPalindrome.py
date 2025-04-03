string_reverse = "racecar"# examples of palindrome words are madam, level, racecar, malayalam etc.,
rev = ""
for i in range(len(string_reverse)-1, -1, -1):
    rev = rev + string_reverse[i]

#print(rev)

if rev == string_reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")