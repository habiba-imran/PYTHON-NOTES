# STATIC METHODS: methods that do not belong to class or any instance
# They're like normal functions, but grouped inside a class for organization.
class Math:
    @staticmethod # it does not have self like other functions of a class
    def add(a , b):
        return a + b
a = Math()
print(a.add(4, 5))
print(Math.add(4, 5)) # we cann call staticMethod using class or object

    

    
