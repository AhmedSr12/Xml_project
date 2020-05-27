from Text import text
from Tag import tag
from Tree import tree
import re

class xmlFile:
    def __init__(self):
        self.file = ''
        self.declerations=[]
        self.listOfTags = []
        self.listOfText = []
        self.listOfAll = []
        self.xmlTree=tree()
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
        noLineSpace = lineSpaceRegex.sub('↕', noTags)
        self.listOfText = textRegEx.findall(noLineSpace)
        noText = textRegEx.sub('⇊', noLineSpace)
        self.validateTexts()
        self.validateTags()
        tagIndex = 0
        textIndex = 0
        for i in range(len(noText)):
            if noText[i] == '⇈':
                self.listOfAll.append(self.listOfTags[tagIndex])
                tagIndex += 1
            elif noText[i] == '⇊':
                if type(self.listOfText[textIndex])==text:
                    self.listOfAll.append(self.listOfText[textIndex])
                textIndex += 1

    def validateTexts(self):
        for i in range(len(self.listOfText)):
            if self.listOfText[i].isspace()!=True:
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
            for i in range(len(self.listOfAll)):
               if i>= len(self.listOfAll):
                    break
               if type(self.listOfAll[i])==str:
                    self.listOfAll[i-1].followingComment=self.listOfAll[i]
                    del self.listOfAll[i]

    def createTree(self):
        self.extractlists()
        self.extractDeclerations()
        self.mergeComments()
        for i in range(len(self.listOfAll)):
            if type(self.listOfAll[i])==text:
                self.xmlTree.addText(self.listOfAll[i])
            elif type(self.listOfAll[i]) == tag:
                if self.listOfAll[i].type=='closing':
                    self.xmlTree.addClosingTag(self.listOfAll[i])
                else:
                    self.xmlTree.addOpenningTag(self.listOfAll[i])
    def detectErrors(self):
        return self.errors+self.xmlTree.completeTree()

    def visualizeErrors(self):
        f=open('errorVisualized.txt','w')
        for i in range(len(self.declerations)):
            f.write(self.declerations[i]+ "\n")
        self.xmlTree.visualizeErrors(f)
        f.close()
        f = open('errorVisualized.txt', 'r')
        string = f.read()
        f.close()
        return string
    def prettifying(self):
        f = open('prettifying.txt', 'w')
        for i in range(len(self.declerations)):
            f.write(self.declerations[i] + "\n")
        self.xmlTree.prettifying(f)
        f.close()
        f=open('prettifying.txt', 'r')
        string=f.read()
        f.close()
        return string

    def minifying(self):
        f = open('minifying.txt', 'w')
        for i in range(len(self.declerations)):
            f.write(self.declerations[i] + "\n")
        self.xmlTree.minifying(f)
        f.close()
        f = open('minifying.txt', 'r')
        string = f.read()
        f.close()
        return string



    def Hypernyms_word(self,string):
        return self.xmlTree.hyper_of_word(string)



    def json(self):
        return self.xmlTree.print_json()

    def no_of_synsets(self):
        return self.xmlTree.no_synsets()

    def word_def(self,s):
        return self.xmlTree.def_of_word(s)













