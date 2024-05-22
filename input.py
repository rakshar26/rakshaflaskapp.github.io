class mynumber:
    def __init__(self,value):
        self.value = value
    def print(self):
        print(self.value)
val = input("Enter number ")
obj = mynumber(val)
obj.print()

