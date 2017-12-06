# Google-Natural-Language-Analysis
By Raymond Zhou
Using google's natural language analysis to analyse my Facebook messages with friends.
Motivation: I have two theories about my friends, that given any one of them, over a long period of time their sentiment in their messages would average out to 0. Sentiment being the negativity or positivity of their language, measured from a range of -1 to 1. So the positive things they say would eventually cancel out with the negative things the say.

However I have another theory that given a person, they have a distinctive personality and hence a distinctive personality. So their sentiment in their language would be either skewed negatively or positively.

So using Google's Natural Language Analysis API I've investigated the sentiment of language and how that reflects on the person.

Setting up:
First we need to get conversations from Facebook. Instructions can be found here.
https://www.facebook.com/help/131112897028467

Go to the downloaded folder and then choose a conversation to analyse from the messages folder.

Next you need to install BeautifulSoup which is a python module I used for parsing HTML. It can be install in the terminal with:
pip install bs4

Next you need to set up a Google Cloud account and set up the work environment.
Instructions can be found here.
https://cloud.google.com/natural-language/docs/quickstart-client-libraries
*ensure that none of your folder names' contain a space as virtualenv doesn't accept this.*

To run the program type:
python3 natural\_language.py name.html
where name.html is the html file containing the conversation.

You type "help" to see a list of commands.
\> user: returns a list of users in the conversation
\> show: returns the HTML text
\> sentiment: performs a sentiment analyse on the conversation and return a ordered list of users from lowest sentiment to highest sentiment. The magnitude is also included.
\> category: performs category analysis on the messages of every user and returns the topic each user has talked about and the confidence of that topic.
\> exit: exit the program



