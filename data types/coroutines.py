def print_matches(matchText):
    print("Looking for ",matchText)

    while True:
        line = (yield)
        if matchText in line:
            print(line)

matcher = print_matches("python")
next(matcher)
matcher.send("Hello World")
matcher.send("python is cool")
matcher.send("Yow pytHon!")
matcher.close()