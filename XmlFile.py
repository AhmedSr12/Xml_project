from Text import text
from Tag import tag
from Tree import tree
from Attribute import attribute
import re


class errors:
    def __init__(self, number=0, name='', description='', replacement=''):
        self.number = number
        self.name = name
        self.description = description
        self.replacement = replacement


class xmlFile:
    def __init__(self):
        self.file = ''
        self.declerations=[]
        self.listOfTags = []
        self.listOfText = []
        self.listOfAll = []
        self.listOfErrors = []
        self.tree=tree()
        self.numberOfComments=0
        self.declerationsComments=0
        self.errors=0

    def addFile(self, file):
        self.file = file

    def extractlists(self):
        tagRegEx = re.compile(r'<[^><]+>')
        lineSpaceRegex = re.compile(r'\n\s*')
        textRegEx = re.compile(r'[^⇈↕]+')
        self.listOfTags = tagRegEx.findall(self.file)
        noTags = tagRegEx.sub('⇈', self.file)
        noLineSpace = lineSpaceRegex.sub('↕', noTags) #to take more than 2 texts
        self.listOfText = textRegEx.findall(noLineSpace)
        noText = textRegEx.sub('⇊', noLineSpace)
        self.validateTexts()
        self.validateTags()
        tagIndex = 0
        textIndex = 0
        for i in range(len(noText)):
            if noText[i] == '⇈':
                self.listOfAll.append(self.listOfTags[tagIndex])  #momken 23ml merge lel comments hna momken 2st3'na 3n el list el kbeera
                tagIndex += 1
            elif noText[i] == '⇊':
                if type(self.listOfText[textIndex])==text:
                    self.listOfAll.append(self.listOfText[textIndex])
                textIndex += 1

    def validateTexts(self):
        for i in range(len(self.listOfText)):
            if self.listOfText[i].isspace()!=True:
                #print(self.listOfText[i])
                newText=text()
                newText.originalShape=self.listOfText[i]
                self.errors+=newText.validateText()
                self.listOfText[i] = newText


    def validateTags(self):
        for i in range(len(self.listOfTags)):
            if self.listOfTags[i][1:4]!='!--'and self.listOfTags[i][1]!='?':
                newTag = tag()
                newTag.originalShape=self.listOfTags[i]
                self.errors+=newTag.validateTag()
                self.listOfTags[i]=newTag
            else :
                self.numberOfComments+=1


    def extractDeclerations(self):
        i=0
        while True:
            if type(self.listOfAll[i])==str:
                self.declerationsComments+=1
                self.declerations.append(self.listOfAll[i])
                del self.listOfAll[i]
                i-=1
            else:
                break
            i+=1
    def mergeComments(self):
        comments=self.numberOfComments-self.declerationsComments
        if comments !=0:
            #print('comments')
            for i in range(len(self.listOfAll)):
                #print(i)
               if i>= len(self.listOfAll):
                    break
               if type(self.listOfAll[i])==str:
                    #print(self.listOfAll[i])
                    self.listOfAll[i-1].followingComment=self.listOfAll[i]
                    del self.listOfAll[i]

    def createTree(self):
        for i in range(len(self.listOfAll)):
            #print(len(self.listOfAll))
            if type(self.listOfAll[i])==text:
                self.tree.addText(self.listOfAll[i])
            elif type(self.listOfAll[i]) == tag:
                if self.listOfAll[i].type=='closing':
                    self.tree.addClosingTag(self.listOfAll[i])
                else:
                    self.tree.addOpenningTag(self.listOfAll[i])
    def detectErrors(self):
        return self.errors+self.tree.completeTree()

    def visualizeErrors(self):
        f=open('errorVisualized.txt','w')
        for i in range(len(self.declerations)):
            f.write(self.declerations[i]+ "\n")
        self.tree.visualizeErrors(f)
        f.close()
        f = open('errorVisualized.txt', 'r')
        string = f.read()
        f.close()
        return string
    def prettifying(self):
        f = open('prettifying.txt', 'w')
        for i in range(len(self.declerations)):
            f.write(self.declerations[i] + "\n")
        self.tree.prettifying(f)
        f.close()
        f=open('prettifying.txt', 'r')
        string=f.read()
        f.close()
        return string

s="test"

    def printTree(self):
        f = open('errorVisualized.txt', 'w')
        f.write('self.declerations[i] '+ "\n")
        self.tree.printTree(f)
        f.close()

    def Hypernyms_word(self,string):
        return self.tree.hyper_of_word()


    def getListOfAll(self):
        return self.listOfAll
    def getListOfTags(self):
        return self.listOfTags
    def getListOfTexts(self):
        return self.listOfText









    def json(self):
        return self.tree.print_json()

    def no_of_synsets(self):
        return self.tree.no_synsets()

    def word_def(self,s):
        return self.tree.def_of_word(s)













