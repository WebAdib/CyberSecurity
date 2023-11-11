def frequency_analysis(ciphertext):
    # Count the frequency of each character in the ciphertext
    char_frequency = {}
    total_chars = 0

    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            char_frequency[char] = char_frequency.get(char, 0) + 1
            total_chars += 1

    # Calculate the percentage of each character
    char_percentage = {char: (count / total_chars) * 100 for char, count in char_frequency.items()}

    # Sort characters by frequency
    sorted_chars = sorted(char_percentage.items(), key=lambda x: x[1], reverse=True)

    # Display the results
    print("Frequency analysis result:")
    for char, percentage in sorted_chars:
        print(f"{char}: {percentage:.2f}% --> Key for 'E': {calculate_key(char)}")

    return sorted_chars


def calculate_key(char):
    # Assuming 'e' is the most common letter in English
    # Calculate the key for a simple Caesar cipher
    key = (ord(char) - ord('e')) % 26
    return key


def main():
    ciphertext = input("Enter the ciphertext for frequency analysis: ")
    result = frequency_analysis(ciphertext)

    # Check if the most frequent character is likely 'e' (most common letter in English)
    if result and result[0][0] == 'e':
        print("The most frequent character is likely 'e', suggesting a simple substitution cipher.")

if __name__ == "__main__":
    main()
