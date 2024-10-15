# Define function to wount words
def count_words(passed_string):
    words = passed_string.split()
    count = len(words)
    return count

# Define function to count letters
def count_letters(passed_string):
    letter_dict = {}
    text = passed_string.lower() # Convert everything to lower case
    for character in text:
        if character in letter_dict:
            letter_dict[character] += 1
        else:
            letter_dict[character] = 1
    return letter_dict

# Define Main
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        letter_count = count_letters(file_contents)
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        print()
        for letter in letter_count:
            if letter.isalpha():
                print(f"The {letter} character was found {letter_count[letter]} times")
            else:
                pass
        

# Call Main
main()