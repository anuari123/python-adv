
def greet(name):
    global message
    message= f"hello,{name}"
    print(message)

greet("jona")

print(message)