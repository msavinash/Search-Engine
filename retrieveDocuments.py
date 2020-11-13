import pickle
import os

with open("index1.pkl", "rb") as f:
	auxIndex, mainIndex = pickle.load(f)
# print(auxIndex.keys())



def convertKeyToPath(key):
	document, row = key.split(":::")
	document = auxIndex[int(document)]
	return os.path.join(document, row)


def retrieveDocuments(query):
	tokens = query.split(" ")
	tmpDocs = []
	for token in tokens:
		tmpDocs.append(list(mainIndex[token].keys()))
	print(tmpDocs[0])
	print(tmpDocs[1])
	resultSet = set(tmpDocs[0])
	for i in range(1, len(tokens)):
		resultSet = resultSet.intersection(tmpDocs[i])
	print(resultSet)
	print(auxIndex.keys())
	resultList = list(map(convertKeyToPath, list(resultSet)))
	print(resultList)




query = "industry airline"
retrieveDocuments(query)
