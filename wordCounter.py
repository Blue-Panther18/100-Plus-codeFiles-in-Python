def wordCounter(text):
    '''
    Counts the number of words in a given text or file.

    text(arg): the text or file to be analyzed.

    return: the number of words in the given text.
    '''

    if text.endswith('.txt'):
        try:
            with open(text, 'r') as file:
                text = file.read()
        except:
            print("File not found.")
            return 0

    words = text.strip().split()
    return len(words)

       
# Example usage:
sentence = "This is a sample sentence with multiple words."
file_path = "./files/sample.txt"

# Testing a sentence with multiple words.
print(f"The number of words in this sentence is: {wordCounter(sentence)}.")

# Testing a file with multiple words.
print(f"The number of words in this file is: {wordCounter(file_path)}.")