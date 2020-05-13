import os
import wget
import pandas as pd
from pyquery import PyQuery

BOOKS_FILE_PATH="books"
SPRINGER_BASE_LINK="https://link.springer.com/"

def directoryHandling():
	if not os.path.exists(os.path.join(BOOKS_FILE_PATH)):
		os.mkdir(os.path.join(BOOKS_FILE_PATH))

def main():
	linkTag="a.test-bookpdf-link"
	booksDF=pd.read_csv("springerBooks.csv", index_col="S.No.", header=0)

	progressFile=open("progressFile.txt", "r")
	line=progressFile.read()
	progressFile.close()
	print("Previously Downloaded Files:", line)

	directoryHandling()

	print("Downloading Books")

	for index, bookEntry in booksDF.iterrows():
		if index <= int(line):
			continue
		htmlLink=bookEntry["OpenURL"]
		bookTitle = bookEntry["Book Title"].replace("\n", "")
		authorsName = bookEntry["Author"].replace("\n", " ")
		edition = bookEntry["Edition"].replace("\n", ", ")

		pq = PyQuery(url=htmlLink)
		bookFileName=bookTitle + "(" + authorsName + ")" + "[" + edition + "]" + ".pdf"

		try:
			bookLink = SPRINGER_BASE_LINK[:-1] + pq(linkTag).attr['href']
		except Exception as e:
			# Maintain a txt file of files not downloaded
			notDownloadedBooks=open("notDownloadedBooks.csv", "a")
			notDownloadedBooks.write(str(index) + " , \"" + bookFileName + "\", " + htmlLink + "\n")
			notDownloadedBooks.close()
			print("Not Downloading", str(index), bookFileName)
			continue

		print(index, bookTitle + "(" + authorsName + ")" + "[" + edition + "]" + ".pdf")

		wget.download(bookLink, out=os.path.join(BOOKS_FILE_PATH))

		# Maintain a txt file which tells how many files were previously downloaded
		progressFile=open("progressFile.txt", "w")
		progressFile.write(str(index))
		progressFile.close()

		os.rename(os.path.join(BOOKS_FILE_PATH, bookLink.split("/")[-1]), os.path.join(BOOKS_FILE_PATH, bookTitle + "(" + authorsName + ")" + "[" + edition + "]" + ".pdf"))
		print()

if __name__ == '__main__':
	main()
