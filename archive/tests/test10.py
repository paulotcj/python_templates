import html
print("--------------------------------")
special_char_string = "this is a string with special characters in it: < > _ # $ ^ @ % ! * ( ) - + = { } [ ] : ; \" \' , . ? / "

print("test:        ",special_char_string)

html_encoded = html.escape(special_char_string)

print("html_encoded:", html_encoded)

html_escape = html.unescape(html_encoded)

print("html_escape: ", html_escape)

print("--------------------------------")


def greetings(name: str) -> str:
    return f"Hello {name}" 


def greetings2(name: str) -> str:
    return True

test = greetings(1)

print(test)

test = greetings2(1)

print(test)

print("--------------------------------")


mygenerator = (x*x for x in range(3))

for i in mygenerator:
    print(i)

print("generator is done - nothing is produced")
for i in mygenerator:
    print(i)    

print("--------------------------------")
def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i    

mygenerator = create_generator() # create a generator     
print(mygenerator) # mygenerator is an object!   

for i in mygenerator:
    print(i)

for i in mygenerator:
    print(i)    

print("--------------------------------")

print("Assert tests")

test = "Success. This xxxx random message"

assert "Success" in test

test = "Fail. This xxxx random message"
assert "Success" in test