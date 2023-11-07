import os
os.path.join
dirs = [
  os.path.join('data','raw'),    #since folder inside an folder is created use os.path.join
  os.path.join('data','processed'),    #since folder inside an folder is created use os.path.join
  'notebooks',                    #here only one folder is created no need to use the join
  'saved_models',                   #here only one folder is created no need to use the join
  'src'
  
 ]



for i in dirs:

    os.makedirs(i,exist_ok=True)                              #wheever this file is executed it will create these folders and inside that it keeps "gitkeep"
    with open(os.path.join(i,".gitkeep"),'w') as f:
       pass

#creating dir sturuct below code
file = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join('src','__init__.py')
    

]

for j in file:
    with open(j,'w') as f:
        pass