from bs4 import BeautifulSoup

import requests

#-------------------------------------------------------------------
#  IMPORTANT: RUN "test_udemy_solutions.py" FIRST
#-------------------------------------------------------------------



# url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# url = "https://www.empireonline.com/movies/features/best-movies-2/"

# response = requests.get(url)

# print(response.text)

# print("--------------------------------")
# const_htmlParser = "html.parser"
# web_page = response.text

# soup = BeautifulSoup(web_page, const_htmlParser )

# print(soup.title)

# print("--------------------------------")

# # all_movies = soup.find_all(name="h3" )
# all_movies = soup.select(selector="div h3")

# print(all_movies)

print("--------------------------------")
print("Reading from a file previously downloaded")

from bs4 import BeautifulSoup


filename = "100_best_movies.html"
const_htmlParser = "html.parser"
const_xmlParser = "lxml"
with open(filename, encoding="utf-8") as file:
    web_page = file.read()

soup = BeautifulSoup(web_page, const_htmlParser )    
print(soup.title)

print("--------------------------------")

all_movies = soup.find_all(name="h3", class_ = "jsx-4245974604" )
print(all_movies)


print("--------------------------------")


for x in all_movies[::-1]:
    print(x.text)



