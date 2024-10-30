# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    def __init__(self, n="no name", a=0):
        self.name=n
        self.age=a
    def __str__(self) -> str:
        s = f"{self.name} is {self.age} years old"
        return s

#instance of the Dog class
logan = Dog("logan", 8)
cookie=Dog()
maple=Dog("maple",1)

print(logan.name)
print(cookie)
print(maple)