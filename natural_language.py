"""
Raymond's langauage analysis of facebook messages
Description: using googles natural language analysis my facebook messages
Functions: load file, return list of users,
return sentiment, return sentiment over time
return categories
"""

import os, sys, doctest
from bs4 import BeautifulSoup
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

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
        elif command == "show":
            show_text()
        else:
            print("Not proper command")

def show_text():
    text = load_file()
    text_soup = BeautifulSoup(text, "html.parser")
    print(text_soup.prettify())

def sentiment_analysis():
    text = load_file()
    text_soup = BeautifulSoup(text, "html.parser")
    user_messages = {}
    user_sentiment = {}
    """all_messages = text_soup.find_all("div", class_="message")
    for message in all_messages:
        print(message)
        print(message.children)
        print(message.descendants)
        """
    all_messages = text_soup.find("div", class_="thread")
    #print(all_messages)
    for child in all_messages.children:
        try:
            if child.find("span", class_="user"):
                name = child.find("span", class_="user").text
                message = child.next_sibling.text
                if name in user_messages:
                    prev_message = user_messages[name]
                    user_messages[name] = message + " " + prev_message
                else:
                    user_messages[name] = message
                #print(name, message)
                #print("---------------")
        except:
            pass
    #print(user_messages)
    # Instantiates a client
    client = language.LanguageServiceClient()

    for user, message in user_messages.items():
        # The text to analyze
        document = types.Document(content=message, type=enums.Document.Type.PLAIN_TEXT)
        # Detects the sentiment of the text
        sentiment = client.analyze_sentiment(document=document).document_sentiment
        user_sentiment[user] = (sentiment.score, sentiment.magnitude)
        #print('User: {}'.format(user))
        #print('Text: {}'.format(message))
        #print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    #print(user_sentiment)
    sorted_dict = (sorted(user_sentiment.items(), key=lambda x:x[1]))
    for i in sorted_dict:
        print("User: {0:10s} \t Sentiment: {1:.2f} \t Magnitude: {2:.2f}".format(i[0],i[1][0],i[1][1]))

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
