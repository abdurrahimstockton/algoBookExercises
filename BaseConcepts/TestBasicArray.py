import  BasicArray
maxSize=100  #max size of the Array
arr= BasicArray.Array(maxSize)   #Object of Array class

arr.insert(77)                                # Insert 10 items
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)


print(f"All items are {arr.traverse()}")
print(f"deleting an item{arr.delete(12)}")
print(f"Searching returning {arr.search(12)}")
