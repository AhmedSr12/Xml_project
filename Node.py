from Tag import tag
from Text import text
class node:
    def __init__(self):
        self.state='empty'
        self.openningTag=tag()
        #self.openingTag.type='no'
        self.listOfText=[]
        self.closingTag=tag()
        #self.closingtag.type='no'
        self.listOfNodes=[]
