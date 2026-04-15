

try:

    result = 10/0
except ZeroDivisionError:
    print("oops! tried to divide by zero")


    fruits = {
        "apple":5,
        "banana":4,
        "orange":6
    }
    print(fruits["banana"])


    try:
        print(fruits["cherry"])
    except KeyError:
        print("the key does not exist in dictionary")
