# Twitter-Text-Analysis

## IMPORTANT!!!
In order to run the code, you must include an api key and api secret key. These keys can be obtained when creating an application on Twitter Developer. 

api_key = "insert api_key here"
api_secret_key = "insert api_secret_key here"

You must also include a user pin for authentication

pin = "insert user pin here"

# Purpose of the code
This code extracts tweets in real time and analyzes the count of named entities

# How it works
The code works at different stages. After importing the packages, the next cell authenticate the user for using the API, which must be entered into the code. The following cells, sets up the StreamListener and the functions to find an print named entities. The "preprocess" function takes the extracted tweets from the SteamListener and removes emojis, stopwords, etc. The function also converts the text to lowercase. The "addLabel" function creates a dictionary that keeps track of labels and its respective count of words found. The "printEntities" function takes the returned dictionary from the "addLabel" function and displays the named entities with its count under different labels.
