
# coding: utf-8

# In[18]:


#class Jukebox(Selector, paymentModule):
class Jukebox():
    def __init__(self, recordSet, price):
        self.recordSet = recordSet
        self.price = price
    def __str__(self):
        return str(self.value)
    
    #other necessary Jukebox specific 


# In[19]:


class RecordSet:
    def __init__(self, setName, records):
        self.setName = setName
        self.records = records
        
    def recordExists(record):
        if record in records:
            return True
        else:
            return False
    
    #def addRecord(record):
        #add record to the recordset
    
    #other recordset functions


# In[20]:


import sys

class Selector(RecordSet):
    def getRecordSelection():
        recordSelection = raw_input("Enter record selection: ")
        validInput = recordExists(recordSelection) 
        if validInput: 
            print ("Playing record...")
        else:
            print ("Record does not exist. Select another record: ")
            recordSelection = raw_input()
    
    #def search(recordName):
        #search record set for a record
        #return records with a similar or exact name
        
    #other select functions
            


# In[1]:


#class paymentModule(playRecordPrice):
class paymentModule():
    def __init__(self, playRecordPrice):
        self.playRecordPrice = playRecordPrice
    
    #def pay(inputAmount):
        #check if payment is adequate
        #refund if necessary
        #otherwise prompt for more money
        
    #other paymentModule functions

