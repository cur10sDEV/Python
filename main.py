class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def intro(self):
        print(f"My name is {self.fname} {self.lname}")

user1 = User("shreyansh", "kourav")
user1.intro()