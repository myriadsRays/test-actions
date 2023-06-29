def check_word_in_file(filename, word):
    with open(filename, 'r') as file:
        content = file.read()
        if word in content:
            return True
        else:
            return False

filename = 'test.txt' 
word = 'life' 

if check_word_in_file(filename, word):
    print(f"The file '{filename}' contains the word '{word}'.") 
else:
    print(f"The file '{filename}' does not contain the word '{word}'.")

