from bs4 import BeautifulSoup
# import lxml

filename = "website.html"
const_htmlParser = "html.parser"
const_xmlParser = "lxml"
with open(filename, encoding="utf-8") as file:
    contents = file.read()


print("--------------------------------")


soup = BeautifulSoup(contents, const_htmlParser )

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print("--------------------------------")

print(soup)

print("--------------------------------")

print(soup.prettify())

print("--------------------------------")

print(soup.p)

print("--------------------------------")

print(soup.find_all(name = "a"))

print(soup.find_all(name = "p"))

print("--------------------------------")

all_anchor_tags = soup.find_all(name = "a")

for tag in all_anchor_tags:
    x = tag.getText()
    print(x)

print("--------------------------------")

for tag in all_anchor_tags:
    x = tag.get("href")
    print(x)

print("--------------------------------")

heading = soup.find_all(name = "h1" , id = "name")

print(heading)


heading = soup.find_all(name = "h3" , class_ = "heading")

print(heading)

print("--------------------------------")

test = soup.select_one(selector="p a")

print(test)
print(test.get("href"))



print("--------------------------------")

test = soup.select_one(selector="#name")

print(test)

print("--------------------------------")

test = soup.select(selector=".heading")

print(test)

