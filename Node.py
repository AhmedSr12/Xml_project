from Tag import tag
from Text import text
class node:
    def __init__(self):
        self.openingTag=tag()
        self.text=text()
        self.closingtag=tag()
        self.listOfNodes=[]
