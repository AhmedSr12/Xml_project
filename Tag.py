from Attribute import attribute
import re
class tag:
    def __init__(self):
        self.name=''
        self.type='no'
        self.originalShape=''
        self.errorvisualized=''
        self.finalShape=''
        self.listOfAttributes=[]
        self.followingComment=''
        self.errors=0
    def validateTag(self):
        partitionsRegEx = re.compile(r'[^<>\s]+')  #attribute value or name don't have spaces or /??
        if self.originalShape[1] == '/':
            self.name=self.originalShape[2:len(self.originalShape)-1]
            self.type = 'closing'
        elif self.originalShape[-2] == '/': #lazem yb2a laze2
            self.type = 'empty'
            partitionsList = partitionsRegEx.findall(self.originalShape)
            if len(partitionsList)==1:
               self.name = partitionsList[0][0:len(partitionsList[0])-1]
            else:
                self.name = partitionsList[0]

            self.listOfAttributes = self.extracAttributesList(partitionsList,'empty')
        else:
            self.type = 'opening'
            partitionsList = partitionsRegEx.findall(self.originalShape)
            self.name = partitionsList[0]
            self.listOfAttributes = self.extracAttributesList(partitionsList,'opening')
        self.createShapes()
        return self.errors

    def extracAttributesList(self,partitions,type):
        del partitions[0]
        if len(partitions)>=1:
            if partitions[-1]=='/':
                del partitions[-1]

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
                        if value[-1]=='/':
                            newAttribute.value = value[0:len(value)-1]
                        else:
                            newAttribute.value = value
                    else:
                        newAttribute.value=partitions[i].split('=')[1]
                else:
                    newAttribute.value = partitions[i].split('=')[1]
                self.errors+=newAttribute.validateAttribute()
                partitions[i] = newAttribute

        return partitions
    def validateListOfAttributes(self):
        d=11111111111111
    def createShapes(self):  #25tsr de law mfee4 errors
        if self.type=='closing':
            self.errorvisualized=self.originalShape
            self.finalShape=self.originalShape
        elif self.type=='empty':
            attributesErrors=''
            attributesFinal=''
            for i in range(len(self.listOfAttributes)):
                if i == 0:
                    attributesErrors = ' '
                    attributesFinal = ' '
                attributesErrors=attributesErrors+self.listOfAttributes[i].name+'='+self.listOfAttributes[i].valueWithError
                attributesFinal=attributesFinal+self.listOfAttributes[i].name+'='+self.listOfAttributes[i].finalShape
                if i !=len(self.listOfAttributes)-1:
                    attributesErrors+=' '
                    attributesFinal += ' '
            self.errorvisualized='<'+self.name+attributesErrors+'/'+'>'
            self.finalShape='<'+self.name+attributesFinal+'/'+'>'

        elif self.type=='opening':
            attributesErrors = ''
            attributesFinal = ''
            for i in range(len(self.listOfAttributes)):
                if i==0:
                   attributesErrors = ' '
                   attributesFinal = ' '
                attributesErrors=attributesErrors+self.listOfAttributes[i].name+'='+self.listOfAttributes[i].valueWithError
                attributesFinal=attributesFinal+self.listOfAttributes[i].name+'='+self.listOfAttributes[i].finalShape
                if i !=len(self.listOfAttributes)-1:
                    attributesErrors+=' '
                    attributesFinal += ' '
            self.errorvisualized = '<' + self.name + attributesErrors + '>'
            self.finalShape = '<' + self.name + attributesFinal + '>'




        #self.errorvisualized = '<'+
        s=1