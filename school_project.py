input_string = input("Enter any word: \n")
reverse_string_list = ''

for token in input_string:
    reverse_string_list = token + reverse_string_list

if reverse_string_list == input_string:
    print("The word is a Plaendrome.")

else:
    print("The word isn't a Plaendrome.")

if input_string == input_string.upper():
    print(input_string.lower())
elif input_string == input_string.lower():
    print(input_string.upper())

