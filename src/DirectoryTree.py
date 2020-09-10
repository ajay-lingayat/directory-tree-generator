import os

class TreeGenerator:
   def __init__( self ):
       pass
       
   def generate( self, path ):
       if os.path.exists(path):
          for root, dirs, files in os.walk(path):
              folder = root.replace(path,'')
              Count = folder.count(os.sep)
        
              spaces = ' '*3*Count
        
              print(f'{spaces}+ {os.path.basename(root)}/')
        
              for file in files:
                  sub_space = ' '*4
                  print(f'{spaces}{sub_space}• {file}')
                  
       else:
          raise FileNotFoundError(f"No such file or directory found \'{path}\'")
               

