list = ['Yuvraj',[1,2,3,4],'Drashti']

print(list)

mylist = ['a','b','c','d','e']
print(mylist)
mylist[0] = 'New Item'
print(mylist)

mylist.append('Yuvraj')
print(mylist)
mylist.extend(list)
print(mylist)
item = mylist.pop() # pop method return item
print(mylist)
print(item)

l2 = [1,2,[3,4,5],6]
print(l2)
print(l2[2][1])


matrix = [[1,2,3,],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[2][2])

# list comprehension
first_col = [row[0] for row in matrix]
print(first_col)







