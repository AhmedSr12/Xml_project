from Text import text
from Tag import tag
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
                self.listOfAll.append(self.listOfText[textIndex])
                textIndex += 1

    def validateTexts(self):
        for i in range(len(self.listOfText)):
            newText=text()
            newText.originalShape=self.listOfText[i]
            newText.validateText()
            self.listOfText[i] = newText

    def validateTags(self):
        for i in range(len(self.listOfTags)):
            if self.listOfTags[i][1:4]!='!--'and self.listOfTags[i][1]!='?':
                newTag = tag()
                newTag.originalShape=self.listOfTags[i]
                newTag.validateTag()
                self.listOfTags[i]=newTag

    def extractDeclerations(self):
        i=0
        while True:
            if type(self.listOfAll[i])==str:
                self.declerations.append(self.listOfAll[i])
                del self.listOfAll[i]
                i-=1
            else:
                break
            i+=1
    def mergeComments(self):
        for i in range(len(self.listOfAll)):
            if i>= len(self.listOfAll):
                break
            if type(self.listOfAll[i])==str:
                print(self.listOfAll[i])
                self.listOfAll[i-1].followingComment==self.listOfAll[i]
                del self.listOfAll[i]



    def getListOfAll(self):
        return self.listOfAll
    def getListOfTags(self):
        return self.listOfTags
    def getListOfTexts(self):
        return self.listOfText












