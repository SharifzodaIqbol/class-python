import re

print(re.findall(r'f[a-z]*', 'which foot or hand fell fastest')) # 'foot', 'fell', 'fastest'

print(re.sub(r'([a-z]+) \1', r'\1', 'cat in the the hat')) # cat in the hat

string = 'tea for too'

print(string.replace('too', 'two')) #tea for two

