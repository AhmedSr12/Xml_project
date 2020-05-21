from XmlFile import xmlFile
A=xmlFile()
A.addFile('''

''')
A.extractlists()
A.extractDeclerations()
A.mergeComments()
A.createTree()
err=A.detectErrors()
print(A.json())
