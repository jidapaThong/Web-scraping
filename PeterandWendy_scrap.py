# This is a project that scrape a novel named "Peter and Wendy" from the website Project Gutenberg using Python. 
# Extracting words from this web data using BeautifulSoup. 
# Analyzing the distribution of words using the Natural Language ToolKit (nltk).

# Question: What are the most frequent 20 words in the novel Peter and Wendy and how often do they occur?
# Answer: Most frequent 20 words:  
# [('peter', 410), ('wendy', 367), ('said', 357), ('pg', 271), ('one', 214), ('would', 214), ('hook', 174), 
# ('could', 143), ('cried', 134), ('john', 133), ('time', 127), ('darling', 118), ('see', 111), ('michael', 110), 
# ('little', 104), ('mother', 102), ('boys', 101), ('children', 99), ('gutenberg', 98), ('know', 94)]

import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt


#get the dataset from link
dataset = 'https://www.gutenberg.org/cache/epub/26654/pg26654-images.html'
novel = requests.get(dataset)
html = novel.text
#Create a BeautifulSoup object from the HTML
data = BeautifulSoup(html,"html.parser")
data.title.string
#Get the text out of the soup
text = data.get_text()

#Extract Words from the text with NLP
#1.Tokenize the text (split text into a list of words)
#2.Remove stopwords

tokenizer = RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
words = []
# Loop through list tokens and make lower case to count as the same word 
for word in tokens:
    words.append(word.lower())
 
stopword = nltk.corpus.stopwords.words('english')
newList = []
# Loop add to newList all words that are in words not in stopword
for word in words:
   if word not in stopword:
       newList.append(word)

#obtains frequency distribution 
word_frequency = nltk.FreqDist(newList) 
print("Most frequent 20 words: ", word_frequency.most_common(20))
#visualization
word_frequency.plot(20, title='Top 20 Most Common Words in Peter and Wendy novel')
