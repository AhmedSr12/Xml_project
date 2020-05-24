from XmlFile import xmlFile
A=xmlFile()
A.addFile('''
<synsets source="dict/data.noun" xml:base="data.noun.xml"><!--10 out of 82115 elements-->
      <synset id="n00001740" type="n">
         <lex_filenum>03</lex_filenum>
         <word lex_id="0">entity</word>
         <pointer refs="n00001930 n00002137 n04424418">Hyponym</pointer>
         <def>that which is perceived or known or inferred to have its own distinct existence (living or nonliving)</def>
      </synset>
      <synset id="n01608265" type="n">
         <lex_filenum>05</lex_filenum>
         <word lex_id="0">honey buzzard</word>
         <word lex_id="0">Pernis apivorus</word>
         <pointer refs="n01605630">Hypernym</pointer>
         <pointer refs="n01608086">Member holonym</pointer>
         <def>Old World hawk that feeds on bee larvae and small rodents and reptiles</def>
      </synset>
      <synset id="n03037590" type="n">
         <lex_filenum>06</lex_filenum>
         <word lex_id="0">clarence</word>
         <pointer refs="n02968473">Hypernym</pointer>
         <def>a closed carriage with four wheels and seats for four passengers</def>
      </synset>
      <synset id="n04421740" type="n">
         <lex_filenum>06</lex_filenum>
         <word lex_id="0">thermojunction</word>
         <pointer refs="n03605915">Hypernym</pointer>
         <def>a junction between two dissimilar metals across which a voltage appears</def>
      </synset>
      <synset id="n06013298" type="n">
         <lex_filenum>09</lex_filenum>
         <word lex_id="0">vector algebra</word>
         <pointer refs="n06012726">Hypernym</pointer>
         <pointer refs="n06000644">Domain of synset - TOPIC</pointer>
         <pointer refs="n06013471">Hyponym</pointer>
         <def>the part of algebra that deals with the theory of vectors and vector spaces</def>
      </synset>
      <synset id="n07581132" type="n">
         <lex_filenum>13</lex_filenum>
         <word lex_id="0">confit</word>
         <pointer refs="n07653394">Hypernym</pointer>
         <def>a piece of meat (especially a duck) cooked slowly in its own fat</def>
      </synset>
      <synset id="n09168592" type="n">
         <lex_filenum>15</lex_filenum>
         <word lex_id="0">Black Rock Desert</word>
         <pointer refs="n08505573">Instance Hypernym</pointer>
         <pointer refs="n09110422">Part holonym</pointer>
         <def>a desert in northwestern Nevada</def>
      </synset>
      <synset id="n10604089" type="n">
         <lex_filenum>18</lex_filenum>
         <word lex_id="0">sitting duck</word>
         <word lex_id="0">easy mark</word>
         <pointer refs="n10752480">Hypernym</pointer>
         <def>a defenseless victim</def>
      </synset>
      <synset id="n12200143" type="n">
         <lex_filenum>20</lex_filenum>
         <word lex_id="0">looking-glass plant</word>
         <word lex_id="0">Heritiera littoralis</word>
         <pointer refs="n13109733">Hypernym</pointer>
         <def>small tree of coastal regions of Old World tropics whose leaves are silvery beneath</def>
      </synset>
      <synset id="n13804375" type="n">
         <lex_filenum>24</lex_filenum>
         <word lex_id="0">paradigm</word>
         <pointer refs="n13803782">Hypernym</pointer>
         <pointer refs="a02965552" source="1" target="1">Derivationally related form</pointer>
         <def>systematic arrangement of all the inflected forms of a word</def>
      </synset>
   </synsets>''')
A.extractlists()
A.extractDeclerations()
A.mergeComments()
A.createTree()
err=A.detectErrors()
print(A.Hypernyms_word('clarence'))
#print(A.json())
#print(A.no_of_synsets())
#print(A.word_def('able'))
