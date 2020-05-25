
from XmlFile import xmlFile
A=xmlFile()
A.addFile('''<users>
    <user>
        <id>1</id>
        <name>user1</name>
        <posts>
            <post>
                loren ipsum
                tempor incididunt
             </post>
             <post>
                ut enim
                ut aliquip
              </post>
        </posts>
        kkkkkk
        kkkkkl
        <followers>
              <follower>
                    <name>2</name>
               </follower>
               <follower>
                     <id>4</id>
               </follower>
        </followers>

      </user>
      <hello>jjjj</hello>
</users>






''')
A.extractlists()
A.extractDeclerations()
A.mergeComments()
A.createTree()
err=A.detectErrors()
A.minifying()