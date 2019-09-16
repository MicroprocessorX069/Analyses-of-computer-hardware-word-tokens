#vNeaMgt0OVCoVXeDtkQsFLeAsPrCuEuO
import requests
import urllib2
from bs4 import BeautifulSoup
import re
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import time

stop_words_added=["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves","also" ]
def parse_articles(articles):

    news = []
    for i in articles["response"]["docs"]:
        news.append(i["web_url"])
    return(news) 

def get_articles(year,query):
    all_articles = []
    r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json?q="+query+"&begin_date="+year+"1001&api-key=vNeaMgt0OVCoVXeDtkQsFLeAsPrCuEuO")
    data = r.json()
    flag=False
    for key, value in data.iteritems():
	if key=="response":
		print("Response exists, phew!")
		flag=True
		break

    articles=[]
    if(flag==True):
	    print("Pages: "+str(len(data)))
	    articles = parse_articles(data)
            return(articles)
    else:
 	    return articles

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
#subTopics=["ram","motherboard","cpu","gpu","server"]
subTopics=["server"]
file_name="/home/vineet/Spring 2019/Data Intensive Computing/Lab 2/data/nyt_data.txt"
#txt = open(file_name, 'w')
stop_words=set(stopwords.words('english'))
for subTopic in subTopics:
	print("Subtopic: ",subTopic)
	time.sleep(25)
	allArticles = []
	for i in range(2008,2019):
	    print('Processing' + str(i) + '...')
	    articles =  get_articles(str(i),subTopic)
	    print("Pages: "+str(len(articles)))
	    if len(articles)>0:
	    	allArticles  += articles

	file_name="/home/vineet/Spring 2019/Data Intensive Computing/Lab 2/data/nyt_data.txt"
	#stemmer = SnowballStemmer("english")
	txt = open(file_name, 'a+')
	stemmer=PorterStemmer()
	for url in allArticles:
		soup = BeautifulSoup(urllib2.urlopen(url).read())
		for tag in soup.find_all('p'):
			text=""
			article=tag.text.encode('utf-8')
			article=re.sub(r'[^\w\s]','',article)
			wordList = article.split()
			for word in wordList:
				word=word.lower()
				if (word not in stop_words) and (word not in stop_words_added) and not(hasNumbers(word)):
					#text+=stemmer.stem(word)
					text+=word
					text+=" "
			txt.write(text + '\n')

	txt.close()
