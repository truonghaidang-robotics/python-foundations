set1 = {23, 56, 78, 21, 56}
print(set1)
21 in set1
len(set1)
print(21 in set1)
print(len(set1))
print(type (set1))
set2 = set('anchefihe')
print(set2)
set3 = set('hjuisjfw')
print(set3-set2)
print(set2&set3)
print(set2|set3)

date = {'haidang':34, 'john':23, 'jane':45, 'bob':57}
print(date['haidang'])
print(date.get('john'))
keys = ['navin', 'histesh', 'hdang']
values = [34, 64,87]
dict1 = dict(zip(keys,values))
print(dict1)
date = {'js':'vscode', 'python': ['vscode', 'pychamr'], 'java': {'core': 'vscode', 'spring': 'iij'}}
print(date)
print(date['js'])
print(date['python'][1])
print(date['java']['core'])
