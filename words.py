def print_uppercase_word(words):
    for word in words:
        print(word.upper())


print_uppercase_word(["Programming", "is", "pretty", "fun"])


def print_words_with_e(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())
            
print_words_with_e(["eagle", "Edward", "Alfred"])


def print_words_with_letter(words):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for word in words:
        if word[0].lower() in vowels:
            print(word.upper())

# Call the function with the list of words
print_words_with_letter(["eagle", "Edward", "Alfred", "zope"])
