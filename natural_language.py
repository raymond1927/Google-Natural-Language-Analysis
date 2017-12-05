"""
Raymond's langauage analysis of facebook messages
Description: using googles natural language analysis my facebook messages
Functions: load file, return list of users,
return sentiment, return sentiment over time
return categories
"""

import os, sys, doctest
from bs4 import BeautifulSoup

def main():
    check_arg()
    interface()
    print("Hello World")


def interface():
    print("type help for instructions")
    while True:
        command = input("> ")
        if command == "exit":
            sys.exit()
        elif command == "help":
            print(instructions)
        elif command == "users" or command == "user":
            print_users()
        elif command == "sentiment" or command == "sent":
            sentiment_analysis()
        else:
            print("Not proper command")

def sentiment_analysis():
    text = load_file()
    text_soup = BeautifulSoup(text, "html.parser")
    print(text_soup.prettify())
    """all_messages = text_soup.find_all("div", class_="message")
    for message in all_messages:
        print(message)
        print(message.children)
        print(message.descendants)
        """
    all_messages = text_soup.find("div", class_="thread")
    print(all_messages)
    for child in all_messages.descendants:
        print(child)


def print_users():
    text = load_file()
    user_list_output = []
    text_soup = BeautifulSoup(text, "html.parser")
    print("From", text_soup.title.string)
    """
    user_list = text_soup.find_all("span", class_="user")
    for user in user_list:
        if user.text not in user_list_output:
            user_list_output.append(user.text)
    print(user_list_output)
    """


def load_file():
    try:
        f = open(sys.argv[1], 'r')
        text = (f.read())
        f.close()
        return text
    except:
        f.close()
        print("Problem reading file")
        sys.exit()

def check_arg():
    if (len(sys.argv) != 2):
        print("Usage: python3 natural_language.py <file_name>")
        sys.exit()
    elif (os.path.isfile(sys.argv[1]) == True):
        pass
    else:
        print("File {} not found".format(sys.argv[1]))
        sys.exit()

if __name__ == "__main__":
    doctest.testmod()
    instructions = """
    Yo whats up
    """
    main()
