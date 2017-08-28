class Person:
    """A general person class."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Person is reclaimed.")

    def wakeup(self, at):
        print('{0} wake up at {1} am'.format(self.name, at))


# mars = Person('Mars', 30)
# eleven = mars
#
# mars.name = 'eleven'
# mars.age = 28

# print(hasattr(mars, "name"))8

# mars.wakeup(8)

# print(getattr(mars,"name"))
# print(setattr(mars, "age", 18))

# delattr(mars, "name")

# print(mars.name)
# print(mars.age)
#
# print(id(mars))
# print(id(eleven))
#
# del mars
# print('only one ref')
# del eleven