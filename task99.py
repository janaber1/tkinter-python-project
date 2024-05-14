def count_word_frequency(file_name):
    word_frequency = {}
    with open(file_name, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words
            words = line.split()# bt2smon h,l
            for word in words:
                # Remove punctuation
                word = word.strip('.,?!;:"')# btshil fara8 w spaceber
                # Convert mn capital to small
                word = word.lower()
                # Update the word frequency in the dictionary
                if word:
                    word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency

def main():
    file_name = input("Enter the name of the text file: ")
    try:
        # Count word frequency
        word_frequency = count_word_frequency(file_name)
        print("Word frequencies:")
        # Print word frequencies
        for word, frequency in word_frequency.items():
            print(f"{word}: {frequency}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
