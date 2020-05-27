class text:
    def __init__(self):
        self.originalShape=''
        self.errorvisualized=''
        self.finalShape=''
        self.followingComment=''
        self.errors=0
    def validateText(self):
        self.finalShape = self.originalShape
        self.errorvisualized = self.originalShape
        if '<' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('<', '(ERR:Using <)')
            self.finalShape = self.finalShape.replace('<', '&lt;')
            self.errors+=1
        if '>' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('>', '(ERR:Using >)')
            self.finalShape = self.finalShape.replace('>', '&gt;')
            self.errors += 1
        if '&' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('&', '(ERR:Using &)')
            self.errorvisualized = self.errorvisualized.replace('(ERR:Using &)' + 'amp;', '&amp;')
            self.finalShape = self.finalShape.replace('&', '&amp;')
            self.finalShape = self.finalShape.replace('&amp;amp;', '&amp;')
            self.errors += 1
        if '\'' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('\'', "(ERR:Using \')")
            self.finalShape = self.finalShape.replace('\'', '&apos;')
            self.errors += 1
        if '\"' in self.originalShape:
            self.errorvisualized = self.errorvisualized.replace('\"', "(ERR:Using \")")
            self.finalShape = self.finalShape.replace('\"', '&quot;')
            self.errors += 1
        return self.errors