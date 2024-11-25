import json
with open ('morse_dict.json', 'r') as file:
    morse_dict = json.load(file)

user_string = input("Type in your sentence: ").lower()

morse_list = [

]
for char in user_string:
    if char == ' ':
        morse_list.append('/') # Spaces are represented by /
    elif char in morse_dict:
        morse_list.append(morse_dict[char])
    else:
        print(f'Error, {char} is not a valid character and will be ignored.')


morse_string = ' '.join(morse_list)
print(morse_string)