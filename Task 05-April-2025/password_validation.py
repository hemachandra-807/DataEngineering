
'''
     Part	                                     Meaning
====================================================================================
^               >-----------------Start of the string
[A-Z]           >-----------------Exactly one uppercase letter at the beginning
[a-z]+	        >-----------------Followed by one or more lowercase letters
[\w@#$%^&+=!]*	>-----------------Then, zero or more characters that are:
                                  - letters (A-Z, a-z)
                                  - digits (0-9)
                                  - underscore (_)
                                  - allowed special characters (@#$%^&+=!)
\d+	            >-----------------Ends with one or more digits
$	            >-----------------End of the string

Note: \w means [A-Za-z0-9_]
=====================================================================================
'''
import re

password_validation = r"^[A-Z][a-z]+[\w@#$%^&+=!]*\d+$"
password = "Hemachandra@807"
match = re.fullmatch(password_validation, password)

if match:
    print("Password Validation is correct: ",match.group())
else:
    print("Password is Invalid please enter valid password")

