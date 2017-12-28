import os
print(os.getcwd())
save_dir = os.path.join(os.getcwd(), 'saved_models')
print(save_dir)
if(os.path.isfile(os.path.join(save_dir,"Test.txt"))):
   print("file found")
else:
   print("file not found")

   
