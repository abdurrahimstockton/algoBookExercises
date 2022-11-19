#Implement an Array data structure as simplified type of list

class Array(object):
    def __init__(self, initialSize):                #constructor
        self.__a=[None]*initialSize                 #The array stored as a list
        self.__nItems=0                             #No items in array initially

    def __len__(self):                              #special function , returning number of items
        return self.__nItems

    def get(self,n):                                # Return the value at index n
        if 0<=n and n<self.__nItems:                # Check if n is in the bounds
            return self.__a[n]                      #Only return  if in bounds

    def set(self, n, value):                        # Set the value at index n
        if 0<=n and n<self.__nItems:                # Check if n is in bounds
            self.__a[n]=value                       # only set item if in bounds

    def insert(self, item):                         # Insert item at end
        self.__a[self.__nItems]=item                # item goes at current end
        self.__nItems+=1                            #Increment number of items

    def find(self,item):                            #Find index for item
        for j in range(self.__nItems):              #Among current items
                if self.__a[j]==item:               #if found,
                    return j                        #then return index to item
        return -1                                   # If not found, return -1

    def search(self, item):                         #Search for item
        return self.get(self.find(item))            #and return item if found

    def delete(self, item):                         #Delete first occurence
        for j in range(self.__nItems):              # of an item
            if self.__a[j]==item:                   # Found item?
                self.__nItems-=1                    #One fewer at end
                for k in range(j, self.__nItems):   #Move items from
                    self.__a[k]=self.__a[k+1]       #right over 1
                    return True
        return False                                #If item was not found

    def traverse(self,function=print):              #Traverse all items
        for j in range(self.__nItems):              #And apply function
            function(self.__a[j])




























