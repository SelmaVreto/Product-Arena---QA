from bs4 import BeautifulSoup
from requests import get
def get_only_text(url):
 page = get(url)
 soup = BeautifulSoup(page.content, "lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 #text = soup.text
 title = ' '.join(soup.title.stripped_strings)
 return title , text    
text = get_only_text("https://en.wikinews.org/wiki/Global_markets_plunge")
len(str.split(text[1]))
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

print("Word count")
print ("Title : " + text[0])
print ("Summary : ")
print (summarize(repr(text[1]), word_count=100))
len(str.split((summarize(repr(text[1]), word_count=100))))

print("Number of Words")
print ("Title : " + text[0])
print ("Summary : ")
print (summarize(repr(text[1]), ratio=0.1))
len(str.split(summarized_text))
print ('\nKeywords:')
print (keywords(text[1], ratio=0.1, lemmatize=True))