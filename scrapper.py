import re

# Updated pattern
pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}),\s*(\d{1,2}:\d{2}\s*[aA][mM]|[pP][mM])\s*-\s*([\+\d]{1,3}\s*\d{10}|[\w!🌷]+(?:[\s\w!🌷]*))\s*:\s*(.+)'

parsed_data = []
unique_names = set()

with open('chat.txt', 'r', encoding='utf-8') as file:
    chat_data = file.readlines()

print("Chat Data:", chat_data)  # Print raw chat data

for line in chat_data:
    line = line.strip()  # Remove leading and trailing whitespace
    print(f"Processing line: {line}")  # Print each line without single quotes
    match = re.match(pattern, line)  # Use the updated pattern

    if match:
        date = match.group(1)
        time = match.group(2)
        name_or_number = match.group(3)
        message = match.group(4)
        
        unique_names.add(name_or_number)  # Add name or number to the set
        parsed_data.append({'date': date, 'time': time, 'name_or_number': name_or_number, 'message': message})
        print("Match found:", {'date': date, 'time': time, 'name_or_number': name_or_number, 'message': message})
    else:
        print("No match for line:", line)  # Print unmatched lines

names_array = list(unique_names)
print("Parsed Data:", parsed_data)
print("Unique Names/Numbers:", names_array)
