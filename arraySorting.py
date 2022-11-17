#Implementing sortable Array data strucutre

class Array(object):

    def __init__(self, initialSize):  #Constructor
        self.__a=[None]*initialSize # The array stores as a list
        self.__nItems=0 #No items in array initally

    def __len__(self):
        return self.__nItems        #Return number of items

    def get(self, n): #Return value at the index n
        if 0<=0 and n<self.__nItems: #check if n is in bounds
            return self.__a[n]

    def set(self,n, value):
        if 0<=n and n<self.__nItems:
            self.__a[n]=value   #set item if it is in the bounds

    def swap(self,j, k): # Swap value at 2 indexes
        if(0<=j and j<self.__nItems and 0<=k and k<self.__nItems): #check if indexes are in bound,before processing
            self.__a[j], self.__a[k]=self.__a[k], self.__a[j]


    def insert(self,item): #Insert item at the end
        if self.__nItems>=len(self.__a): #if array is full, raise exception
            raise Exception("Array overflow")
        self.__a[self.__nItems]=item #Item goes at the current end
        self.__nItems+=1

    def find(self, item):  # Find index for item
        for j in range(self.__nItems):  # Among current items
            if self.__a[j] == item:  # If found,
                return j  # then return index to element
        return -1  # Not found -> return -1

    def search(self, item):  # Search for item
        return self.get(self.find(item))  # and return item if found

    def delete(self, item):  # Delete first occurrence
        for j in range(self.__nItems):  # of an item
            if self.__a[j] == item:  # Found item
                self.__nItems -= 1  # One fewer at end
                for k in range(j, self.__nItems):  # Move items from
                    self.__a[k] = self.__a[k + 1]  # right over 1
                return True  # Return success flag

        return False  # Made it here, so couldn't find the item

    def traverse(self, function=print):  # Traverse all items
        for j in range(self.__nItems):  # and apply a function
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket,
                ans += ", "  # separate items with comma
            ans += str(self.__a[i])  # Add string form of item
        ans += "]"  # Close with right bracket
        return ans

    def bubbleSort(self):  # Sort comparing adjacent vals
        for last in range(self.__nItems - 1, 0, -1):  # and bubble up
            for inner in range(last):  # inner loop goes up to last
                if self.__a[inner] > self.__a[inner + 1]:  # If elem less
                    self.swap(inner, inner + 1)  # than adjacent value, swap

    def selectionSort(self):  # Sort by selecting min and
        for outer in range(self.__nItems - 1):  # swapping min to leftmost
            min = outer  # Assume min is leftmost
            for inner in range(outer + 1, self.__nItems):  # Hunt to right
                if self.__a[inner] < self.__a[min]:  # If we find new min,
                    min = inner  # update the min index

            # __a[min] is smallest among __a[outer]...__a[__nItems-1]
            self.swap(outer, min)  # Swap leftmost and min

    def insertionSort(self):  # Sort by repeated inserts
        for outer in range(1, self.__nItems):  # Mark one element
            temp = self.__a[outer]  # Store marked elem in temp
            inner = outer  # Inner loop starts at mark
            while inner > 0 and temp < self.__a[inner - 1]:  # If marked
                self.__a[inner] = self.__a[inner - 1]  # elem smaller, then
                inner -= 1  # shift elem to right
            self.__a[inner] = temp  # Move marked elem to 'hole'

































































