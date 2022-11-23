#Implement a Queue data structure using a Python list

class Queue(object):
    def __init__(self, size):                   #constructor
        self.__maxSize= size                    #Size of a (circular) array
        self.__que=[None]*size                  #Queue stored as a list
        self.__front=1                          #Empty Queue has front 1
        self.__rear=0                           #after rear and
        self.__nItems=0                         # No items in queue


    def insert(self, item):                     #instert item at rear
        if self.isFull():                       #if not full
            raise Exception("Queue overflow")
        self.__rear+=1                          #Rear moves one to the right
        if self.__rear==self.__maxSize:         #Wrap around circular array--rear and maxSize are the same
            self.__rear=0
        self.__que[self.__rear]= item           #Store item at rear
        self.__nItems+=1
        return True


    def remove(self):                           #Remove front item of queue ( look, no argument in the method)
        if self.isEmpty():                      #and return it, if not empty
            raise  Exception("Queue under flow---no items in it")
        front=self.__que[self.__front]           #get the value at front
        self.__que[self.__front]=None            #remove item reference
        self.__front+=1                          #frot move on to the right
        if self.__front==self.__maxSize:         #Wrap around circular array
            self.__front=0
        self.__nItems-=1
        return front


    def peek(self):                                 #Return front most item
        return None if self.isEmpty() else self.__que[self.__front]

    def isEmpty(self): return self.__nItems==0

    def isFull(self): return self.__nItems==self.__maxSize

    def __len__(self): return self.__nItems

    def __str__(self):                              #convert queue to string
        ans="["                                     #start with left bracket
        for i in range(self.__nItems):              #loop through current items
            if len(ans)>1:                          #Except next to left bracket
                ans+=","                            #Separate item with comma

            j=i+ self.__front                       # offset from front
            if j>=self.__maxSize:                   #Wrap around circular array
                j-=self.__maxSize
            ans+=str(self.__que[j])                 # Add string form of item
        ans+="]"                                    #close with right bracket
        return ans





