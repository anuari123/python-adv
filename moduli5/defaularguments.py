from plotly.serializers import custom_serializers

from moduli5.function import greet


def greet_person(name, greeting="hello")
    message = f"{greeting},{name}"
    return message

default_greeting = greet_person("alisa")
print(default_greeting)

custom_greeting = greet_person("alisa","hi")
print(custom_greeting)