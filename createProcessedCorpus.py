import csv
import os
from preProcessor import preProcess

FOLDER = "..\\TelevisionNews"
NEW_FOLDER = "TelevisionNews2"


LOGFILE = "log.txt"



def getFilesRecursive(folder):
	# folder = rewritePath(folder)
	files = []
	for root,d_names,f_names in os.walk(folder):
		files.extend(list(map(lambda x:os.path.join(root, x), f_names)))
	return files


def storeData(data, path, number):
	path = path.replace("TelevisionNews", NEW_FOLDER)
	# print(path)
	try:
		os.makedirs(path)
	except FileExistsError:
		pass
	fileName = str(number) + ".txt"
	with open(os.path.join(path, fileName), "w") as f:
		f.write(" ".join(data))

files = getFilesRecursive(FOLDER)

# print(files[0])
skippedCount = 0
skippedFiles = []
for file in files:
	print(file)
	with open(file, "r") as f:
		csvReader = csv.reader(f)
		try:
			rows = list(csvReader)
		except UnicodeDecodeError:
			print("Skipping", file)
			skippedCount += 1
			skippedFiles.append(file)
			continue
	for rowNum in range(1, len(rows)):
		row = " ".join(rows[rowNum])
		tokens = preProcess(row)
		# print(tokens)
		folderPath = ".."+file.strip(".csv")
		storeData(tokens, folderPath, rowNum+1)
with open(LOGFILE, "w") as f:
	f.writelines([str(skippedCount)] + skippedFiles)

