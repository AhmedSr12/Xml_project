from XmlFile import xmlFile
A=xmlFile()
A.addFile('''
<root>
  <word>hhhh</word>
  <word>kkkk</word>
</root>
''')
A.extractlists()
A.extractDeclerations()
A.mergeComments()
A.createTree()
err=A.detectErrors()
print(A.json())
