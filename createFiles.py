import os

for root,dirs, files in os.walk(os.getcwd()):
  print(root, dirs, files)
  if  root.find(".git") == -1:
    f = open(f"{root}/test.txt", "w")
    f.write("yrdy")
    f.close()