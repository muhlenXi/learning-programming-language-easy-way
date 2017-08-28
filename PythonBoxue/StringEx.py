
print("%s World!" % "Hello")
print("%s %s" % ("Hello", "World!"))
print("{0} {1}".format("Hello", "World!"))

welcome = {"action":"Hello", "name":"World"}
print("{action} {name}!".format(**welcome))

stringInDoubleQuotes = "Hello Python!"
stringInSingleQuotes = 'Hello Python!'
stringInTripleQuotes = '''Hello Python!
This might be a long string
going through multiple lines.'''

aNumber = 23
aString = str(aNumber)
print(aString)

oneTwoThree = int("123")
print(oneTwoThree)

action = "Hello "
name = "Mars!"
welcome = action + name
print(welcome.upper())
print(welcome.lower())
print(action.strip())

print(action[0:4])
