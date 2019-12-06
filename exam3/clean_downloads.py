"""
import os, time, sys
winuser = os.popen('/mnt/c/Windows/System32/cmd.exe /c "echo %USERNAME%"').read()
#print(winuser)
path_to_watch = "/mnt/c/Users/" + winuser[:-1] + "/Downloads/"
"""
#!/usr/bin/python3
import os

winuser = os.popen('/mnt/c/Windows/System32/cmd.exe /c "echo %USERNAME%"').read()
path_to_watch = "/mnt/c/Users/" + winuser[:-1] + "/Downloads/"
list_files = os.listdir("/mnt/c/Users/" + winuser[:-1] + "/Downloads/")
# list_files = os.listdir(".") # repertoire courant
# print(list_files)
print(type(list_files))
"""
print(list_files[0])
print(list_files[1])
"""
print(list_files[0:99])
# trouver la taille des fichiers
list_files[0:99]
# avec os.stat trouver la taille
# os.stat(list_files[2]) #ne fonctionne pas car il manque le chemin
os.stat("/mnt/c/Users/" + winuser[:-1] + "/Downloads/" + list_files[0:99]) # fonctionne ok
print("toutes les informations du fichier: ", os.stat("/mnt/c/Users/" + winuser[:-1] + "/Downloads/" + list_files[0:99]))
print("id du owner du fichier: ", os.stat("/mnt/c/Users/" + winuser[:-1] + "/Downloads/" + list_files[0:99]).st_uid)
print("taille      du fichier: ", os.stat("/mnt/c/Users/" + winuser[:-1] + "/Downloads/" + list_files[0:99]).st_size)
from pwd import getpwuid
print("txt  owner  du fichier:", getpwuid(os.stat("/mnt/c/Users/" + winuser[:-1] + "/Downloads/" + list_files[0:99]).st_uid).pw_name)
