class attribute:
    def __init__(self):
        self.name=''
        self.value=''
        self.valueWithError=''
        self.finalShape=''
    def validateAttribute(self):
        self.valueWithError =self.value
        self.finalShape = self.value
        if self.valueWithError[0]!='"':
            self.valueWithError='〔ERROR6〕'+self.valueWithError
            self.finalShape = '"'+self.finalShape

        if self.valueWithError[-1]!='"':
            self.valueWithError=self.valueWithError+'〔ERROR6〕'
            self.finalShape = self.finalShape+'"'