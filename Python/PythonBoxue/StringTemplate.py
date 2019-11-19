print("Hello %s!" % "Mars")

name = "Mars"
print("%s %s" % ("Hello",name))

print("PI: %f" % 3.14)
print("PI: %.2f" % 3.14)

welcome = {"action": "Hello", "name": "Mars"}
print("%(action)s %(name)s" % welcome)

print("{0} {1}!".format("Hello", "Mars"))

print("{action} {name}!".format(**welcome))