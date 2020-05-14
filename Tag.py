from Attribute import attribute
import re
class tag:
    def __init__(self):
        self.name=''
        self.type=''
        self.originalShape=''
        self.errorvisualized=''
        self.finalShape=''
        self.listOfAttributes=[]
        self.followingComment=''
    def validateTag(self):
        partitionsRegEx = re.compile(r'[^<>\s]+')
        if self.originalShape[1] == '/':
            self.type = 'closing'
        elif self.originalShape[-2] == '/':
            self.type = 'empty'
            partitionsList = partitionsRegEx.findall(self.originalShape)
            self.name = partitionsList[0]
            self.listOfAttributes = self.extracAttributesList(partitionsList,'empty')
        else:
            self.type = 'opening'
            partitionsList = partitionsRegEx.findall(self.originalShape)
            self.name = partitionsList[0]
            self.listOfAttributes = self.extracAttributesList(partitionsList,'opening')
        self.createShapes()

    def extracAttributesList(self,partitions,type):
        del partitions[0]
        if len(partitions) != 0:
            i = 0
            while True:  # merge
                if i >= len(partitions):
                    break
                if i > 0:
                    if '=' not in partitions[i]:
                        partitions[i - 1] = partitions[i - 1] + ' ' + partitions[i]
                        del partitions[i]
                        i -= 1
                i += 1
            for i in range(len(partitions)):
                newAttribute = attribute()
                newAttribute.name = partitions[i].split('=')[0]
                if i==len(partitions)-1:

                    if type=='empty':
                        value=partitions[i].split('=')[1]
                        newAttribute.value = value[0:len(value)-1]
                    else:
                        newAttribute.value=partitions[i].split('=')[1]
                else:
                    newAttribute.value = partitions[i].split('=')[1]
                newAttribute.validateAttribute()
                partitions[i] = newAttribute

        return partitions
    def validateListOfAttributes(self):
        d=11111111111111
    def createShapes(self):
        if self.type=='closing':
            self.errorvisualized=self.originalShape
            self.finalShape=self.originalShape
        elif self.type=='empty':
            attributesErrors=''
            attributesFinal=''
            for i in range(len(self.listOfAttributes)):
                attributesErrors=attributesErrors+self.listOfAttributes[i].name+'='+self.listOfAttributes[i].valueWithError
                attributesFinal=attributesFinal+self.listOfAttributes[i].name+'='+self.listOfAttributes[i].finalShape
                if i !=len(self.listOfAttributes)-1:
                    attributesErrors+=' '
                    attributesFinal = ' '
            self.errorvisualized='<'+self.name+' '+attributesErrors+'/'+'>'
            self.finalShape='<'+self.name+' '+attributesFinal+'/'+'>'

        elif self.type=='opening':
            attributesErrors = ''
            attributesFinal = ''
            for i in range(len(self.listOfAttributes)):
                attributesErrors=attributesErrors+self.listOfAttributes[i].name+'='+self.listOfAttributes[i].valueWithError
                attributesFinal=attributesFinal+self.listOfAttributes[i].name+'='+self.listOfAttributes[i].finalShape
                if i !=len(self.listOfAttributes)-1:
                    attributesErrors+=' '
                    attributesFinal = ' '
            self.errorvisualized = '<' + self.name + ' ' + attributesErrors + '>'
            self.finalShape = '<' + self.name + ' ' + attributesFinal + '>'




        #self.errorvisualized = '<'+
        s=1