'''
ls = []
tp = ()
for i in range(1, 10):
    ls.append(i)
print(ls)
tp = ls
tp = tuple(tp)
print(tp)
'''

a = list(range(5))
print(a)

b = [i for i in range(5)]
print(b)

c = [i*2 for i in range(5)]
print(c)

def test(x):
    x = str(x)+'ab'
    return x
print([test(i) for i in range(1,5)])

print([i for i in range(100) if i%10==0])

print([i for i in range(100) if i%10==0 if i%6==0])

print(['even' if i%2==0 else 'odd' for i in range(5)])

print(['even' if i%2==0 else '1' if i==1 else 'odd' for i in range(10)])

'''
if i%2==0 : i가 2로 나누어 떨어지면 i를 그대로 출력
else 'odd-1' if i==1 : 2로 나누어 떨어지지 않으면, i가 1일 때 'odd-1' 출력
else 'odd-3' : 위의 두 조건이 모두 성립하지 않으면 'odd-3' 출력
정리하자면, i가 2로 나누어 떨어지면 그대로 출력하고, 1일 때는 'odd-1'을 출력하고
그렇지 않은 경우는 3밖에 남지 않으므로, 3일 때 'odd-3'이 출력됩니다.
'''

print([(i,j) for i in range(0,3) for j in range(2)])

li=[]
for i in range(3):
    for j in range(2):
        li.append((i,j))
print(li)

print({(i,j) for i in range(2) for j in range(2)})
print({i:j for i in range(2) for j in range(2)})

