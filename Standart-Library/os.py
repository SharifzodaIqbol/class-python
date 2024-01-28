import os

print(os.getcwd()) # C:\Users\USER\Desktop\push\class-python\Standart-Library

print(os.system('mkdir today'))# 1

for i in dir(os):
    print(i,end='\n')

'''DirEntry
EX_OK
F_OK
GenericAlias
Mapping
MutableMapping
O_APPEND
O_BINARY
O_CREAT
O_EXCL
O_NOINHERIT
O_RANDOM
O_RDONLY
O_RDWR
......
'''
print(help(os)) #returns an extensive manual page created from the module's docstrings

