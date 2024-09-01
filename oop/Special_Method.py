l1 = [1,2,3]
print(l1)

class Book():
    def __init__(self,title,page):
        self.title = title
        self.page = page

    def __str__(self):
        return "Title: {}  Page: {}".format(self.title,self.page)


    def __len__(self):
        return self.page

    def __del__(self):
        print("A book is destroy")

b = Book('Python',200)

print(b)
print(len(b))
del b
 





