# GETTERS and SETTERS
# Getters: Functions used to access the value of a private attribute.
# Setters: Functions used to update/change the value of a private attribute.
class Person:
    def __init__(self, n):
        self.__name = n # double undersores for private variable
        # private variable can't be accessed direcly, so we use getter function
    def set_name(self, new_name):
        self.__name = new_name
    def get_name(self):
        return self.__name
    
a = Person("habiba")
print(a.get_name()) # prints habiba
a.set_name("hunain")
print(a.get_name()) # prints hunain
# Without a setter, your object becomes unchangeable, 
# unless you expose the private variable (which breaks encapsulation).
# Setter allows you to change the value after the object is created.
# self.value	 |   Public
# self._value	 |   Protected	
# self.__value	 |   Private





