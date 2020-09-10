# directory-tree-generator

## Requirements

```
python >= 3.0
```

## Installation
```
pip install directory-tree-generator
```

## Usage
Pass the directory path to the generate method

```python
from DirectoryTree import TreeGenerator
Tree = TreeGenerator()
Tree.generate('C:/users/Ajay/Desktop/Junk')
```

Output
```
+ Junk/
   + Stylesheets/
       • country.css
   + Java Files/
       • mm.java
   + Media/
      + Images/
          • globe.png
          • 1598791605362.jpg
      + GIFs/
          • connection_11598806195526.gif
      + Audios/
          • Sound.mp3
   + Database Files/
       • db.sqlite3
   + PDFs/
       • Pdf.pdf
   + Javascript Files/
       • app.js
   + Python Files/
       • Notepad.py
   + Text Files/
       • requirements.txt
   + HTML Files/
       • share.html
   + Json Files/
       • package-lock.json
   + Documents/
       • DBMS_ALL Programs.docx
   + Readme Files/
       • README.md
```
