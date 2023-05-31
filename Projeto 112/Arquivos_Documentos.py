import os
import shutil

from_dir = "C:/Users\pc\Downloads"
to_dir = "C:/Users\pc\Desktop\Python\Projetos\Projeto 111"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for files in list_of_files:
    name,extention = os.path.splitext(files)
    print(name)
    print(extention)

    if extention == "":
        continue
    if extention in lista [ ".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+"/"+files
        path2 = to_dir+"/"+"Arquivos_Documentos"
        path3 = to_dir+"/"+"Arquivos_Documentos"+"/"+files