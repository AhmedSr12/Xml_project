from XmlFile import xmlFile
A=xmlFile()
A.addFile(''' <root> 
      <synset id="a00001740" type="a">
         <lex_filenum>00</lex_filenum>
         <word lex_id="0">able</word>
         hhhhhhhhhhhhhhhhhh
         <pointer refs="n05200169 n05616246">Attribute</pointer>
         <pointer refs="n05616246 n05200169" source="1" target="1">Derivationally related form</pointer>
         <pointer refs="a00002098" source="1" target="1">Antonym</pointer>
         <def>(usually followed by `to') having the necessary means or skill or know-how or authority to do something</def>
         <example>able to swim</example>
         55555555555555
         <example type="a">she was able to program her computer</example>
         <example>we were at last able to buy a car</example>
         <example type="a">able to get a grant for the project</example>
         <frame>
           jjj
           hhhhh
         </frame>
      </synset>
</root>
''')
A.extractlists()
A.extractDeclerations()
A.mergeComments()
print(A.json())
