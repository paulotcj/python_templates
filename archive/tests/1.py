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