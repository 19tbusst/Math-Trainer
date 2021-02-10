class book:
   def __init__(self, name, id):
       self.name = name
       self.id = id

   def myMeth(self):
        print("Name:", self.name, "\nID:", self.id)

b0 = book("Lord of the Flies", 0)
b1 = book("How to Kill a Mocking Jay", 1)
b2 = book("The Hobbit", 2)

#change "b1" to change output
b2.myMeth()





