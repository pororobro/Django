# ***********************
# ------Data Type--------
# ***********************

'''
Python has Five standard types
Numbers : int, float, complex
String : str
Collection : List, Tuple, Dictionary, Set

'''

hello = 'hello'
print(hello)
print('hello')
print(hello[0])
print(hello[2:5])

'''
Python List
'''

# CREATE
# READ
# UPDATE
# DELETE
# List CRUD Example
print('-------------------List--------------------')
ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']
print(f'CREATE:{ls}')
# Create: ls 에 '100'을 추가 Create
ls.append('100')
# Read: ls 의 목록을 출력
print(f'READ:{ls}')
# Update: ls와 tinyls 의 결합
ls = ls + tinyls
print(f'UPDATE:{ls}')
# Delete: ls 에서 786을 제거
ls.remove(786)
print(f'DELETE: {ls}')
print('-------------------Tuple--------------------')
# Tuple CRUD Example
tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')
print(f'CREATE:{tp}')
# Create: tp 에 '100'을 추가 Create
tp1 = list(tp)
tp1.append('100')
print(f'리스트화:{tp1}')
tp = tuple(tp1)
# Read: tp 의 목록을 출력
print(f'READ:{tp}')
# Update: tp와 tinytp 의 결합
tp = tp + tinytp
print(f'UPDATE:{tp}')
# Delete: tp 에서 786을 제거
tp1 = list(tp)
del tp1[1]
tp = tuple(tp1)
print(f'DELETE:{tp}')
# dictionary CRUD Example
dt = {'abcd': 786, 'john': 70.2}
tinydt = {'홍':102, '30세':11}
print(tinydt)
print('-------------------Dictionary--------------------')
print(f'CREATE:{dt}')
# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create
dt.update({'tom':100})
dt['tom'] = 100
# Read: dt 의 목록을 출력
print(f'READ:{dt}')
# Update: dt와 tinydt 의 결합
'''dt.update(tinydt)
print(f'UPDATE:{dt}')'''
dt.update(tinydt)
print(f'UPDATE:{dt}')
# Delete: dt 에서 'abcd' 제거
del dt['abcd']
print(f'DELETE:{dt}')