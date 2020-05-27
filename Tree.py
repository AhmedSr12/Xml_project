from Node import node

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
        if  subTree.listOfNodes[-1].state=='text' or subTree.listOfNodes[-1].state=='close' :
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
        if self.root.state=='empty':
            self.root.state = 'open'
            self.root.openningTag=tag
            if tag.type=='empty':
                self.root.state = 'close'
                self.root.closingTag = tag
            return
        elif self.root.state=='close'or(self.root.state=='text'and self.root.openningTag.type=='no'):
            rootBranch1=node()
            rootBranch1.state='close'
            rootBranch1.openningTag= self.root.openningTag
            rootBranch1.listOfText= self.root.listOfText
            rootBranch1.closingTag=self.root.closingTag
            rootBranch1.listOfNodes=self.root.listOfNodes
            self.root=node()
            self.root.state='passed'
            rootBranch2=node()
            rootBranch2.state = 'open'
            rootBranch2.openningTag=tag
            if tag.type=='empty':
                rootBranch2.state = 'close'
                rootBranch2.closingTag = tag
            self.root.listOfNodes.append( rootBranch1)
            self.root.listOfNodes.append( rootBranch2)
        else :
            self.root.state = 'passed'
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
        else:
            self.addTextSubtree(self.root, text)

    def addClosingTag(self,tag):
        if self.root.state == 'empty':
            self.root.state = 'close'
            self.root.closingTag = tag
        elif self.root.state == 'close':
            rootBranch1 = node()
            rootBranch1.state = 'close'
            rootBranch1.openningTag = self.root.openningTag
            rootBranch1.listOfText = self.root.listOfText
            rootBranch1.closingTag = self.root.closingTag
            rootBranch1.listOfNodes = self.root.listOfNodes
            self.root = node()  # clear root
            self.root.state = 'close'
            self.root.closingTag=tag
            self.root.listOfNodes.append(rootBranch1)
        else :
            self.addClosingSubtree(self.root, tag,0)

    def addClosingSubtree(self,subTree,Tag,founflag):
        if subTree.openningTag.name == Tag.name and subTree.state!='close' :
           if len(subTree.listOfNodes) == 0 :
               founflag=0
           else:
               if subTree.listOfNodes[-1].state == 'close' and subTree.state != 'close':
                   founflag = 0
               else:
                   founflag = 1
        if len(subTree.listOfNodes) == 0 and subTree.state!='close':
           if(founflag==0):
               subTree.state = 'close'
               subTree.closingTag=Tag
               return
           else:
               subTree.state = 'close'
               self.addClosingSubtree(self.root, Tag,0)
               return
        if len(subTree.listOfNodes) != 0:
            if subTree.listOfNodes[-1].state=='close' and subTree.state!='close':
                if (founflag == 0):
                   subTree.state = 'close'
                   subTree.closingTag = Tag
                   return
                else:
                    subTree.state = 'close'
                    self.addClosingSubtree(self.root, Tag, 0)
                    return
        self.addClosingSubtree(subTree.listOfNodes[-1], Tag,founflag)

    def completeTree(self):
        if self.root.openningTag.type=='no' and self.root.closingTag.type=='no':
            self.root.openningTag.name='root'
            self.root.closingTag.name='root'
            self.root.openningTag.type = 'open'
            self.root.closingTag.type = 'close'
            self.root.openningTag.errorvisualized = "(ERR:Missing Root)"
            self.root.openningTag.finalShape = '<' + self.root.openningTag.name + '>'
            self.root.closingTag.errorvisualized = "(ERR:Missing Root)"
            self.root.closingTag.finalShape = '<' + '/'+ self.root.openningTag.name + '>'
            self.errors += 1
        self.completeSubTree(self.root)
        return self.errors
    def completeSubTree(self,subTree):
        if subTree.openningTag.type == 'no' and subTree.closingTag.type != 'no':
            subTree.openningTag.name = subTree.closingTag.name
            subTree.openningTag.type='open'
            subTree.openningTag.errorvisualized = "(ERR:Missing Openning Tag)"
            subTree.openningTag.finalShape = '<' + subTree.openningTag.name + '>'
            self.errors += 1
        elif subTree.openningTag.type != 'no' and subTree.closingTag.type == 'no':
            subTree.closingTag.name = subTree.openningTag.name
            subTree.closingTag.type='close'
            subTree.closingTag.errorvisualized = "(ERR:Missing Closing Tag)"
            subTree.closingTag.finalShape = '<' + '/' + subTree.openningTag.name + '>'
            self.errors += 1
        elif subTree.openningTag.type != 'no' and subTree.closingTag.type != 'no':  # mismatch
            if subTree.openningTag.name != subTree.closingTag.name:
                subTree.closingTag.name = subTree.openningTag.name
                subTree.closingTag.errorvisualized = "(ERR:Not Matching Tag)"
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
            file.write(indentation+subTree.openningTag.errorvisualized+subTree.openningTag.followingComment)
            if len(subTree.listOfText)==1:
                file.write(subTree.listOfText[0].errorvisualized+subTree.listOfText[0].followingComment)
            elif len(subTree.listOfText)>1:
                file.write("\n")
                for i in range(len(subTree.listOfText)):
                    file.write(indentation+"\t"+subTree.listOfText[i].errorvisualized+subTree.listOfText[i].followingComment)
                    if i != len(subTree.listOfText) - 1:
                        file.write("\n")
            if len(subTree.listOfNodes)==0:
                if subTree.openningTag.type!='empty':
                    if len(subTree.listOfText)>1:
                        file.write("\n")
                        file.write(indentation+subTree.closingTag.errorvisualized+subTree.closingTag.followingComment)   #+'\n'??
                    else:
                        file.write(subTree.closingTag.errorvisualized+subTree.closingTag.followingComment)
            else:
                for i in range(len(subTree.listOfNodes)):
                    if i==0:
                        file.write("\n")
                    self.visualizeSubTree(subTree.listOfNodes[i],file,indentation+"\t")
                    file.write("\n")
                if subTree.openningTag.type != 'empty':
                    file.write(indentation+subTree.closingTag.errorvisualized + subTree.closingTag.followingComment)
        else:
            for i in range(len(subTree.listOfText)):
                file.write(indentation + subTree.listOfText[i].errorvisualized + subTree.listOfText[i].followingComment)
                if i !=len(subTree.listOfText)-1:
                    file.write("\n")

    def prettifying(self,file):
        indentation=''
        self.prettifyingSubTree(self.root,file,indentation)

    def prettifyingSubTree(self,subTree,file,indentation):
        if subTree.openningTag.type!='no':
            file.write(indentation+subTree.openningTag.finalShape+subTree.openningTag.followingComment)
            if len(subTree.listOfText)==1:
                file.write(subTree.listOfText[0].finalShape+subTree.listOfText[0].followingComment)
            elif len(subTree.listOfText)>1:
                file.write("\n")
                for i in range(len(subTree.listOfText)):
                    file.write(indentation+"\t"+subTree.listOfText[i].finalShape+subTree.listOfText[i].followingComment)
                    if i != len(subTree.listOfText) - 1:
                        file.write("\n")
            if len(subTree.listOfNodes)==0:
                if subTree.openningTag.type!='empty':
                    if len(subTree.listOfText)>1:
                        file.write("\n")
                        file.write(indentation+subTree.closingTag.finalShape+subTree.closingTag.followingComment)
                    else:
                        file.write(subTree.closingTag.finalShape+subTree.closingTag.followingComment)
            else:
                for i in range(len(subTree.listOfNodes)):
                    if i==0:
                        file.write("\n")
                    self.prettifyingSubTree(subTree.listOfNodes[i],file,indentation+"\t")
                    file.write("\n")
                if subTree.openningTag.type != 'empty':
                    file.write(indentation+subTree.closingTag.finalShape + subTree.closingTag.followingComment)
        else:
            for i in range(len(subTree.listOfText)):
                file.write(indentation + subTree.listOfText[i].finalShape + subTree.listOfText[i].followingComment)
                if i !=len(subTree.listOfText)-1:
                    file.write("\n")

    def minifying(self, file):
        self.minifyingSubTree(self.root, file)

    def minifyingSubTree(self, subTree, file):
        file.write(subTree.openningTag.finalShape + subTree.openningTag.followingComment)
        for i in range(len(subTree.listOfText)):
            file.write(subTree.listOfText[i].finalShape + subTree.listOfText[i].followingComment)
            if i != len(subTree.listOfText) - 1:
                file.write(' ')
        if len(subTree.listOfNodes) == 0:
            if subTree.openningTag.type != 'empty':
                file.write(subTree.closingTag.finalShape + subTree.closingTag.followingComment)
        if len(subTree.listOfNodes) > 0:
            if subTree == self.root:
                file.write("\n")
                for i in range(len(subTree.listOfNodes)):
                    file.write("\t")
                    self.minifyingSubTree(subTree.listOfNodes[i], file)
                    file.write("\n")
            else:
                for i in range(len(subTree.listOfNodes)):
                    self.minifyingSubTree(subTree.listOfNodes[i], file)

            if subTree.openningTag.type != 'empty':
                file.write(subTree.closingTag.finalShape + subTree.closingTag.followingComment)






    def json(self,nodee,level,jsontring):
        if len(nodee.listOfNodes)!=0 or len(nodee.openningTag.listOfAttributes)!=0 or len(nodee.listOfText) != 0 :
            if len(nodee.listOfNodes) == 0:
                if len(nodee.listOfText) == 1 and len(nodee.openningTag.listOfAttributes) == 0:
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + '": "' + nodee.listOfText[0].finalShape + '",')
                elif len(nodee.openningTag.listOfAttributes) == 1 and len(nodee.listOfText) == 0 :
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + '": { "-' +
                                     nodee.openningTag.listOfAttributes[0].name + '": ' +
                                     nodee.openningTag.listOfAttributes[0].finalShape + ' },')
                elif len(nodee.listOfText) != 1 and len(nodee.openningTag.listOfAttributes) == 0:
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + '": "')
                    for i in nodee.listOfText : jsontring.append((level+1) * '  ' +i.finalShape)
                    jsontring.append((level+1) * ' ' + '",')
                elif len(nodee.openningTag.listOfAttributes) != 1 and len(nodee.listOfText) == 0 :
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + '": {')
                    for i in nodee.openningTag.listOfAttributes :
                        if i == nodee.openningTag.listOfAttributes[-1] :
                            jsontring.append((level + 1) * '  ' + '"-' +i.name + '": ' +i.finalShape+'')
                            jsontring.append(level * '  ' + '},')
                        else: jsontring.append((level + 1) * '  ' + '"-' +i.name + '": ' +i.finalShape+',')
                else :
                    jsontring.append(level * '  ' + '"' + nodee.openningTag.name + '": {')
                    for i in nodee.openningTag.listOfAttributes:
                        jsontring.append((level + 1) * '  ' + '"-' + i.name + '": ' + i.finalShape + ',')
                    jsontring.append((level + 1) * '  ' +'"#text": "  ' +  nodee.listOfText[0].finalShape )
                    for i in nodee.listOfText[1:]: jsontring.append((level + 1) * '   ' + i.finalShape)
                    s= jsontring[-1]+'"'
                    del jsontring[-1]
                    jsontring.append(s)
                    jsontring.append(level * '  ' + '},')
            else :

                del_nodes=[]
                jsontring.append(level * '  ' + '"' + nodee.openningTag.name + '": {')
                for k in nodee.openningTag.listOfAttributes:
                    jsontring.append((level + 1) * '  ' + '"-' + k.name + '": ' + k.finalShape + ',')
                list_of_list_of_texts = []
                if nodee.listOfText != []: list_of_list_of_texts.append(nodee.listOfText)
                for i in range(len(nodee.listOfNodes)):
                    if i not in del_nodes :
                        if nodee.listOfNodes[i].openningTag.type == 'no': list_of_list_of_texts.append(nodee.listOfNodes[i].listOfText)
                        else :
                            tmp = nodee.listOfNodes[i + 1:]
                            one_node_flag = 1
                            for j in range(len(tmp)):
                                if nodee.listOfNodes[i].openningTag.name == tmp[j].openningTag.name:
                                    del_nodes.append(j + i + 1)
                                    if one_node_flag == 1:
                                        one_node_flag = 0
                                        jsontring.append(
                                            (level + 1) * '  ' + '"' + nodee.listOfNodes[i].openningTag.name + '": [')
                                        self.repeated_json(nodee.listOfNodes[i], level + 1, jsontring)
                                    self.repeated_json(tmp[j], level + 1, jsontring)
                            if one_node_flag == 0:
                                temp2_str = jsontring[-1][:-1]
                                del jsontring[-1]
                                jsontring.append(temp2_str)
                                jsontring.append((level + 1) * '  ' + '],')
                            if one_node_flag == 1: self.json(nodee.listOfNodes[i], level + 1, jsontring)

                if list_of_list_of_texts != []: jsontring.append((level + 1) * '  ' + '"#text": ')
                for w in list_of_list_of_texts:
                    jsontring.append((level + 1) * '  ' + '"')
                    for e in w: jsontring.append((level + 1) * '  ' + e.finalShape)
                    jsontring.append((level + 1) * '  ' + '",')
                temp2_str = jsontring[-1][:-1]
                del jsontring[-1]
                jsontring.append(temp2_str)
                jsontring.append(level * '  ' + '},')




    def repeated_json(self,nodee,level,jsontring):
        if len(nodee.listOfNodes) != 0 or len(nodee.openningTag.listOfAttributes) != 0 or len(nodee.listOfText) != 0:
            if len(nodee.listOfNodes) == 0:
                if len(nodee.listOfText) == 1 and len(nodee.openningTag.listOfAttributes) == 0:
                    jsontring.append(
                        level * '  ' + '"' + nodee.listOfText[0].finalShape + '",')
                elif len(nodee.openningTag.listOfAttributes) == 1 and len(nodee.listOfText) == 0:
                    jsontring.append(level * '  '  + '{ "-' +
                                     nodee.openningTag.listOfAttributes[0].name + '": ' +
                                     nodee.openningTag.listOfAttributes[0].finalShape + ' },')
                elif len(nodee.listOfText) != 1 and len(nodee.openningTag.listOfAttributes) == 0:
                    jsontring.append(level * '  ' + ': "')
                    for i in nodee.listOfText: jsontring.append((level + 1) * '  ' + i.finalShape)
                    jsontring.append((level + 1) * ' ' + '",')
                elif len(nodee.openningTag.listOfAttributes) != 1 and len(nodee.listOfText) == 0:
                    jsontring.append(level * '  ' +  ' {')
                    for i in nodee.openningTag.listOfAttributes:
                        if i == nodee.openningTag.listOfAttributes[-1]:
                            jsontring.append((level + 1) * '  ' + '"-' + i.name + '": ' + i.finalShape + '')
                            jsontring.append(level * '  ' + '},')
                        else:
                            jsontring.append((level + 1) * '  ' + '"-' + i.name + '": ' + i.finalShape + ',')
                else:
                    jsontring.append(level * '  ' +  ' {')
                    for i in nodee.openningTag.listOfAttributes:
                        jsontring.append((level + 1) * '  ' + '"-' + i.name + '": ' + i.finalShape + ',')
                    jsontring.append((level + 1) * '  ' + '"#text": "  ' + nodee.listOfText[0].finalShape)
                    for i in nodee.listOfText[1:]: jsontring.append((level + 1) * '   ' + i.finalShape)
                    s = jsontring[-1] + '"'
                    del jsontring[-1]
                    jsontring.append(s)
                    jsontring.append(level * '  ' + '},')
            else:

                del_nodes = []
                jsontring.append(level * '  ' +  '{')
                for k in nodee.openningTag.listOfAttributes:
                    jsontring.append((level + 1) * '  ' + '"-' + k.name + '": ' + k.finalShape + ',')
                list_of_list_of_texts = []
                if nodee.listOfText != []: list_of_list_of_texts.append(nodee.listOfText)
                for i in range(len(nodee.listOfNodes)):
                    if i not in del_nodes:
                        if nodee.listOfNodes[i].openningTag.type == 'no': list_of_list_of_texts.append(nodee.listOfNodes[i].listOfText)
                        else :
                            tmp = nodee.listOfNodes[i + 1:]
                            one_node_flag = 1
                            for j in range(len(tmp)):
                                if nodee.listOfNodes[i].openningTag.name == tmp[j].openningTag.name:
                                    del_nodes.append(j + i + 1)
                                    if one_node_flag == 1:
                                        one_node_flag = 0
                                        jsontring.append(
                                            (level + 1) * '  ' + '"' + nodee.listOfNodes[i].openningTag.name + '": [')
                                        self.repeated_json(nodee.listOfNodes[i], level + 1, jsontring)
                                    self.repeated_json(tmp[j], level + 1, jsontring)
                            if one_node_flag == 0:
                                temp2_str = jsontring[-1][:-1]
                                del jsontring[-1]
                                jsontring.append(temp2_str)
                                jsontring.append((level + 1) * '  ' + '],')
                            if one_node_flag == 1: self.json(nodee.listOfNodes[i], level + 1, jsontring)

                if list_of_list_of_texts != []: jsontring.append((level + 1) * '  ' + '"#text": ')
                for w in list_of_list_of_texts:
                    jsontring.append((level + 1) * '  ' + '"')
                    for e in w: jsontring.append((level + 1) * '  ' + e.finalShape)
                    jsontring.append((level + 1) * '  ' + '",')
                temp2_str = jsontring[-1][:-1]
                del jsontring[-1]
                jsontring.append(temp2_str)
                jsontring.append(level * '  ' + '},')


    def print_json(self):
        main_string=[]
        main_string.append('{')
        self.json(self.root,1,main_string)
        temp2_str = main_string[-1][:-1]
        del main_string[-1]
        main_string.append(temp2_str)
        main_string.append('}')
        return '\n'.join(main_string)

    def no_synsets(self):
        n=0
        if self.root.openningTag.name == 'synset' : n=1
        return str(self.synsets(self.root,n))



    def synsets(self,x,n):

        for i in x.listOfNodes :
            if i.openningTag.name == 'synset' : n= n+1
            n=self.synsets(i,n)
        return n




    def def_word(self,x,word):
        for i in x.listOfNodes :
            if i.listOfText !=[] :
                if i.openningTag.name == 'word' and i.listOfText[0].finalShape == word:
                    for j in x.listOfNodes:
                        if j.openningTag.name == 'def':
                            r=[]
                            for k in j.listOfText : r.append(k.finalShape)
                            return '\n'.join(r)
            s=self.def_word(i,word)
            if s != None : return s

    def def_of_word(self,s):
        return self.def_word(self.root,s)


    def hyper(self, x, word):
        for i in x.listOfNodes:
            if i.listOfText != []:
                if i.openningTag.name == 'word' and i.listOfText[0].finalShape == word:
                    for j in x.listOfNodes:
                        if j.openningTag.name == 'pointer' and j.listOfText[0].finalShape == 'Hypernym':
                            for k in j.openningTag.listOfAttributes:
                                if k.name == 'refs':
                                    refs = k.finalShape[1:-1]
                                    ids = refs.split()
                                    result = []
                                    for l in ids:
                                        self.search_in_tree(self.root, l, result)
                                    if result == []:
                                        return refs
                                    else:
                                        return ' '.join(result)
            r= self.hyper(i, word)
            if r!= None : return r


    def search_in_tree(self, x, id, result):
        for i in x.listOfNodes:
            for j in i.openningTag.listOfAttributes:
                if j.name == 'id' and j.finalShape[1:-1] == id:
                    for k in i.listOfNodes:
                        if k.openningTag.name == 'word': result.append(k.listOfText[0].finalShape)
            self.search_in_tree(i, id, result)

    def hyper_of_word(self, word):
        return self.hyper(self.root, word)



