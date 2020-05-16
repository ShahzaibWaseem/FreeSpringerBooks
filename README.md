# Free Springer Books

All books were downloaded from the springer website, which are a part of the COVID-19 Package Issue. This list may get updated on the [springer website](https://link.springer.com/search?facet-content-type=%22Book%22&package=mat-covid19_textbooks&%23038;facet-language=%22En%22&%23038;sortOrder=newestFirst&%23038;showAll=true).

## Code

The Code file ```springerDownloader.py``` is written for Python 3 to run it just run the code file
```bash
$python3 springerDownloader.py 
```
The Program requires a .csv file ```springerBooks.csv```, which contains all the links to the individual books, it also creates two maintainer files ```progressFile.txt```, which tells it how many books were downloaded in the previous session (this is if the program was terminated due to some internet connection issue) so it resumes from that point on, and ```notDownloadedBooks.csv```, which tells the program which books failed to download, the reason may be that the book was free initially but now is not available on the springer website or due to some other error. Lastly the program makes a folder ```"books/"``` and saves the downloaded books there.

### Libraries Needed
- os
- wget
- pandas
- pyquery