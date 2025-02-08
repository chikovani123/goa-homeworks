def convert_to_uppercase(sentence):
    return sentence.upper()

def get_name_uppercase():
    name = input("Enter your name: ")
    return name.upper()

def list_to_uppercase(lst):
    return [word.upper() for word in lst]


def convert_to_lowercase(sentence):
    return sentence.lower()

def get_email_lowercase():
    email = input("Enter your email address: ")
    return email.lower()

def to_lowercase(mixed_string):
    return mixed_string.lower()


def capitalize_sentence(sentence):
    return sentence.capitalize()

def capitalize_list(lst):
    return [word.capitalize() for word in lst]

def capitalize_string(string):
    return string.capitalize()

def find_python(sentence):
    return sentence.find("Python")

def find_substring(string, substring):
    return string.find(substring)

def find_character_index(string, char):
    return string.find(char)

def get_string_length(string):
    return len(string)

def get_list_lengths(lst):
    return [len(word) for word in lst]


def count_the(paragraph):
    return paragraph.lower().split().count("the")

def count_character(string, char):
    return string.count(char)

def count_word_occurrences(text, word):
    return text.lower().split().count(word.lower())


if __name__ == "__main__":
    print(convert_to_uppercase("hello world")) 
    print(get_name_uppercase()) 
    print(list_to_uppercase(["apple", "banana", "cherry"])) 
    
    print(convert_to_lowercase("HELLO WORLD"))  
    print(get_email_lowercase()) 
    print(to_lowercase("MiXeD CaSe")) 
    
    print(capitalize_sentence("hello world")) 
    print(capitalize_list(["apple", "banana", "cherry"]))  
    print(capitalize_string("python programming"))
    
    print(find_python("I love Python programming.")) 
    print(find_substring("Hello world", "world")) 
    print(find_character_index("Hello world", "o")) 
    
    print(get_string_length("Hello"))  
    print(get_list_lengths(["apple", "banana", "cherry"]))  
    
    print(count_the("The quick brown fox jumps over the lazy dog."))  
    print(count_character("banana", "a"))
    print(count_word_occurrences("The cat and the dog", "the")) 
