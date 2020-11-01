import csv
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem import WordNetLemmatizer

file = "../TelevisionNews/BBCNEWS.201701.csv"




def preProcess(data):
	tokenizer = RegexpTokenizer("\\w+")
	tokens = tokenizer.tokenize(sample)
	tokens = list(map(str.lower, tokens))
	# print(tokens, len(tokens))

	stopwrds = stopwords.words("english")
	tokens_stopwrd_removed = list(filter(lambda x:x not in stopwrds, tokens))
	tokens_stopwrd_removed_set = list(set(tokens_stopwrd_removed))
	lem = WordNetLemmatizer()
	for i in range(len(tokens_stopwrd_removed_set)):
		tokens_stopwrd_removed_set[i] = lem.lemmatize(tokens_stopwrd_removed_set[i])
	return tokens_stopwrd_removed_set




with open(file, "r") as f:
	csvReader = csv.reader(f)
	data = list(csvReader)

sample = " ".join(data[1])
tokens = preProcess(sample)
print(tokens)