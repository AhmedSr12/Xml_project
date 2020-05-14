from XmlFile import xmlFile
A=xmlFile()
A.addFile('''  <ahmed>hhhhh</ahmed>
</omar>

''')
A.extractlists()
#A.validateTexts()
A.extractDeclerations()
A.mergeComments()
list=A.getListOfTexts()
list2=A.getListOfAll()
print(len(list2))
print(len(list))
for i in range (len(list)):
    g=1
#    print(list[i].finalShape)
#    print(list[i].errorvisualized)