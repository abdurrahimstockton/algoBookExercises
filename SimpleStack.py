#Stack exercises
#Implement a Stack data structre using a Python list

class Stack(object):
    def __init__(self, max):  #constructor
        self.__stackList=[None]*max #The stack stored as a list
        self.__top=-1 #No items initially //-1 to check stack before copying and pushing anything in the stack

    def push(self, item):  #Insert item at top of the stack
        self.__top+=1 #Advance the pointer
        self.__stackList[self.__top]=item # store item

    def pop(self):  #Remove top item from the stack
        top=self.__stackList[self.__top] #Top item
        self.__stackList[self.__top]= None # Remove item reference
        self.__top-=1 #Decrease the pointer
        return top #Return top item

    def peek(self):  #Return top item
        if not self.isEmpty(): #if stack is not empty
            return self.__stackList[self.__top]  #Return top item

    def isEmpty(self): # Check if the stack is empty
        return self.__top<0

    def isFull(self): #Chek if the stack is full
        return self.__top>=len(self.__stackList)-1

    def __len__(self): #Returns number of items on the stack
        return self.__top+1

    def __str__(self): #Convert stack to string
        ans="["  #start with left bracket
        for i in range(self.__top+1):
            if len(ans)>1: #Except next to left bracket
                ans+=","
            ans+=str(self.__stackList[i]) #Add string form of item
        ans+="]"
        return ans

#End of Class
