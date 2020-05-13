from Node import node
from Text import text
class tree:
    def __init__(self):
        self.root=node()
    def createNodeSubtree(self,subTree,tag):
        if len(subTree.listOfNodes)==0  :
            newNode=node()
            newNode.openingTag=tag
            subTree.listOfNodes.append(newNode)
        if  subTree.listOfNodes[-1].closingtag.name!='':
            newNode = node()
            newNode.openingTag = tag
            subTree.listOfNodes.append(newNode)
        if subTree.listOfNodes[-1].closingtag.name=='':
            self.createNode(subTree.listOfNodes[-1],tag)

    def createNode(self,tag):
        if self.root.openingTag.name=='':   #root is empty
            self.root.openingTag=tag
        else :
            self.createNode(self.root,tag)


    def addTextSubtree(self,subTree,text):
        if len(subTree.listOfNodes) == 0:
            subTree.text=text
        else :
            self.addTextSubtree(subTree.listOfNodes[-1], text)


    def addText(self,text):
        if len(self.root.listOfNodes)==0:
            self.root.text=text
        else:
            self.addTextSubtree(self.root, text)



