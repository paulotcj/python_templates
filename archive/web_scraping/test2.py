from bs4 import BeautifulSoup

import requests

url = "https://news.ycombinator.com/news"

response = requests.get(url)

print(response.text)

print("--------------------------------")
const_htmlParser = "html.parser"
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, const_htmlParser )

print(soup.title)

print("--------------------------------")

article_tag = soup.select(selector="span", class_ = "titleline")
print(article_tag)

for x in article_tag:
    print(x)



