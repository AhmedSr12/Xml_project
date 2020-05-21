class attribute:
    def __init__(self):
        self.name=''
        self.value=''
        self.valueWithError=''
        self.finalShape=''
        self.errors=0
    def validateAttribute(self):
        self.valueWithError =self.value
        self.finalShape = self.value
        if self.valueWithError[0]!='"':
            self.valueWithError="(ERR:missing \")"+self.valueWithError
            self.finalShape = '"'+self.finalShape
            self.errors+=1

        if self.valueWithError[-1]!='"':
            self.valueWithError=self.valueWithError+"(ERR:Missing \")"
            self.finalShape = self.finalShape+'"'
            self.errors+=1
        return self.errors