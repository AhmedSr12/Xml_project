from Node import node
from Text import text
from Tag import tag
import copy
class tree:
    def __init__(self):
        self.root=node()
        self.errors=0
    def addOpenningSubtree(self,subTree,tag):
        if len(subTree.listOfNodes)==0  :
            newNode=node()
            newNode.state='open'
            newNode.openningTag=tag
            if tag.type == 'empty':
                newNode.state = 'close'
                newNode.closingTag = tag
            subTree.listOfNodes.append(newNode)
            return
        if  subTree.listOfNodes[-1].state=='text' or subTree.listOfNodes[-1].state=='close' : #lazem
            newNode = node()
            newNode.state='open'
            newNode.openningTag = tag
            if tag.type == 'empty':
                newNode.state = 'close'
                newNode.closingTag = tag
            subTree.listOfNodes.append(newNode)
            return
        self.addOpenningSubtree(subTree.listOfNodes[-1],tag)

    def addOpenningTag(self,tag):
        if self.root.state=='empty':   #root is empty
            self.root.state = 'open'
            self.root.openningTag=tag
            if tag.type=='empty':
                self.root.state = 'close'
                self.root.closingTag = tag
            return
        else :
            self.root.state == 'passed'  #to change text state
            self.addOpenningSubtree(self.root,tag)



    def addTextSubtree(self,subTree,text):
        if len(subTree.listOfNodes) == 0:
            subTree.state = 'text'
            subTree.listOfText.append(text)
            return
        if  subTree.listOfNodes[-1].state == 'close':
            newNode = node()
            newNode.state = 'text'
            newNode.listOfText.append(text)
            subTree.listOfNodes.append(newNode)
            return

        self.addTextSubtree(subTree.listOfNodes[-1], text)


    def addText(self,text):
        if self.root.state == 'empty'or self.root.state=='text':
            self.root.state = 'text'
            self.root.listOfText.append(text)
            return
        #if len(self.root.listOfNodes)==0:
        #   self.root.text=text
        else:
            self.addTextSubtree(self.root, text)

    def addClosingTag(self,tag): #hal lazem 3la 2 fns
        if self.root.state == 'empty':#not empty but may need close
            self.root.state = 'close'
            self.root.closingTag = tag
        else :
            #self.root.state == 'passed'
            self.addClosingSubtree(self.root, tag)

    def addClosingSubtree(self,subTree,Tag):
        if subTree.openningTag.name == Tag.name and subTree.state!='close' :
            subTree.closingTag=Tag
            subTree.state='close'
            return
        if subTree.openningTag.name == Tag.name and subTree.state == 'close':
            newNode=node()
            newNode.listOfText=subTree.listOfText
            subTree.listOfText=[]
            newNode.closingTag = subTree.closingTag
            subTree.closingTag=Tag
            subTree.listOfNodes.insert(0,newNode)
            subTree.state = 'close'
            return



        if len(subTree.listOfNodes) == 0 and subTree.state!='close':#if passed so has children
            subTree.state = 'close'
            subTree.closingTag=Tag
            return
        if len(subTree.listOfNodes) == 0 : #lazem? #Bb Bc
            newNode = node()
            newNode.state = 'close'
            newNode.openningTag=subTree.openningTag
            subTree.openningTag=tag()
            newNode.listOfText = subTree.listOfText
            subTree.listOfText = []
            newNode.closingTag = subTree.closingTag
            subTree.closingTag = Tag


            subTree.listOfNodes.append(newNode)
            return
        if len(subTree.listOfNodes) != 0: #Cc
            if subTree.listOfNodes[-1].state=='close' and subTree.state!='close':
                subTree.state = 'close'
                subTree.closingTag = Tag
                return


        self.addClosingSubtree(subTree.listOfNodes[-1], Tag)


    def printTree(self,file):
        #self.printSubTree(self.root)
        self.printSubTreeFile(self.root, file)

    def printSubTreeold(self, subTree):
        if len(subTree.listOfNodes) == 0:
            if subTree.openningTag.type == 'no' and subTree.closingTag.type == 'no':  # m3molha creation
                for i in range(len(subTree.listOfText)):
                    print(subTree.listOfText[i].originalShape)
                return
            if subTree.openningTag.type == 'empty':
                print(subTree.openningTag.originalShape)
                return
            if subTree.openningTag.type == 'no':
                print('〔ERROR7〕')
            else:
                print(subTree.openningTag.originalShape)
            if subTree.listOfText != []:
                for i in range(len(subTree.listOfText)):
                    print(subTree.listOfText[i].originalShape)
            if subTree.closingTag.type == 'no':
                print('〔ERROR8〕')
            elif subTree.closingTag.name != subTree.openningTag.name:
                print('〔ERROR9〕')
            else:
                print(subTree.closingTag.originalShape)

        else:
            for i in range(len(subTree.listOfNodes)):
                self.printSubTree(subTree.listOfNodes[i])
    def printSubTree(self,subTree):
        if subTree.openningTag.type == 'empty':
            print(subTree.openningTag.originalShape)
            return

        if subTree.openningTag.type!='no':
            print(subTree.openningTag.originalShape)
            if len(subTree.listOfText) != 0:
                for i in range (len(subTree.listOfText)):
                    print(subTree.listOfText[i].originalShape)
            if len(subTree.listOfNodes) != 0:
                for i in range(len(subTree.listOfNodes)):
                    self.printSubTree(subTree.listOfNodes[i])
            if subTree.closingTag.type != 'no':
                if subTree.closingTag.name != subTree.openningTag.name:
                   print('〔ERROR7〕') #notmatching
                else:
                    print(subTree.closingTag.originalShape)
                return
            else:
                print('〔ERROR8〕')  # missing closing
                return
        else:
            if subTree.closingTag.type=='no':
                for i in range (len(subTree.listOfText)):
                    print(subTree.listOfText[i].originalShape)
                return
            else:
                print('〔ERROR9〕')  # missing opening
                if len(subTree.listOfText) != 0:
                    for i in range(len(subTree.listOfText)):
                        print(subTree.listOfText[i].originalShape)
                if len(subTree.listOfNodes) != 0:
                    for i in range(len(subTree.listOfNodes)):
                         self.printSubTree(subTree.listOfNodes[i])

                print(subTree.closingTag.originalShape)
                return
    def printSubTreeFile(self,subTree,file):
        if subTree.openningTag.type == 'empty':
            file.write(subTree.openningTag.originalShape+"\n")
            #file.write("\n")
            return

        if subTree.openningTag.type!='no':
            file.write(subTree.openningTag.originalShape+'\n'+'\t')
            #file.write("\n")

            if len(subTree.listOfText) != 0:
                for i in range (len(subTree.listOfText)):
                    file.write(subTree.listOfText[i].originalShape+"\n")
                    #file.write("\n")

            if len(subTree.listOfNodes) != 0:
                for i in range(len(subTree.listOfNodes)):
                    self.printSubTreeFile(subTree.listOfNodes[i],file)
            if subTree.closingTag.type != 'no':
                if subTree.closingTag.name != subTree.openningTag.name:
                   file.write('〔ERROR7〕'+"\n") #notmatching
                   #file.write("\n")

                else:
                    file.write(subTree.closingTag.originalShape+"\n")
                    #file.write("\n")

                return
            else:
                file.write('〔ERROR8〕'+"\n")  # missing closing
                #file.write("\n")

                return
        else:
            if subTree.closingTag.type=='no':
                for i in range (len(subTree.listOfText)):
                    file.write(subTree.listOfText[i].originalShape+"\n")
                    #file.write("\n")

                return
            else:
                file.write('〔ERROR9〕'+"\n")  # missing opening
                #file.write("\n")

                if len(subTree.listOfText) != 0:
                    for i in range(len(subTree.listOfText)):
                        file.write(subTree.listOfText[i].originalShape+"\n")
                        #file.write("\n")

                if len(subTree.listOfNodes) != 0:
                    for i in range(len(subTree.listOfNodes)):
                         self.printSubTreeFile(subTree.listOfNodes[i],file)

                file.write(subTree.closingTag.originalShape+"\n")
                #file.write("\n")

                return

    def completeTree(self):
        self.completeSubTree(self.root)
        return self.errors
    def completeSubTree(self,subTree):
        if subTree.openningTag.type == 'no' and subTree.closingTag.type != 'no':
            #print(1)
            subTree.openningTag.name = subTree.closingTag.name
            subTree.openningTag.errorvisualized = '〔ERROR9〕'
            subTree.openningTag.finalShape = '<' + subTree.openningTag.name + '>'
            self.errors += 1
        elif subTree.openningTag.type != 'no' and subTree.closingTag.type == 'no':
            #print(2)
            subTree.closingTag.name = subTree.openningTag.name
            subTree.closingTag.errorvisualized = '〔ERROR8〕'
            subTree.closingTag.finalShape = '<' + '/' + subTree.openningTag.name + '>'
            self.errors += 1
        elif subTree.openningTag.type != 'no' and subTree.closingTag.type != 'no':  # mismatch
            if subTree.openningTag.name != subTree.closingTag.name:
                #print(3)
                subTree.closingTag.name = subTree.openningTag.name
                subTree.closingTag.errorvisualized = '〔ERROR7〕'
                subTree.closingTag.finalShape = '<' + '/' + subTree.openningTag.name + '>'
                self.errors += 1


        if len(subTree.listOfNodes) != 0:
            for i in range(len(subTree.listOfNodes)):
                self.completeSubTree(subTree.listOfNodes[i])

    def visualizeErrors(self,file):
        indentation=''
        self.visualizeSubTree(self.root,file,indentation)

    def visualizeSubTree(self,subTree,file,indentation):
        if subTree.openningTag.type!='no':
            file.write(subTree.closingTag.originalShape + "\n")











































    def json(self,nodee,level,jsontring):
        if len(nodee.listOfNodes)!=0 or len(nodee.openningTag.listOfAttributes)!=0 or len(nodee.listOfText) != 0 :
            if len(nodee.listOfNodes) == 0:
                if len(nodee.listOfText) == 1 and len(nodee.openningTag.listOfAttributes) == 0:
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + '": "' + nodee.listOfText[0].finalShape + '"')
                if len(nodee.openningTag.listOfAttributes) == 1 and len(nodee.listOfText) == 0 :
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + ': { "-' +
                                     nodee.openningTag.listOfAttributes[0].name + '": "' +
                                     nodee.openningTag.listOfAttributes[0].finalShape + '" }')
                if len(nodee.listOfText) != 1 and len(nodee.openningTag.listOfAttributes) == 0:
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + '": "')
                    for i in nodee.listOfText : jsontring.append((level+1) * '  ' +i.finalShape)
                    jsontring.append((level+1) * ' ' + '"')
                if len(nodee.openningTag.listOfAttributes) != 1 and len(nodee.listOfText) == 0 :
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + ': {')
                    for i in nodee.openningTag.listOfAttributes :
                        if i == nodee.openningTag.listOfAttributes[-1] :
                            jsontring.append((level + 1) * '  ' + '"-' +i.name + '": "' +i.finalShape+'"')
                            jsontring.append(level * '  ' + '}')
                        else: jsontring.append((level + 1) * '  ' + '"-' +i.name + '": "' +i.finalShape+'",')
                else :
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + ': {')
                    for i in nodee.openningTag.listOfAttributes:
                        jsontring.append((level + 1) * '  ' + '"-' + i.name + '": "' + i.finalShape + '"')
                    jsontring.append(' "#text": "')
                    for i in nodee.listOfText: jsontring.append((level + 1) * '  ' + i.finalShape)
                    jsontring.append((level + 1) * ' ' + '"')
                    jsontring.append(level * '  ' + '}')

            else :
                tmp_nodes=copy.deepcopy(nodee.listOfNodes)
                del_nodes=[]
                for i in range(len(tmp_nodes)):
                    s=level * '  ' + '"' + nodee.openningTag.name + '":'
                    tmp=tmp_nodes[i+1:]
                    one_node_flag=1
                    for j in range(len(tmp)) :
                        if tmp_nodes[i].openningTag.name == tmp[j].openningTag.name :
                            del_nodes.append(j)
                            if one_node_flag==1 :
                                one_node_flag = 0
                                s = s + ' ['
                                jsontring.append(s)
                                self.repeated_json(tmp_nodes[i], level + 1, jsontring)
                            self.repeated_json(tmp[j], level + 1, jsontring)
                            temp_str = jsontring[-1] +','
                            del jsontring[-1]
                            jsontring.append(temp_str)
                    temp2_str= jsontring[-1][:-1]
                    del jsontring[-1]
                    jsontring.append(temp2_str)
                    for r in del_nodes :  del tmp_nodes[r]
                    if one_node_flag == 1 :
                        s=s+' {'
                        jsontring.append(s)
                        for k in tmp_nodes[i].openningTag.listOfAttributes :
                            jsontring.append((level + 1) * '  ' + '"-' + k.name + '": "' + k.finalShape + '",')
                        list_of_list_of_texts =[]
                        if tmp_nodes[i].listOfText != [] : list_of_list_of_texts.append(tmp_nodes[i].listOfText)
                        for q in tmp_nodes[i].listOfNodes :
                            if q.openningTag.type =='no' : list_of_list_of_texts.append(q.listOfText)
                            else : self.json(q,level+1,jsontring)
                        if list_of_list_of_texts != [] : jsontring.append(' "#text": "')
                        for w in list_of_list_of_texts :
                            for e in w :  jsontring.append((level + 1) * '  ' + e.finalShape)
                        jsontring.append(level * '  ' + '}')

    def repeated_json(self,nodee,level,jsontring):
        if len(nodee.listOfNodes) != 0 or len(nodee.openningTag.listOfAttributes) != 0 or len(nodee.listOfText) != 0:
            if len(nodee.listOfNodes) == 0:
                if len(nodee.listOfText) == 1 and len(nodee.openningTag.listOfAttributes) == 0:
                    jsontring.append(level * '  ' + '"'  + nodee.listOfText[0].finalShape + '"')
                if len(nodee.openningTag.listOfAttributes) == 1 and len(nodee.listOfText) == 0:
                    jsontring.append(level * '  ' +  '"-' +
                                     nodee.openningTag.listOfAttributes[0].name + '": "' +
                                     nodee.openningTag.listOfAttributes[0].finalShape + '" }')
                if len(nodee.listOfText) != 1 and len(nodee.openningTag.listOfAttributes) == 0:
                    jsontring.append(level * '  ' + '"')
                    for i in nodee.listOfText: jsontring.append((level + 1) * '  ' + i.finalShape)
                    jsontring.append((level + 1) * ' ' + '"')
                if len(nodee.openningTag.listOfAttributes) != 1 and len(nodee.listOfText) == 0:
                    jsontring.append(level * '  ' + '{')
                    for i in nodee.openningTag.listOfAttributes:
                        if i == nodee.openningTag.listOfAttributes[-1]:
                            jsontring.append((level + 1) * '  ' + '"-' + i.name + '": "' + i.finalShape + '"')
                            jsontring.append(level * '  ' + '}')
                        else:
                            jsontring.append((level + 1) * '  ' + '"-' + i.name + '": "' + i.finalShape + '",')
                else:
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + ': {')
                    for i in nodee.openningTag.listOfAttributes:
                        jsontring.append((level + 1) * '  ' + '"-' + i.name + '": "' + i.finalShape + '"')
                    jsontring.append(' "#text": "')
                    for i in nodee.listOfText: jsontring.append((level + 1) * '  ' + i.finalShape)
                    jsontring.append((level + 1) * ' ' + '"')
                    jsontring.append(level * '  ' + '}')

            else:
                tmp_nodes = copy.deepcopy(nodee.listOfNodes)
                del_nodes = []
                for i in range(len(tmp_nodes)):
                    s = level * '  '
                    tmp = tmp_nodes[i + 1:]
                    one_node_flag = 1
                    for j in range(len(tmp)):
                        if tmp_nodes[i].openningTag.name == tmp[j].openningTag.name:
                            del_nodes.append(j)
                            if one_node_flag == 1:
                                one_node_flag = 0
                                s = s + ' ['
                                jsontring.append(s)
                                self.repeated_json(tmp_nodes[i], level + 1, jsontring)
                            self.repeated_json(tmp[j], level + 1, jsontring)
                            temp_str = jsontring[-1] + ','
                            del jsontring[-1]
                            jsontring.append(temp_str)
                    if one_node_flag == 0:
                        temp2_str = jsontring[-1][:-1]
                        del jsontring[-1]
                        jsontring.append(temp2_str)
                        for r in del_nodes:  del tmp_nodes[r]
                    if one_node_flag == 1:
                        s = s + ' {'
                        jsontring.append(s)
                        for k in tmp_nodes[i].openningTag.listOfAttributes:
                            jsontring.append((level + 1) * '  ' + '"-' + k.name + '": "' + k.finalShape + '",')
                        list_of_list_of_texts = []
                        if tmp_nodes[i].listOfText != []: list_of_list_of_texts.append(tmp_nodes[i].listOfText)
                        for q in tmp_nodes[i].listOfNodes:
                            if q.openningTag.type == 'no':
                                list_of_list_of_texts.append(q.listOfText)
                            else:
                                self.json(q, level + 1, jsontring)
                        if list_of_list_of_texts != []: jsontring.append(' "#text": "')
                        for w in list_of_list_of_texts:
                            for e in w:  jsontring.append((level + 1) * '  ' + e.finalShape)
                        jsontring.append(level * '  ' + '}')

    def print_json(self):
        main_string=[]
        main_string.append('{')
        self.json(self.root,1,main_string)
        main_string.append('}')
        return '\n'.join(main_string)







