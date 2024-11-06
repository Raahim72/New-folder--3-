new_file = open('han' , 'w')
new_file.close()

import os
print("checking if my file_exists or not......")
if os.path.exists("my_file.txt"):
 os.remove("han")
else:
 print("the file does not exist")

my_file = open ("han" , "w")
my_file.write ("hi iam penguin im 1 year old")
my_file.close()

os.remove('han')

os.rmdir('folder')

