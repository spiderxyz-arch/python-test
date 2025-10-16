def greet_user(name):
    name = input("enter your name: ")
    print("hey, " + name + " python is waiting for you!")


def string_exploration(sentence):
    user_sentence = input("Enter your sentence: ")   
    print("Title case:", sentence.title())
    print("Spaces replaced with '-':", sentence.replace(" ", "-"))
    print("Without leading/trailing spaces:", sentence.strip())
 
    greet_user(__name__)
    string_exploration(user_sentence)
    




