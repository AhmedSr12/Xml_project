class text:
    def __init__(self):
        self.originalShape='' #may be deleted
        self.errorvisualized=''
        self.finalShape=''
        self.followingComments=''
        self.followingComment=''
    def validateText(self):
        self.finalShape = self.originalShape
        self.errorvisualized = self.originalShape
        if '<' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('<', '〔ERROR1〕')
            self.finalShape = self.finalShape.replace('<', '&lt')
        if '>' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('>', '〔ERROR2〕')
            self.finalShape = self.finalShape.replace('>', '&gt')
        if '&' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('&', '〔ERROR3〕')
            self.errorvisualized = self.errorvisualized.replace('〔ERROR3〕' + 'amp', '&amp')
            self.finalShape = self.finalShape.replace('&', '&amp')
            self.finalShape = self.finalShape.replace('&ampamp', '&amp')
        if '\'' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('\'', '〔ERROR4〕')
            self.finalShape = self.finalShape.replace('\'', '&apos')
        if '\"' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('\"', '〔ERROR5〕')
            self.finalShape = self.finalShape.replace('\"', '&quot')