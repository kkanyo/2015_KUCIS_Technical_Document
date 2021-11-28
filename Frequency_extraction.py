from konlpy.corpus import kobill
files_ko = kobill.fileids()
doc_ko = kobill.open('comment1.txt').read()
from konlpy.tag import Twitter; 
t = Twitter()
tokens_ko = t.nouns(doc_ko)
import nltk
ko = nltk.Text(tokens_ko, name = '음란1호')
data = ko.vocab().items()
import csv
with open('words.csv', 'w', encoding='utf-8') as f:
	f.write('word,freq\n')
	writer = csv.writer(f)
	writer.writerows(data)