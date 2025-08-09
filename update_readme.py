import re

def update_readme():
    """
    Updates the day counter in README.md by finding a number in the format (XX.XXX days),
    incrementing it by one, and writing the updated content back to the file.
    """
    readme_path = 'README.md'
    try:
        with open(readme_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: {readme_path} not found.")
        return

    # Regex to find the pattern like (11.828 days)
    pattern = re.compile(r'\((\d{2}\.\d{3}) days\)')

    match = pattern.search(content)
    if not match:
        print("Could not find the day counter in the README.")
        return

    # Extracting the number, removing the dot, and incrementing
    current_days_str = match.group(1)
    current_days = int(current_days_str.replace('.', ''))
    new_days = current_days + 1

    # Formatting the new number back to XX.XXX format
    new_days_str = str(new_days)
    formatted_new_days = f"{new_days_str[:-3]}.{new_days_str[-3:]}"

    # Replacing the old string with the new one
    old_string = f'({current_days_str} days)'
    new_string = f'({formatted_new_days} days)'

    new_content = content.replace(old_string, new_string)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"Successfully updated days from {current_days} to {new_days}.")

if __name__ == "__main__":
    update_readme()
