from XmlFile import xmlFile
A=xmlFile()
A.addFile('''
<root>
  <word id="a00001740" type="a">
      hhh
      555
  </word>
</root> 
''')
A.extractlists()
A.extractDeclerations()
A.mergeComments()
A.createTree()
err=A.detectErrors()
print(A.json())
