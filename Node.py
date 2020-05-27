from Tag import tag
class node:
    def __init__(self):
        self.state='empty'
        self.openningTag=tag()
        self.listOfText=[]
        self.closingTag=tag()
        self.listOfNodes=[]
