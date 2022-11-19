#Implement an ordered Array data strucutre

class OrderedArray(object):
    def __init__(self, initialSize):   #Constructor
        self.__a=[None]*initialSize # The array stored as a list
        self.__nItems=0  #No items in array initially

    def __len__(self):   #Special len function, returning the number of items in the array
        return self.__nItems

    def get(self,n):   #Return the value at index n
        if 0<=n and n<self.__nItems: #Check if n is in bounds
            return self.__a[n]  #only return item if in bounds
        raise IndexError(f"Index {str(n)} is out of range ")

    #Set function is not requrired. If set function is introduced, that would allow users to change values in ways the not keep items in order

    def traverse(self,function=print): #Traverse all items and apply a function
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):   #special str function
        ans="["
        for i in range (self.__nItems): #loop through the items
            if len(ans)>1: #except next to the left bracket
                ans+=","  #separate items with comma
            ans+=str(self.__a[i])  #add string from item
        ans+="]"  #close the right bracket
        return ans


    def find(self, item):  #Find index at or just below
        lo=0    #item in ordered list
        hi=self.__nItems-1 #look between lo and high

        while lo<=hi:
            mid=(lo+hi)//2   #select mid point
            if self.__a[mid]==item: #Did we find it at mid point?
                return mid  #Return location of item
            elif self.__a[mid]<item: #is item in upper half?
                lo=mid +1 # increase the lo boundary
            else:
                hi=mid-1  #if item is in the lower half, lower the hi boundary
        return lo  #Item not found, return insertion point instead


    def search(self, item):
        index=self.find(item)   #Search for item
        if index<self.__nItems and self.__a[index]==item:
            return self.__a[index]  #and return item if found

    def insert(self, item): #Insert item into correct position
        if self.__nItems>=len(self.__a): #if array is full
            raise Exception("Array overflow")  #raise exception

        index=self.find(item) #Find index where item should go
        for j in range (self.__nItems, index, -1): #move bigger items to the right
            self.__a[j]=self.__a[j-1]

        self.__a[index]= item   #Insert the item
        self.__nItems+=1 #Increase the number of items


    def delete(self,item):   #Delete any occurance
        j=self.find(item) # Try to find the item
        if j<self.__nItems and self.__a[j]==item: #if found
            self.__nItems-=1 #one fewer at the end
            for k in range(j, self.__nItems): #Move bigger items to the left
                self.__a[k]=self.__a[k+1]
                return True   #return success flag
        return False # If item not found

#End of Class 